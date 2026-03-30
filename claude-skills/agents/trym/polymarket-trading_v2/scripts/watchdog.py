#!/usr/bin/env python3
"""
PM Watchdog — Independent fallback for PM stalls.
Runs via cron every 30 minutes. Does NOT depend on Claude or Agent Teams.

Checks:
1. Was team_context.md updated recently? (PM activity indicator)
2. Was check_stoploss.py run recently? (monitoring gap detection)
3. Are any positions past -25% stoploss right now? (emergency check)

If issues found → sends Telegram alert to Gaute.
If position past -25% and PM hasn't acted → executes emergency exit.

Setup:
  crontab -e
  */30 * * * * cd ~/clawd/projects/polymarket-bot && python3 scripts/watchdog.py

Environment:
  TELEGRAM_BOT_TOKEN — Bot token from @BotFather
  TELEGRAM_CHAT_ID — Gaute's chat ID
  (or store in ~/.watchdog_config.json)
"""

import json, os, sys, time, urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

BOT_DIR = Path(os.path.expanduser("~/clawd/projects/polymarket-bot"))
TEAM_CONTEXT = BOT_DIR / "team_context.md"
STOPLOSS_LOG = BOT_DIR / "stoploss_last_run.txt"
TRADE_LEDGER = BOT_DIR / "trade_ledger.json"
CONFIG_FILE = Path(os.path.expanduser("~/.watchdog_config.json"))

# Thresholds
CONTEXT_STALE_HOURS = 2       # Alert if team_context.md older than this
STOPLOSS_STALE_MINUTES = 45   # Alert if stoploss check older than this (30min interval + buffer)
STOPLOSS_THRESHOLD = -0.25    # -25% hard floor

ON_CHAIN_API = "https://data-api.polymarket.com/positions?user=0x3df911149339b7ed777cfc340ffc01c2f3a12e43&sizeThreshold=0"
GAMMA_API = "https://gamma-api.polymarket.com"
HEADERS = {"User-Agent": "PolymarketWatchdog/1.0"}


def load_config():
    """Load Telegram credentials from env or config file."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE) as f:
                cfg = json.load(f)
            token = token or cfg.get("telegram_bot_token")
            chat_id = chat_id or cfg.get("telegram_chat_id")

    if not token or not chat_id:
        print("ERROR: Telegram credentials not configured.")
        print(f"Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID env vars, or create {CONFIG_FILE}")
        sys.exit(1)

    return token, chat_id


def send_telegram(token, chat_id, message):
    """Send a message via Telegram Bot API."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = json.dumps({"chat_id": chat_id, "text": message, "parse_mode": "HTML"}).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=10)
        print(f"Telegram alert sent: {message[:80]}...")
    except Exception as e:
        print(f"ERROR sending Telegram: {e}")


def check_file_freshness(filepath, max_age_minutes):
    """Check if a file was modified within max_age_minutes. Returns (is_fresh, age_minutes)."""
    if not filepath.exists():
        return False, float("inf")
    mtime = datetime.fromtimestamp(filepath.stat().st_mtime, tz=timezone.utc)
    age = datetime.now(timezone.utc) - mtime
    age_minutes = age.total_seconds() / 60
    return age_minutes <= max_age_minutes, round(age_minutes)


def get_on_chain_positions():
    """Fetch current on-chain positions."""
    try:
        req = urllib.request.Request(ON_CHAIN_API, headers=HEADERS)
        data = json.loads(urllib.request.urlopen(req, timeout=10).read())
        return data if isinstance(data, list) else []
    except Exception as e:
        print(f"ERROR fetching on-chain positions: {e}")
        return []


def get_current_price(token_id):
    """Get current price for a token from Gamma API."""
    try:
        url = f"{GAMMA_API}/markets?clob_token_ids={token_id}&limit=1"
        req = urllib.request.Request(url, headers=HEADERS)
        data = json.loads(urllib.request.urlopen(req, timeout=5).read())
        if data:
            tokens = json.loads(data[0].get("clobTokenIds", "[]"))
            prices = json.loads(data[0].get("outcomePrices", "[]"))
            if token_id == tokens[0]:
                return float(prices[0])
            elif len(tokens) > 1 and token_id == tokens[1]:
                return float(prices[1])
        return None
    except:
        return None


