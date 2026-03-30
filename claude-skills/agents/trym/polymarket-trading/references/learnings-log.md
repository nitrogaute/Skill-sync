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
| 2026-03-20 | US x Iran ceasefire by April 15 | 0.23 | 0.20 | -1.57 | CLV negative ALL 25 snapshots from day 1. Market disagreed with thesis from start. Exit faster when CLV never turns positive. |
| 2026-03-20 | Will Ethereum dip to 1800 in March | 0.14 | 0.01 | -22.59 | Illiquid tail-risk markets gap through stoploss levels. Book had no bids above 0.01. For illiquid positions, exit at -20pct not -25pct. |
| 2026-03-20 | S&P 500 5pct daily loss Q1 | 0.06 | 0.03 | -7.38 | Thin order book forced selling in 3 batches at declining prices. Stoploss fill was 50pct worse than trigger price. |
| 2026-03-20 | Dashboard data integrity | 0 | 0 | 0 | Ledger-based dashboard drifted from on-chain reality. Rebuilt to use ONLY on-chain data. Never trust ledger for current positions. |
| 2026-03-20 | SYSTEM: Failed to take profits at peaks | 0 | 0 | 0 | Were in profit twice and gave it back both times. No profit-taking rules existed. Only had loss rules. Must add trailing stops and take-profit targets. |
| 2026-03-20 | SYSTEM: No time-based profit taking | 0 | 0 | 0 | Held positions through peaks waiting for expiry. Time decay and mean reversion eroded gains. |
| 2026-03-20 | SYSTEM: Eurovision bookmaker arbitrage d | 0 | 0 | 0 | Comparing PM prices with bookmaker composite odds reveals clear edges. Finland overpriced by 8.7pct on PM vs 14 bookmakers. Method: scrape eurovisionworld.com, compare with PM. |
| 2026-03-20 | SYSTEM: NAV calculation wrong - incomple | 0 | 0 | 0 | Ledger had 6 of 17 closed trades. Dashboard showed wrong NAV. Cash was off by 100 dollars. Root cause: trades closed via different scripts and manual exits never logged to ledger. Single source of truth was broken. |
| 2026-03-20 | SYSTEM: Presented wrong NAV 5 times in o | 0 | 0 | 0 | Showed different wrong NAV numbers throughout the day. Root cause: presented unverified numbers with confidence instead of saying I dont know. Fix: never present a number you cant verify from on-chain source. |
| 2026-03-20 | SYSTEM: Failed to act on ground troops n | 0 | 0 | 0 | Ground troops breaking news came in at 18:56. I analyzed it, said it was massive, then did NOTHING. Waited for Gaute to ask. Classic anti-passivity failure. News sentinel should trigger automatic trade evaluation AND execution, not just alerting. |
| 2026-03-20 | SYSTEM: Need auto-trade on news alerts | 0 | 0 | 0 | Python script can give clearer trade recommendations than me in the moment. Script has no passivity bias. Build news_to_trade.py that outputs specific BUY/SELL recommendations with sizing when sentinel fires. |
| 2026-03-20 | SYSTEM: Cannot sell NO on NegRisk market | 0 | 0 | 0 | NegRisk NO orderbook shows 0.01/0.99 adapter pattern. Selling NO at 0.01 = giving away shares. Cannot trim NegRisk NO positions via CLOB. They sit to expiry. |
| 2026-03-20 | Iowa State NCAA - no exit strategy defin | 0.057 | 0 | 0 | Placed NCAA basket bet without kill condition. Tournament markets are binary - team is in or out. Must define at entry: if eliminated hold to zero, budget is the max loss. Basket strategy means individual losses are expected. |

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

## 2026-03-19 — Energy Crisis Day

### Speed of Reaction (CRITICAL)
- Gulf energy infrastructure attacked at ~01:00. We didn't trade until 09:00.
- Could have bought CL $100 HIGH at $0.50-0.60 instead of $0.80.
- Fix: Built News Sentinel (RSS + Twitter/Nitter) + Price Sentinel. Dual 5-min monitoring.

