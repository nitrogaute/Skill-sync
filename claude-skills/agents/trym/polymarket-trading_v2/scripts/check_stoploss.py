#!/usr/bin/env python3
"""
Lightweight stoploss checker. Runs frequently (every 5-10 min).
Only checks prices — no research, no scanning, no dashboard rebuild.
Exits with code 1 if any stoploss triggered (for cron alerting).
"""
import json, os, urllib.request, sys

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
BOT_DIR = os.path.join(os.path.dirname(SKILL_DIR), "..", "..", "projects", "polymarket-bot")
# Normalize
BOT_DIR = os.path.expanduser("~/clawd/projects/polymarket-bot")
LEDGER = os.path.join(BOT_DIR, "trade_ledger.json")
GAMMA = "https://gamma-api.polymarket.com"
STOPLOSS_PCT = -25  # exit at -25%

def check():
    with open(LEDGER) as f:
        ledger = json.load(f)
    
    # Build net positions
    positions = {}
    for t in ledger.get("trades", []):
        key = f"{t['market']}|{t.get('outcome','Yes')}"
        if key not in positions:
            positions[key] = {"token": t["token_id"], "buy_size": 0, "buy_cost": 0, "sell_size": 0, "market": t["market"], "outcome": t.get("outcome", "Yes")}
        s = t["size"]
        if t["side"] == "BUY":
            positions[key]["buy_size"] += s
            positions[key]["buy_cost"] += s * t["price"]
        else:
            positions[key]["sell_size"] += s
    
    triggered = []
    for key, pos in positions.items():
        net = pos["buy_size"] - pos["sell_size"]
        if net < 1:
            continue
        avg_entry = pos["buy_cost"] / pos["buy_size"]
        
        # Get current price
        try:
            token = pos["token"]
            url = f"{GAMMA}/markets?clob_token_ids={token}&limit=1"
            req = urllib.request.Request(url, headers={"User-Agent": "PolymarketBot/1.0"})
            data = json.loads(urllib.request.urlopen(req, timeout=5).read())
            if data:
                tokens = json.loads(data[0].get("clobTokenIds", "[]"))
                prices = json.loads(data[0].get("outcomePrices", "[]"))
                if token == tokens[0]:
                    current = float(prices[0])
                elif len(tokens) > 1 and token == tokens[1]:
                    current = float(prices[1])
                else:
                    current = float(prices[0])
            else:
                continue
        except:
            continue
        
        pnl_pct = ((current - avg_entry) / avg_entry) * 100
        
        if pnl_pct <= STOPLOSS_PCT:
            triggered.append({
                "market": pos["market"],
                "outcome": pos["outcome"],
                "entry": avg_entry,
                "current": current,
                "pnl_pct": pnl_pct,
                "shares": net,
                "token": token,
            })
            print(f"🚨 STOPLOSS: {pos['market'][:45]} ({pos['outcome']}) — {pnl_pct:+.1f}% (entry={avg_entry:.3f} now={current:.3f})")
    
    if not triggered:
        print(f"✅ All {len([k for k,v in positions.items() if v['buy_size']-v['sell_size']>1])} positions OK")
        return 0
    
    # Write triggered positions for the cron to act on
    with open(os.path.join(BOT_DIR, "stoploss_triggered.json"), "w") as f:
        json.dump(triggered, f, indent=2)
    
    return 1

if __name__ == "__main__":
    sys.exit(check())
