#!/usr/bin/env python3
"""
Market Scanner — finds asymmetric opportunities on Polymarket.
Usage: python3 scan_markets.py [--min-payout 5] [--max-days 30] [--min-volume 10000]
"""
import json, urllib.request, argparse
from datetime import datetime, timezone, timedelta

GAMMA_API = "https://gamma-api.polymarket.com"
HEADERS = {"User-Agent": "PolymarketBot/1.0"}

def scan(min_payout=5, max_days=30, min_volume=10000):
    now = datetime.now(timezone.utc)
    cutoff = now + timedelta(days=max_days)
    candidates = []
    
    for offset in range(0, 500, 100):
        url = f"{GAMMA_API}/markets?limit=100&active=true&closed=false&order=volume24hr&ascending=false&offset={offset}"
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            markets = json.loads(urllib.request.urlopen(req, timeout=10).read())
            if not markets:
                break
        except:
            break
        
        for m in markets:
            vol24 = float(m.get("volume24hr", 0) or 0)
            if vol24 < min_volume:
                continue
            
            prices = json.loads(m.get("outcomePrices", "[]"))
            if not prices:
                continue
            yes = float(prices[0])
            no = float(prices[1]) if len(prices) > 1 else 1 - yes
            
            # Check both sides for asymmetry
            for side, price in [("YES", yes), ("NO", no)]:
                if price < 0.03 or price > 0.50:
                    continue
                payout = 1 / price
                if payout < min_payout:
                    continue
                
                tokens = json.loads(m.get("clobTokenIds", "[]"))
                token = tokens[0] if side == "YES" and tokens else (tokens[1] if side == "NO" and len(tokens) > 1 else "")
                
                candidates.append({
                    "question": m.get("question", ""),
                    "side": side,
                    "price": price,
                    "payout": payout,
                    "vol24": vol24,
                    "token": token,
                    "end": m.get("endDate", "")[:10],
                })
    
    candidates.sort(key=lambda x: x["vol24"], reverse=True)
    return candidates

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-payout", type=float, default=5)
    parser.add_argument("--max-days", type=int, default=30)
    parser.add_argument("--min-volume", type=int, default=10000)
    args = parser.parse_args()
    
    results = scan(args.min_payout, args.max_days, args.min_volume)
    print(f"Found {len(results)} candidates (>{args.min_payout}x payout, <{args.max_days}d, >${args.min_volume} vol)")
    print()
    for c in results[:20]:
        print(f"  {c['side']:3s} {c['question'][:55]}")
        print(f"      Price: {c['price']:.1%} | Payout: {c['payout']:.1f}x | 24h vol: ${c['vol24']:,.0f}")
        print()
