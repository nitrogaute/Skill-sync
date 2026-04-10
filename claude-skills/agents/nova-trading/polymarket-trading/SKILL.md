---
name: polymarket-trading
description: "Polymarket prediction market trading -- 5-step eval pipeline with bull/bear critique, Kelly-sized drama sells, autonomous execution. Use when the user mentions Polymarket, prediction markets, trading positions, market scanning, Kelly sizing, portfolio status, or any polymarket-bot work. Also trigger for casual mentions like 'how are my positions', 'any good markets', 'market scan', 'run the pipeline', or trade execution. NOT for: general crypto/stock trading, sports betting, or financial advice to third parties."
---

# Polymarket Trading -- 5-Step Pipeline

Fully autonomous. Execute within framework, report after. No permission needed.

## Mission

Recover from drawdown toward $549 break-even and beyond. Method: drama sells (NO on hyped unlikely events), macro thesis plays, bookmaker arbs. Every candidate goes through bull/bear adversarial critique before execution.

## The 5-Step Pipeline

Run on every session start and every scheduled scan window (09:00, 16:00, 21:00 CET).

### Step 1: Portfolio Health

```bash
cd ~/NovaTrading/polymarket-bot
python3 dashboard.py
python3 stoploss_monitor.py
```

- Refresh on-chain data, check NAV
- Any stoploss triggered? Execute exit immediately.
- Any market resolved at $1.00 or $0.00? Record settlement, update closed_trades.json.
- Any position hit +20% profit-take rule? Sell half (Rule 4).
- Read portfolio.json for current state.

**Output:** NAV, cash available, position count, any alerts.

### Step 2: News Scan

- Web search for breaking news on each open position's theme
- Focus on: thesis-changing events, approaching catalysts, surprises
- Cross-reference against kill conditions in trade_ledger.json
- If a kill condition is triggered, proceed directly to exit

**Output:** Per-position news impact (bullish/bearish/neutral), any kill conditions triggered.

### Step 3: Opportunity Scan

Search Polymarket for candidates matching these criteria:

**Drama sells (primary strategy):**
- Event market (not price/financial)
- NO price: $0.80-0.95
- Base rate: verifiably ~0% (must cite historical precedent)
- Expiry: 7-45 days
- Liquidity: >$50k volume
- Spread: <$0.04

**Also scan for:**
- Macro thesis plays (Fed, recession, inflation)
- Bookmaker arbs (PM price vs composite odds, >5% edge after vig)
- Resolution criteria edge (market misreading rules)
- Any market where crowd is pricing emotion over base rates

**Output:** Candidate list with market name, price, volume, expiry, estimated edge.

### Step 4: Bull/Bear Critique

**MANDATORY for every candidate from Step 3.** Also run on any existing position where news from Step 2 changed the thesis. This step exists because overconfidence and confirmation bias caused most of our historical losses. The bear case is the antidote.

For each candidate, run adversarial analysis (use `scripts/adversarial_debate.py` for significant trades $15+, or do it inline for smaller ones):

**BULL case** (argue FOR the trade):
1. Core thesis -- why this side wins (specific evidence, not vibes)
2. Catalysts -- what events drive resolution in our favor
3. Why the market is wrong -- what edge we have that others don't
4. Base rate -- historical frequency of similar outcomes
5. Confidence: LOW / MEDIUM / HIGH with honest reasoning

**BEAR case** (argue AGAINST -- be ruthless):
1. Why the thesis is wrong -- specific counter-evidence
2. Hidden risks the bull case ignores
3. Market efficiency -- why the current price might already be correct
4. Adverse scenarios -- concrete paths to losing this trade
5. Kill conditions -- what signals would prove the trade is dead

**SYNTHESIS** (neutral judge):
1. Strongest bull point
2. Strongest bear point
3. What bear revealed that bull missed
4. Adjusted probability estimate
5. Edge vs market price: +X% or -X%
6. **VERDICT: TRADE / SKIP / REDUCE SIZE**
7. If TRADE: recommended size (quarter-Kelly, max $30)
8. Kill condition to adopt from bear case

Only TRADE verdicts proceed to Step 5. If the bear case destroys the bull case, the verdict is SKIP -- no exceptions.

### Step 5: Execute or Pass

For each TRADE verdict, fill the pre-trade template before placing any order:

