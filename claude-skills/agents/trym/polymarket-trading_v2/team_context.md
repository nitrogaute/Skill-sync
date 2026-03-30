# Team Context (updated: PENDING — PM must populate on first session)

> **This file is read by every specialist at spawn.** PM updates it after every eval and every trade.
> Keep it compact — this is context, not a report. Target: <100 lines.

## Portfolio Snapshot
- Bankroll: $??? | Cash: $??? (??%) | Deployed: $??? (??%)
- Open positions: ??? | Correlation: ???%
- Drawdown from peak: ???% (circuit breaker at 20%)
- Trades today: 0/3
- USDC.e balance: $???

## Open Positions
<!-- One line per position. Include kill condition so Position Monitor doesn't need to re-derive. -->
<!-- Format: Market | Side | Entry | Current | P&L | Kill condition | Expiry -->

| Market | Side | Entry | Current | P&L | Kill Condition | Expiry |
|--------|------|-------|---------|-----|---------------|--------|
| _PM: populate from reconcile.py + trade_ledger.json_ | | | | | | |

## Recent Outcomes (last 5 closed trades)
<!-- So specialists learn from recent history without reading the full ledger. -->

| Market | Result | P&L | Key Learning |
|--------|--------|-----|-------------|
| _PM: populate from closed_trades.json_ | | | |

## Active Learnings
<!-- Retrospector updates this section. Key insights that should influence current decisions. -->

- _PM: seed from references/learnings-log.md (most recent and most important entries)_

## Known Market Quirks
<!-- Practical knowledge that scripts don't capture — e.g. orderbook behavior, API gotchas. -->

- NegRisk order books show extreme spreads — use Gamma outcomePrices for real values
- _PM: add any market-specific quirks discovered during operation_

## Upcoming Catalysts
<!-- Geopolitical Intel and PM maintain this. Helps Market Analyst and Position Monitor. -->

| Date | Event | Affected Markets | Pre-positioned? |
|------|-------|-----------------|----------------|
| _PM: populate from research + news_ | | | |

## Strategy Performance (rolling)
<!-- Retrospector updates this. Helps Market Analyst prioritize strategies. -->

| Strategy | Trades | Win Rate | Avg P&L | Trend |
|----------|--------|----------|---------|-------|
| Sell Overpriced Drama | ? | ?% | ? | ? |
| Catalyst Trading | ? | ?% | ? | ? |
| Asymmetric Lottery | ? | ?% | ? | ? |
| Quantitative Diversification | ? | ?% | ? | ? |
