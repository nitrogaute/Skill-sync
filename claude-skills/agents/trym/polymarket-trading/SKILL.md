---
name: polymarket-trading
context_fork: true
description: "Polymarket prediction market trading — drama sells only, behavior-tracked, automated exits. Use when the user mentions Polymarket, prediction markets, trading positions, or portfolio status."
---

# Polymarket Trading — Process V2

Fully autonomous. Execute within framework, report after. No permission needed.

## Mission
Recover from -53% drawdown ($256 → target $549 break-even, then $8,235 15x).
Method: Drama sells (NO on hyped unlikely events). Nothing else until proven.

## Daily Process (30 min total)

### 09:00 — Health Check (5 min)
```bash
cd ~/clawd/projects/polymarket-bot && source .venv/bin/activate
python3 scripts/reconcile.py && python3 scripts/check_stoploss.py
```
Action only if: stoploss triggered, settlement occurred, or mismatch found.

### 16:00 — Scan & Trade (15 min)
Criteria: event market, NO $0.80-0.95, base rate ~0%, expiry 7-45d, volume >$50k, spread <$0.04.

**Pre-trade template (MANDATORY before any order):**
```
Market: ___
Side: NO
Edge: Market YES = ___%, My YES = ___%, Edge = ___%
Max loss: $___
Kill condition: Exit if ___
Size: $__ (quarter-Kelly of bankroll, max $40)
Take profit: $___
Stop loss: $___
```

If template can't be filled → no trade. Zero trades is correct most days.

### 21:00 — Close (10 min)
Fills? Update ledger. News changing thesis? Evaluate. Log behavior.

## 5 Rules

1. **One number or no trade.** Edge must be a calculable percentage.
2. **Exits at entry.** TP + SL + kill condition in ledger BEFORE order.
3. **Max 30% correlated.** No single theme >30% of portfolio.
4. **Sell half at +20%.** Profit-taker enforces this automatically.
5. **Max 5 positions, $40 max each.** Capital is $200 active, $75 reserve.

## Few-Shot: Good vs Bad Trades

### ✅ Good Trade (Drama Sell)
```
Market: Will Qatar strike Iran by March 31?
Side: NO at $0.94
Edge: Market YES=6%, My YES=0.1% (base rate: Qatar has never struck Iran), Edge=5.9%
Max loss: $1.80 (30 shares × $0.06)
Kill condition: Exit if credible Qatar military mobilization reported
Size: $28.20 (quarter-Kelly, 30 shares)
Take profit: Hold to expiry (NO→$1.00 = +$1.80)
Stop loss: NO < $0.82
Result: ✅ Resolved NO. +$1.80 (+6.4%)
Why it worked: Near-zero base rate event, market overpriced YES due to regional fear narrative.
```

### ✅ Good Trade (Bookmaker Arb)
```
Market: Will Carolina Hurricanes win 2026 NHL Stanley Cup?
Side: YES at $0.105
Edge: Bookmaker composite=11.8% (VegasInsider median), PM=10.5%, Edge=+1.3% raw, +6.0% after vig
Max loss: $20 (190 shares × $0.105)
Kill condition: Exit if eliminated from playoffs
Size: $20 (quarter-Kelly)
Take profit: Sell at $0.14 (+33%) or hold to playoffs
Stop loss: YES < $0.07
```

### ❌ Bad Trade (Avoid This Pattern)
```
Market: Will BTC hit $85,000 by March 20?
Side: YES at $0.22
Edge: GBM touch prob=28%, PM=22%, "Edge"=6%
WHY IT FAILED: GBM overestimates in bearish regime. Price-based, not event-based.
Lost: -$8.80 (-100%). BTC was at $82k and falling.
Lesson: PRICE-based markets = no real edge. GBM assumes random walk, ignores momentum/regime.
```

## Banned Trades (Permanent)
- ❌ Crypto price direction (0/6, -$53)
- ❌ Oil strike YES (0/7, -$33)
- ❌ Regime change YES (0/4, -$45)
- ❌ NegRisk markets (can't exit)
- ❌ News sentinel auto-trades (net -$45)

## Allowed Trades
- ✅ Drama sells: NO on hyped events with 0% base rate
- ✅ Bookmaker arb: PM price vs composite odds, >5% edge
- ✅ Resolution criteria edge: misread by market

## Behavior Log (Daily)
```
Opportunities seen: 
Traded: yes/no
Didn't trade why: 
Emotion: calm/anxious/excited
```

## Post Mar 31: Paper Trade 2 Weeks
10 paper trades with >50% hit rate before deploying new capital.

## Key Files
- `POSTMORTEM.md` — full loss autopsy
- `PROCESS_V2.md` — detailed process doc  
- `trade_ledger.json` — position log
- `closed_trades.json` — P&L history
- `scripts/reconcile.py` — on-chain verification
- `scripts/check_stoploss.py` — automated exits
- `scripts/profit_taker.py` — trailing stops (cron)

## API
- Collateral: USDC.e (0x2791...), NOT native USDC
- Orders: LIMIT only, 1¢ better than best bid/ask
- Minimum: 5 shares
- neg_risk=False always for our markets
- Gamma for prices, not CLOB orderbook (shows adapter artifacts)