```
Market: ___
Side: ___
Edge: Market YES = ___%, My YES = ___%, Edge = ___%
Max loss: $___
Kill condition: Exit if ___
Size: $__ (quarter-Kelly of bankroll, max $30)
Take profit: $___
Stop loss: $___
```

If the template can't be filled with real numbers, the trade doesn't happen.

Then:
1. Check correlation: no single theme >30% of portfolio
2. Check position count: max 5 active + $50 max single position
3. Check USDC.e balance via `python3 trade.py balance`
4. Place LIMIT order (1c better than best bid/ask) via `python3 trade.py`
5. Update trade_ledger.json with entry, exits, kill condition
6. Log in behavior-log.md
7. Send post-trade summary to Gaute via `scripts/notify.sh`
8. Verify on-chain that position matches

If no candidates survived the critique: **zero trades is the correct answer most days.** Log it in the behavior log and move on.

---

## 5 Hard Rules

These exist because breaking them caused real losses. Each rule maps to a specific failure mode from our postmortem.

1. **One number or no trade.** Edge must be a calculable percentage. If you can't state it as a number, you don't have edge -- you have a feeling.
2. **Exits at entry.** Take profit + stop loss + kill condition written in the ledger BEFORE the order is placed. Prevents zombie positions.
3. **Max 30% correlated.** No single theme >30% of portfolio. Our Iran cluster at 60% nearly wiped us.
4. **Sell half at +20%.** Profit capture is non-negotiable. The profit_taker.py cron enforces this.
5. **Max 5 active positions, $50 max each.** Capital constraints for our bankroll size.

## Exit Priority

Most losses came from holding positions after the entry thesis died. Exit in this order:

1. **Thesis invalidated** -- entry rationale gone. Exit regardless of P&L.
2. **Edge evaporated** -- CLV negative for 3+ consecutive snapshots.
3. **Time decay** -- <5 days to expiry, out of the money, no imminent catalyst.
4. **-25% hard floor** -- per-position absolute backstop. Non-negotiable.

## Edge Checklist (all 6 must be YES before any trade)

1. What does the market NOT see that I see?
2. Am I agreeing with consensus? (If yes -> NO TRADE)
3. What specific catalyst will move this?
4. What is my unique advantage?
5. What would invalidate this thesis?
6. If wrong, how much do I lose?

## Few-Shot: Good vs Bad Trades

### Good Trade (Drama Sell)
```
Market: Will Qatar strike Iran by March 31?
Side: NO at $0.94
Edge: Market YES=6%, My YES=0.1% (base rate: Qatar has never struck Iran), Edge=5.9%
Max loss: $1.80 (30 shares x $0.06)
Kill condition: Exit if credible Qatar military mobilization reported
Size: $28.20 (quarter-Kelly, 30 shares)
Take profit: Hold to expiry (NO->$1.00 = +$1.80)
Stop loss: NO < $0.82
Result: Resolved NO. +$1.80 (+6.4%)
Why it worked: Near-zero base rate event, market overpriced YES due to regional fear narrative.
```

### Good Trade (Bookmaker Arb)
```
Market: Will Carolina Hurricanes win 2026 NHL Stanley Cup?
Side: YES at $0.105
Edge: Bookmaker composite=11.8% (VegasInsider median), PM=10.5%, Edge=+1.3% raw, +6.0% after vig
Max loss: $20 (190 shares x $0.105)
Kill condition: Exit if eliminated from playoffs
Size: $20 (quarter-Kelly)
Take profit: Sell at $0.14 (+33%) or hold to playoffs
Stop loss: YES < $0.07
```

### Bad Trade (AVOID THIS PATTERN)
```
Market: Will BTC hit $85,000 by March 20?
Side: YES at $0.22
Edge: GBM touch prob=28%, PM=22%, "Edge"=6%
WHY IT FAILED: GBM overestimates in bearish regime. Price-based, not event-based.
Lost: -$8.80 (-100%). BTC was at $82k and falling.
Lesson: PRICE-based markets have no real edge. GBM assumes random walk, ignores momentum/regime.
```

## Banned Trades (Permanent)

