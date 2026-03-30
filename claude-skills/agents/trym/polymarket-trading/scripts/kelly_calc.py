#!/usr/bin/env python3
"""
Kelly Calculator — quick CLI for position sizing.
Usage: python3 kelly_calc.py <my_probability> <market_price> <bankroll>
Example: python3 kelly_calc.py 0.88 0.72 400
"""
import sys

def kelly(q, p, bankroll, fraction=0.25):
    """Calculate Kelly-optimal position size."""
    b = (1/p) - 1
    f_star = (q * b - (1-q)) / b
    if f_star <= 0:
        return {"edge": False, "f_star": f_star, "size": 0, "reason": "No edge (Kelly ≤ 0)"}
    
    size = f_star * fraction * bankroll
    ev_per_dollar = q * (1/p) - 1
    
    return {
        "edge": True,
        "my_p": q,
        "market_p": p,
        "delta": q - p,
        "net_odds": b,
        "f_star": f_star,
        "quarter_kelly": size,
        "half_kelly": f_star * 0.5 * bankroll,
        "full_kelly": f_star * bankroll,
        "ev_per_dollar": ev_per_dollar,
        "max_position": min(size, bankroll * 0.25),  # hard cap 25%
    }

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: kelly_calc.py <my_probability> <market_price> <bankroll>")
        print("Example: kelly_calc.py 0.88 0.72 400")
        sys.exit(1)
    
    q, p, bankroll = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    r = kelly(q, p, bankroll)
    
    if not r["edge"]:
        print(f"❌ NO EDGE — Kelly = {r['f_star']:.3f}. Do not trade.")
    else:
        print(f"✅ EDGE FOUND")
        print(f"   My P: {r['my_p']:.1%} vs Market: {r['market_p']:.1%} (delta: {r['delta']:+.1%})")
        print(f"   EV per $1: {r['ev_per_dollar']*100:+.1f}¢")
        print(f"   Full Kelly: {r['f_star']:.1%} of bankroll (${r['full_kelly']:.2f})")
        print(f"   0.25x Kelly: ${r['quarter_kelly']:.2f}")
        print(f"   0.50x Kelly: ${r['half_kelly']:.2f}")
        print(f"   Max position (25% cap): ${r['max_position']:.2f}")
