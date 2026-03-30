# Reporting Templates

## Post-Trade Summary (immediate — after every trade or exit)

Send via Telegram immediately after execution:

```
🔔 TRADE EXECUTED:
  Action: BUY/SELL [side] [market] — [shares] @ $[price]
  Rationale: [1-2 sentences]
  Risk verdict: APPROVED | Size: $XX (X% of bankroll)
  Kill condition: [what would trigger exit]
  Portfolio: Deployed X% | Cash X% | Correlation X%
```

```
🔔 EXIT EXECUTED:
  Action: SOLD [side] [market] — [shares] @ $[price]
  Reason: [thesis_invalidated / edge_evaporated / time_decay / stoploss]
  P&L: ±$X.XX (±X.X%)
  Learning: [one sentence]
```

## Touchpoint Portfolio Report (at deep eval sessions)

Send at US Close (22:00 Oslo) and any eval where trades were placed:

```
📊 Polymarket Status — [time]
Portfolio: $X (-$Y / -Z%)
Cash: $X | Deployed: $X
Realized P&L: -$X

Positions (on-chain verified ✅):
🟢/🔴 [Market] [YES/NO] — [±X.X%] ([±$Y.YY])
...

Edge status: X trades with +EV | Correlation: X%
Reconciliation: ✅ X/X matched
Actions this session: [trades, exits, adjustments]
Upcoming catalysts: [what the team is tracking]
```

## /trading_status Command

When Gaute asks for status:
```bash
cd ~/clawd/projects/polymarket-bot
python3 scripts/reconcile.py
python3 scripts/trading_status.py
```
Send output via Telegram. No commentary unless suggestions are actionable now.

## Escalation (rare — four cases only)

1. Wallet recovery needed
2. Single trade >$100
3. Proposed change to the framework
4. Risk Guardian veto that PM believes should be overridden
