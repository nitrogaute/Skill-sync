# Learnings Log

## Trade Postmortems
| Date | Trade | Entry | Exit | P&L | Learning |
|------|-------|-------|------|-----|----------|
| 2026-03-15 | Setup day | — | — | -3.8% | Spread cost on entry is real. Limit orders save money. |
| 2026-03-16 | CL $150 STOPLOSS | 0.150 | 0.080 | -$5.60 | -40% loss. Should have exited at -25%. Automate stoplosses BEFORE trading. |
| 2026-03-16 | CL $130 STOPLOSS | 0.320 | 0.210 | -$2.75 | -30% loss. Same lesson. |
| 2026-03-16 | CL $180 EXIT | 0.058 | 0.040 | -$1.19 | Dead weight. Near-impossible in timeframe. |
| 2026-03-16 | CL $200 EXIT | 0.037 | 0.030 | -$0.35 | Same — apocalyptic scenario. |
| 2026-03-16 | Iran Apr EXIT | 0.160 | 0.140 | -$0.62 | Timeline too aggressive for regime change. |
| 2026-03-16 | CL $110 EXIT | 0.650 | 0.540 | -$6.60 | Kelly ≤ 0. No edge. Was holding due to sunk cost. |
| 2026-03-16 | Iran Jun EXIT | 0.300 | 0.270 | -$0.99 | Kelly ≤ 0. No edge vs market. |
| 2026-03-16 | EVALUATION | — | — | -45.5% | Consensus trades, 85% concentration, averaged down. Every mistake in the book. |
| 2026-03-16 | PIVOT to NO | — | — | — | "Sell drama" strategy. Markets overprice dramatic scenarios. Kelly-sized. |
| 2026-03-16 | Dashboard rewrite | — | — | — | CLOB misses taker fills. Ledger is truth. NO tokens need correct token_id. Don't shadow pnl_color. |

## API/Technical Learnings
- neg_risk=True → "invalid signature" on py-clob-client 0.34.6. ALWAYS use False.
- Minimum order size: 5 shares
- NO token_id ≠ YES token_id. Get from clobTokenIds[1]
- Gamma conditionId search returns 2020 markets. Use clob_token_ids param.
- NegRisk orderbooks show extreme spreads. Use Gamma outcomePrices.
- get_trades() misses taker fills. Local trade_ledger.json is source of truth.
- Don't shadow template variables in loops (pnl_color bug hit twice).
- Full error messages matter. "lower than minimum: 5" was misread as "invalid signature".

## 2026-03-17 — Edge Improvement Sprint

### Exchange Funding
- Polymarket CLOB uses USDC.e, NOT USDC native. Wallet balance ≠ exchange balance.
- Fix: auto-swap via Uniswap V3 (fee tier 100, ~$0.01/swap). Batch $50-100.

### Order Execution  
- Large orders fail with "not enough balance" — it's USDC.e, not actual balance.
- Batch: 5-share test first, then scale.
- Duplicate limit orders happen if script runs twice — check open orders first.

### Market Liquidity
- Gamma API `spread`/`bestBid`/`bestAsk` = real liquidity. Use these.
- CLOB order book shows $0.001/$0.999 for NegRisk markets — DO NOT use for spread filter.

### GBM Touch Probability
- Works for crypto. CoinGecko 90d daily → daily vol → barrier model.
- Caveat: constant vol assumption. Underestimates tail events.
- Applied: BTC $80k (model 67% vs market 41%), BTC $85k (model 34% vs market 12%).

### Stale-Line Detection
- Reuters RSS for headlines. CLV snapshots for price history. Need 6h+ tracking data.
