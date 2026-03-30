# Hard Rules — From Painful Experience + Pro Research

## Entry Discipline
1. **Consensus is not an edge.** If everyone sees the same news, it's priced in.
2. **Base rate first.** What's the historical base rate? Then adjust.
3. **Opposite argument required.** For positions >$20, write 2 sentences arguing why we're WRONG.
4. **Minimum 5% edge.** Our P vs market P must differ by >5% absolute.
5. **Limit orders only.** Bid $0.01-0.03 below mid. Exception: emergency exits.
6. **News cooldown.** After breaking news, wait 30 min. Let MMs reprice.

## Position Management
7. **Never average down.**
8. **Quarter-Kelly sizing.** Calculate Kelly, then ÷4. Max 10% per position.
9. **Diversify.** Max 25% correlated. Oil + oil + oil = 1 bet.
10. **Sunk cost override.** Ignore entry price. "Would I buy this TODAY?"
11. **Max 3 new trades per day.** Each requires written EV calc.

## Execution
12. **Trade during US hours (15:00-21:00 CET).** Best liquidity.
13. **Spread filter.** Don't enter markets with bid-ask >$0.04.
14. **Fee-adjusted edge.** Subtract fees. Skip if <3%.

## Risk
15. **Automated stop-loss MUST run** before any position is opened.
16. **No loss chasing.** After loss >5% of bankroll, reduce next 3 trades by 50%.

## Learning
17. **Track CLV.** Log entry price + pre-resolution price.
18. **Bayesian updates max 10 points.** Single news = 2-5 point move, not 20.
19. **Weekly calibration review.**
20. **Read full API error messages.** Truncating → misdiagnosis.

## EDGE CHECKLIST (all 6 must be YES)
1. ☐ What does the market NOT see that I see?
2. ☐ Am I agreeing with consensus? (If yes → NO TRADE)
3. ☐ What specific catalyst will move this? (Must be concrete)
4. ☐ What is my unique advantage?
5. ☐ What would invalidate this thesis?
6. ☐ If wrong, how much do I lose?
21. **Exit when CLV is negative for ALL snapshots in first 48h — market is saying you are wrong.**
22. **For markets with less than 50k liquidity, set stoploss at -20pct instead of -25pct.**
23. **Dashboard must read positions from on-chain API only. Ledger is append-only historical log.**
24. **Trailing profit lock: when position hits +30pct, set floor at +15pct. Lock gains to redeploy capital into next +EV trade. Compound, dont hoard.**
25. **Time-based take profit: less than 7 days to expiry plus more than +20pct unrealized equals take profit. Take profit and redeploy into fresh +EV opportunities. Capital sitting in a +20pct winner could compound elsewhere.**
26. **For event markets with active bookmaker odds (sports, Eurovision, elections), ALWAYS cross-reference PM with bookmaker composite before trading.**
27. **Every trade exit MUST write to trade_ledger.json before anything else. No exit is complete until ledger is updated. Verify ledger count matches on-chain history after every session.**
28. **Never present a financial number you cannot verify from blockchain or wallet. Say I dont know before saying a wrong number.**
29. **When news sentinel finds CRITICAL or HIGH alert that directly impacts portfolio thesis, evaluate AND place trades in the same session. Never just monitor and wait.**
30. **News sentinel must output actionable trade recommendations with specific market, side, size, and price. Not just alert text.**
31. **~~NEVER sell NegRisk NO tokens on CLOB.~~ RETRACTED 2026-03-23. NegRisk BUY and SELL both work via API with correct token IDs. Original rule was based on truncated token IDs in one failed test. Lesson: never write a "can't do" rule without 3 independent verification tests.**
32. **DRAMA DEALER STRATEGY (Mar 21 pivot):** Our edge is selling overpriced drama — buy NO on events media hypes but won't happen. We are 5/5 on these. NEVER take directional financial bets (BTC price targets, oil strike prices, crypto dips). We are 1/14 on those. The market has better models than us for financial prices.
33. **Let winners run.** Never exit a position just because it's +5-10%. Hold to expiry or major thesis change. We need big winners, not many small ones. Spread costs on churn are the silent killer.
34. **Allowed trade types:** (1) Drama sells — NO on hyped unlikely events, $15-30 each. (2) Lottery tickets — YES on low-prob high-impact events, <$10 each. (3) NOTHING ELSE.
35. **Reduce monitoring frequency.** Price sentinel: 60 min (not 20). News sentinel: 30 min. Stop micromanaging positions with 10-40 day expiry windows.
36. **Trade during US hours only (rule 12).** Weekend spreads are wide. Research weekends, execute Monday-Friday 15:00-21:00 CET.
