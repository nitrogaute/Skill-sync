#!/usr/bin/env python3
"""
CLV (Closing Line Value) Tracker
Snapshots current prices for all positions. Run regularly.
At resolution: compare entry vs pre-resolution price to measure edge.

Usage: python3 track_clv.py           # snapshot current prices
       python3 track_clv.py --report  # show CLV analysis
"""
import json, os, sys, urllib.request
from datetime import datetime, timezone

BOT_DIR = os.path.expanduser("~/clawd/projects/polymarket-bot")
LEDGER = os.path.join(BOT_DIR, "trade_ledger.json")
CLV_FILE = os.path.join(BOT_DIR, "clv_snapshots.json")
GAMMA = "https://gamma-api.polymarket.com"
HEADERS = {"User-Agent": "PolymarketBot/1.0"}


def get_positions():
    """Get open positions from ledger."""
    with open(LEDGER) as f:
        ledger = json.load(f)
    
    positions = {}
    for t in ledger.get("trades", []):
        key = f"{t['market']}|{t.get('outcome', 'Yes')}"
        if key not in positions:
            positions[key] = {"token": t["token_id"], "market": t["market"], 
                            "outcome": t.get("outcome", "Yes"), "buy_size": 0, "buy_cost": 0, "sell_size": 0}
        if t["side"] == "BUY":
            positions[key]["buy_size"] += t["size"]
            positions[key]["buy_cost"] += t["size"] * t["price"]
        else:
            positions[key]["sell_size"] += t["size"]
    
    return {k: v for k, v in positions.items() if v["buy_size"] - v["sell_size"] > 0.5}


def get_current_price(token_id):
    """Get current price from Gamma."""
    try:
        url = f"{GAMMA}/markets?clob_token_ids={token_id}&limit=1"
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


def snapshot():
    """Take a price snapshot of all positions."""
    positions = get_positions()
    
    # Load existing snapshots
    snapshots = []
    if os.path.exists(CLV_FILE):
        with open(CLV_FILE) as f:
            snapshots = json.load(f)
    
    now = datetime.now(timezone.utc).isoformat()
    
    for key, pos in positions.items():
        price = get_current_price(pos["token"])
        if price is None:
            continue
        
        avg_entry = pos["buy_cost"] / pos["buy_size"]
        
        snapshots.append({
            "timestamp": now,
            "market": pos["market"],
            "outcome": pos["outcome"],
            "entry_price": round(avg_entry, 4),
            "current_price": round(price, 4),
            "clv": round(price - avg_entry, 4),  # positive = we got a better price than current
        })
    
    # Keep last 2000 snapshots
    snapshots = snapshots[-2000:]
    
    with open(CLV_FILE, "w") as f:
        json.dump(snapshots, f, indent=2)
    
    print(f"✅ Snapshot: {len(positions)} positions at {now[:19]}")
    for key, pos in positions.items():
        price = get_current_price(pos["token"])
        if price:
            avg_entry = pos["buy_cost"] / pos["buy_size"]
            clv = price - avg_entry
            emoji = "🟢" if clv > 0 else "🔴"
            print(f"  {emoji} {pos['market'][:40]} ({pos['outcome']}) entry={avg_entry:.3f} now={price:.3f} CLV={clv:+.3f}")


def report():
    """Analyze CLV across all snapshots."""
    if not os.path.exists(CLV_FILE):
        print("No CLV data yet. Run snapshots first.")
        return
    
    with open(CLV_FILE) as f:
        snapshots = json.load(f)
    
    # Group by market
    by_market = {}
    for s in snapshots:
        key = f"{s['market']}|{s['outcome']}"
        if key not in by_market:
            by_market[key] = []
        by_market[key].append(s)
    
    print("=== CLV REPORT ===")
    total_clv = 0
    count = 0
    for key, snaps in by_market.items():
        latest = snaps[-1]
        avg_clv = sum(s["clv"] for s in snaps) / len(snaps)
        total_clv += avg_clv
        count += 1
        emoji = "🟢" if latest["clv"] > 0 else "🔴"
        print(f"{emoji} {latest['market'][:40]} ({latest['outcome']})")
        print(f"   Entry: {latest['entry_price']:.3f} | Latest: {latest['current_price']:.3f} | CLV: {latest['clv']:+.3f} | Avg CLV: {avg_clv:+.3f} | Snapshots: {len(snaps)}")
    
    if count > 0:
        print(f"\nOverall avg CLV: {total_clv/count:+.4f}")
        if total_clv > 0:
            print("📈 Positive CLV = our entries are beating current prices. Edge confirmed.")
        else:
            print("📉 Negative CLV = market moved against us since entry. Model may need recalibration.")


if __name__ == "__main__":
    if "--report" in sys.argv:
        report()
    else:
        snapshot()