### Asymmetric Basket Strategy
- Deployed 4-bet basket ($50 total) targeting fat-tail events.
- ETH $1,800 dip YES: +43% within hours. Best performer.
- BTC $67k today YES: -100% (expired, expected for daily lottery).
- Lesson: Basket approach works. Need only 1 of 4 to profit. Size each bet to affordable loss.

### Circuit Breaker Override
- Hit -24% drawdown (>20% threshold). Gaute overrode.
- Rationale: Legacy damage from prior bad trades, active positions healthy.
- Learning: Circuit breaker should distinguish between "active positions bleeding" vs "realized losses dragging total down."

### CL $100 HIGH — WTI vs Brent
- Bought at $0.80 thinking WTI $99 → $100 was imminent.
- Dropped to $0.70 despite Brent at $119. WTI and Brent diverge in supply disruption.
- Learning: CL markets resolve on WTI settlement, not Brent. Don't conflate the two.

### De-escalation Risk
- Twitter intel (Javier Blas) showed tacit ceasefire on upstream energy attacks.
- Trump trying to de-escalate. Oil could drop.
- Learning: Trump gas price promise = structural ceiling. Don't go long aggressive oil strikes.

### Vercel Overhead
- Dropped Vercel dashboard deployment. Local screenshot → Telegram is instant.
- Saved ~5 min per dashboard update cycle.

### Dashboard for Decision-Making
- Built hedge-fund-director view: NAV, drawdown, equity curve, position book, exposure breakdown, trade stats, alerts.
- Screenshot workflow: dashboard.py → dashboard_compact.html → browser screenshot → Telegram.

### Twitter as Intel Source
- Nitter RSS → 5 key accounts (@JavierBlas, @BNONews, @ELINTNews, @TheInsiderPaper, @zaborowski_m)
- Twitter intel was 2-6 hours ahead of traditional RSS feeds.
- Nitter is free but fragile. Failover across 4 instances implemented.

### Closed Trades Postmortem
- BTC $67k today YES: Pure lottery (-100%). Daily crypto dip markets are coin-flips. Size appropriately.
- BTC >$66k Mar 24 YES: Exited at $0.83 (loss -$4.61). Thesis deteriorated (BTC fell from $83k to $70k). Good exit timing.
- BTC >$66k Mar 24 NO: Stoploss at -31.4% (-$5). BTC bounced, NO side crushed. Small position.

## 2026-03-21 — Strategy Overhaul Day

### Edge Discovery
- EVENT-based drama-sells: 5-12% edge (base rate ~0%, market prices 5-15%)
- PRICE-based drama-sells: often ZERO edge (GBM prices correctly at 96-97%)
- BTC $85k NO and ETH $1600 NO: overpaid. GBM says 78-82% NO, we paid 96.5%
- Bookmaker arb confirmed: NCAA Michigan +325 (23.5%) vs PM 19% = 4.5% edge (NegRisk blocked)

### Exit Efficiency (from @sjosephburns)
- Our exit efficiency: ~0% on biggest trades
- ETH $1800: peaked +39%, exited -93%
- BTC $70k: peaked +14.3%, now +2.7% (giving back 11.6%)
- Profit-taker recalibrated: +5% threshold (was +10%), tighter trails throughout

### Portfolio Consolidation
- From 20 positions → 10 meaningful (7 core + 3 near-expiry)
- Concentrated in event-based high-edge positions
- Sold: Hamilton F1, Houston NCAA, Florida NCAA, BTC $85k NO, ETH $1600 NO, Oil $140 NO, Netanyahu NO, Trump end mil ops NO, ETH $2400 NO, Iran conflict ends NO
- Added to: Regime fall NO ($54 total), Oil LOW $85 NO ($40), Another country strike NO ($31)

### What Winners Do
1. Market making (need $50k+)
2. Domain expertise → information advantage
3. Cross-platform arbitrage
4. Resolution criteria exploitation
5. Pre-positioned limit orders
6. Event-driven speed trading (remove LLM from loop)

### Key Mistakes Today
- Pivoted strategy 4 times in one day (panic, not strategy)
- Bought PRICE-based drama-sells without GBM verification
- Deferred work multiple times ("Monday", "tonight", "tomorrow")
- Built agent team infrastructure with zero trading value