These all have proven negative track records:
- Crypto price direction bets (0/6 win rate, -$53)
- Oil strike YES bets (0/7, -$33)
- Regime change YES bets (0/4, -$45)
- NegRisk markets (can't exit positions)
- News sentinel auto-trades (net -$45)

## Allowed Trades
- Drama sells: NO on hyped events with ~0% base rate
- Bookmaker arb: PM price vs composite odds, >5% edge after vig
- Resolution criteria edge: market misreading resolution rules
- Macro thesis: strong consensus-building directional plays (e.g. Fed policy)

## Self-Challenge (every eval)

Before concluding "nothing to do," ask yourself these questions. They exist to prevent the system from going passive:

1. Did scan find candidates? If yes, run them through bull/bear critique.
2. Any position with deteriorating thesis? Exit now, don't wait.
3. Unfilled limit order sitting 12h+? Adjust or cancel.
4. Portfolio >60% correlated? Find an uncorrelated trade.
5. Any position past -25%? Exit immediately.
6. Cash sitting idle >30% of NAV? Deploy or justify why not.
7. Am I doing actual work or just generating status messages?

## Behavior Log (Daily)

```
DATE: YYYY-MM-DD
Opportunities seen: [list]
Traded: yes/no
Didn't trade why: [reason -- "no edge" is valid, "wasn't paying attention" is not]
Emotion: calm/anxious/excited
```

This log matters more than P&L tracking. P&L is outcome. Behavior is process.

## Reporting

After pipeline completes, brief Gaute via `scripts/notify.sh`:
- NAV and daily change
- Position alerts (stoplosses, profit-takes, settlements)
- New trades executed (with edge calculation shown)
- Key news affecting positions
- Keep it under 15 lines

### Post-trade format
```
TRADE EXECUTED:
  Action: BUY/SELL [side] [market] -- [shares] @ $[price]
  Rationale: [1-2 sentences]
  Edge: [X%] | Size: $XX | Kill: [condition]
```

### Exit format
```
EXIT EXECUTED:
  Action: SOLD [side] [market] -- [shares] @ $[price]
  Reason: [thesis_invalidated / edge_evaporated / time_decay / stoploss]
  P&L: +/-$X.XX (+/-X.X%)
  Learning: [one sentence]
```

## Kelly Sizing

```
q = true probability | p = market price | b = (1/p) - 1
f* = (q x b - (1-q)) / b
If f* <= 0 -> NO TRADE (negative EV)
Position = f* x 0.25 x bankroll (quarter-Kelly)
Deploy at 50% (starter). Scale only if thesis holds 3-5 days.
```

## Key Files

All paths relative to ~/NovaTrading/polymarket-bot/:

| File | Purpose |
|------|---------|
| PIPELINE.md | This pipeline (canonical reference) |
| PROCESS_V2.md | Detailed process rules and daily windows |
| POSTMORTEM.md | Full loss autopsy -- read before repeating old mistakes |
| scripts/adversarial_debate.py | Bull/bear critique tool for $15+ trades |
| trade.py | CLI trade executor (buy/sell/positions/balance) |
| dashboard.py | Portfolio refresh from on-chain data |
| stoploss_monitor.py | Automated stoploss checks |
| trade_ledger.json | Position log (not ground truth -- on-chain is) |
| closed_trades.json | Closed position P&L history |
| portfolio.json | Current state (refreshed by dashboard.py) |
| behavior-log.md | Daily behavior tracking |

## API Notes

- Collateral: USDC.e (0x2791...), NOT native USDC
- Orders: LIMIT only, 1c better than best bid/ask
- Minimum: 5 shares
- neg_risk=False for our markets
- Use Gamma API for prices (CLOB orderbook shows adapter artifacts)
- Wallet: macOS Keychain polymarket-private-key

## Failure Modes (from experience)

| What went wrong | What prevents it now |
|----------------|---------------------|
| No exit strategy defined | Kill condition required at entry |
| Phantom positions in ledger | On-chain reconciliation before every report |
| Hidden losses not surfaced | dashboard.py reconciles against on-chain |
| Stoploss missed | stoploss_monitor.py on cron + manual checks |
| Waited for permission instead of acting | Mandate: execute, report after |
| Overconfidence on entries | Bull/bear critique mandatory (Step 4) |
| Crypto/oil YES bets | Permanently banned strategies |
| PM went passive between sessions | 3 daily scan windows + self-challenge questions |