def get_entry_prices():
    """Get average entry prices from trade ledger."""
    if not TRADE_LEDGER.exists():
        return {}

    with open(TRADE_LEDGER) as f:
        ledger = json.load(f)

    positions = {}
    for t in ledger.get("trades", []):
        key = t.get("token_id", t.get("token", ""))
        if not key:
            continue
        if key not in positions:
            positions[key] = {"buy_size": 0, "buy_cost": 0, "sell_size": 0}
        if t.get("side") == "BUY":
            positions[key]["buy_size"] += t.get("size", 0)
            positions[key]["buy_cost"] += t.get("size", 0) * t.get("price", 0)
        else:
            positions[key]["sell_size"] += t.get("size", 0)

    entries = {}
    for key, pos in positions.items():
        net = pos["buy_size"] - pos["sell_size"]
        if net > 0.5 and pos["buy_size"] > 0:
            entries[key] = pos["buy_cost"] / pos["buy_size"]

    return entries


def check_stoploss_violations():
    """Check if any position is past the -25% stoploss."""
    entry_prices = get_entry_prices()
    if not entry_prices:
        return []

    violations = []
    for token_id, entry_price in entry_prices.items():
        current = get_current_price(token_id)
        if current is None:
            continue

        pnl_pct = (current - entry_price) / entry_price if entry_price > 0 else 0

        if pnl_pct <= STOPLOSS_THRESHOLD:
            violations.append({
                "token_id": token_id,
                "entry": round(entry_price, 4),
                "current": round(current, 4),
                "pnl_pct": round(pnl_pct * 100, 1),
            })

    return violations


def main():
    token, chat_id = load_config()
    alerts = []
    now = datetime.now(timezone.utc)

    # Check 1: team_context.md freshness
    fresh, age = check_file_freshness(TEAM_CONTEXT, CONTEXT_STALE_HOURS * 60)
    if not fresh:
        if age == float("inf"):
            alerts.append("team_context.md does not exist — PM may not have initialized")
        else:
            alerts.append(f"team_context.md is {age} minutes old (threshold: {CONTEXT_STALE_HOURS}h) — PM may be stalled")

    # Check 2: stoploss check freshness
    fresh, age = check_file_freshness(STOPLOSS_LOG, STOPLOSS_STALE_MINUTES)
    if not fresh:
        if age == float("inf"):
            alerts.append("No stoploss check log found — monitoring may not be running")
        else:
            alerts.append(f"Last stoploss check was {age} minutes ago (threshold: {STOPLOSS_STALE_MINUTES}min) — monitoring gap")

    # Check 3: stoploss violations
    violations = check_stoploss_violations()
    for v in violations:
        alerts.append(
            f"STOPLOSS BREACH: token {v['token_id'][:20]}... "
            f"entry={v['entry']} current={v['current']} P&L={v['pnl_pct']}%"
        )

    # Report
    if alerts:
        message = (
            "⚠️ <b>PM WATCHDOG ALERT</b>\n"
            f"Time: {now.strftime('%Y-%m-%d %H:%M UTC')}\n\n"
            + "\n".join(f"• {a}" for a in alerts)
        )

        if violations:
            message += (
                "\n\n🚨 <b>Emergency stoploss exit may be required.</b>\n"
                "If PM is not responding, manual intervention needed."
            )
            # Future: auto-execute emergency exit via trade.py
            # For v1, alert only — manual execution is safer until watchdog is battle-tested

        send_telegram(token, chat_id, message)
        print(f"ALERT: {len(alerts)} issue(s) detected")
    else:
        print(f"OK: All checks passed at {now.strftime('%H:%M UTC')}")


if __name__ == "__main__":
    main()
