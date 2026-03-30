#!/usr/bin/env python3
"""
Lightweight stoploss checker. Runs frequently (every 10 min via cron).
Uses ON-CHAIN positions as ground truth (not ledger).
Cross-references ledger for entry prices.
Exits with code 1 if any stoploss triggered (for cron alerting).
"""
import json, os, urllib.request, sys

BOT_DIR = os.path.expanduser("~/clawd/projects/polymarket-bot")
LEDGER = os.path.join(BOT_DIR, "trade_ledger.json")
GAMMA = "https://gamma-api.polymarket.com"
ON_CHAIN_API = "https://data-api.polymarket.com/positions?user=0x3df911149339b7ed777cfc340ffc01c2f3a12e43&sizeThreshold=0"
STOPLOSS_PCT = -25  # exit at -25%
HEADERS = {"User-Agent": "PolymarketBot/1.0"}


def get_on_chain_positions():
    """Fetch current on-chain positions — the ONLY ground truth."""
    req = urllib.request.Request(ON_CHAIN_API, headers=HEADERS)
    data = json.loads(urllib.request.urlopen(req, timeout=10).read())
    return data if isinstance(data, list) else []


def get_ledger_entries():
    """Load ledger for entry price reference."""
    try:
        with open(LEDGER) as f:
            ledger = json.load(f)
        entries = {}
        for t in ledger.get("trades", []):
            if t.get("status") in ("cancelled", "closed"):
                continue
            token = t.get("token_id")
            if not token:
                continue
            price = t.get("price", t.get("entry_price"))
            if price is None:
                continue
            price = float(price)
            size = float(t.get("size", t.get("shares", t.get("amount_shares", 0))))
            if token not in entries:
                entries[token] = {"total_cost": 0, "total_size": 0}
            trade_side = t.get("action", t.get("side", "BUY"))
            if trade_side in ("Yes", "No"):
                trade_side = "BUY"
            if trade_side == "BUY":
                entries[token]["total_cost"] += size * price
                entries[token]["total_size"] += size
        # Compute avg entry
        for token, e in entries.items():
            if e["total_size"] > 0:
                e["avg_entry"] = e["total_cost"] / e["total_size"]
            else:
                e["avg_entry"] = 0
        return entries
    except Exception as ex:
        print(f"WARNING: Could not load ledger: {ex}")
        return {}


def get_gamma_price(token_id):
    """Get current price from Gamma API."""
    url = f"{GAMMA}/markets?clob_token_ids={token_id}&limit=1"
    req = urllib.request.Request(url, headers=HEADERS)
    data = json.loads(urllib.request.urlopen(req, timeout=5).read())
    if not data:
        return None
    tokens = json.loads(data[0].get("clobTokenIds", "[]"))
    prices = json.loads(data[0].get("outcomePrices", "[]"))
    if token_id == tokens[0]:
        return float(prices[0])
    elif len(tokens) > 1 and token_id == tokens[1]:
        return float(prices[1])
    return float(prices[0]) if prices else None


def check():
    # Get on-chain positions (ground truth)
    positions = get_on_chain_positions()
    if not positions:
        print("⚠️  Could not fetch on-chain positions")
        return 0

    # Get ledger for entry prices
    ledger_entries = get_ledger_entries()

    triggered = []
    checked = 0

    for pos in positions:
        size = float(pos.get("size", 0))
        if size < 1:
            continue

        token_id = pos.get("asset", "")
        market_title = pos.get("title", pos.get("market", "Unknown"))
        outcome = pos.get("outcome", "?")

        # Get entry price: prefer on-chain avgPrice, fall back to ledger
        avg_entry = float(pos.get("avgPrice", 0))
        if avg_entry <= 0 and token_id in ledger_entries:
            avg_entry = ledger_entries[token_id]["avg_entry"]
        if avg_entry <= 0:
            # Can't check without entry price
            continue

        # Get current price
        try:
            # On-chain curPrice if available
            current = float(pos.get("curPrice", 0))
            if current <= 0:
                current = get_gamma_price(token_id)
            if current is None or current <= 0:
                continue
        except:
            continue

        checked += 1
        pnl_pct = ((current - avg_entry) / avg_entry) * 100

        if pnl_pct <= STOPLOSS_PCT:
            triggered.append({
                "market": market_title,
                "outcome": outcome,
                "entry": avg_entry,
                "current": current,
                "pnl_pct": pnl_pct,
                "shares": size,
                "token": token_id,
            })
            print(f"🚨 STOPLOSS: {market_title[:50]} ({outcome}) — {pnl_pct:+.1f}% (entry={avg_entry:.3f} now={current:.3f})")

    if not triggered:
        print(f"✅ All {checked} positions OK")
        return 0

    # Write triggered positions for cron to act on
    with open(os.path.join(BOT_DIR, "stoploss_triggered.json"), "w") as f:
        json.dump(triggered, f, indent=2)

    return 1


if __name__ == "__main__":
    sys.exit(check())
