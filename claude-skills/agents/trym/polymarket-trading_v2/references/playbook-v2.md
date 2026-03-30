# Playbook v2 — Kelly-Optimised Framework

Source: `~/clawd/projects/polymarket-bot/research/polymarket-15x-playbook-v2.docx`

## Objective C: Asymmetric Lottery with Ruin Budget
- **Ruin budget:** ~$200 (everything except $100 UI reserve)
- **Deadline:** April 5, 2026. Extend if positive EV.
- **USDC reserve ($122):** Authorized to deploy via swap.
- **UI position ($100):** Off-limits.
- Cash reserve ≥15% ALWAYS.

## Kelly Sizing Workflow (10 steps)
1. Estimate true probability: q
2. Record market midpoint: p
3. Net odds: b = (1/p) - 1
4. Full Kelly: f* = (q × b - (1-q)) / b
5. If f* ≤ 0 → DO NOT BET
6. Position = f* × 0.25 × bankroll (default 0.25x Kelly)
   → 0.5x ONLY at 5/5 confidence + independent verification + rubric 4+ on all 6
7. Check hard caps: max 25% at entry, max 40% at any point
8. Check order book depth (>20% of liquidity → reduce)
9. Net edge after fees + slippage < 3¢ → SKIP
10. Log all inputs in position card

Deploy at 50% of calculated size (starter). Scale to full ONLY if thesis holds 3-5 days.

## Portfolio Structure
**Anchor (15-25%):** Price 40-65¢, modest edge, slow compounding (NO on overpriced drama)
**Convexity (50-70%):** Price 5-20¢, large edge, growth engine
**Cash reserve (≥15%):** Dry powder

Kelly determines which bucket, not vibes.

## Market Selection Rubric (min 18/30)
| Dimension | 1 (worst) | 5 (best) |
|-----------|-----------|----------|
| Edge clarity | Consensus | Unique insight |
| Catalyst specificity | "Eventually" | Named event + date |
| Liquidity | Spread >$0.10 | Spread <$0.02 |
| Time to resolution | >90 days | <14 days |
| Payout asymmetry | <2x | >10x |
| Correlation to portfolio | Same thesis | Fully uncorrelated |

## Staged Entry
1. Starter: 50% of Kelly size
2. Add ONLY IF thesis strengthens
3. NEVER add if price moved against us
4. Pre-write exit plan BEFORE entry

## Position Card (every position must have)
Market, Token ID, Side, Entry/Current price, Size, Thesis, Edge (my P vs market P),
Catalyst + date, Invalidation trigger, Target exit, Stoploss (-25%), Rubric score,
Barbell bucket, Entry stage.

## Agent Kill Switches
Any agent violating these gets shut down immediately.
(See SKILL.md Hard Rules section)
