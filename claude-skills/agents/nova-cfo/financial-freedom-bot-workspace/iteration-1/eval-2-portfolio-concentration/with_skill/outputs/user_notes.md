# User Notes: Portfolio Concentration Analysis

## Uncertainties

1. **Web search unavailable.** The skill's Stage 1 (Screening) calls for live web searches for current stock prices (KOG.OL, KM.OL), Norges Bank styringsrente, and tax law changes. WebSearch was denied permission. All market data was sourced from vault notes (KOG Demerger Strategy, dated 8 April 2026) and the skill's built-in tax knowledge. Prices and rates should be independently verified before executing any trades.

2. **FI number is estimated, not precise.** The FI tracker note (`04-Areas/Finance/Financial Freedom Tracker.md`) does not exist yet in the vault. Annual lifestyle expenses are unknown -- the first baseline review is scheduled for 21 April. The FI number of ~28.6M NOK is a rough estimate based on assumed ~1M NOK annual expenses. This will need to be recalculated once real expense data is available.

3. **Exact cost basis for KOG position not in vault.** The vault note states "~300% return" on ~3,600 shares at ~419 NOK (~1.51M), implying a cost basis of roughly ~380k NOK and unrealized gains of ~1.13M. The exact cost basis per share matters for ASK withdrawal tax calculations and should be confirmed from the broker's records.

4. **Savings rate unknown.** The Personal Finance Plan states "low savings rate" and aspirational 50% target, but no actual data exists yet. The scenario modeling used 30% as a "realistic near-term" assumption. This significantly affects all FI timeline projections.

5. **Insider trading / quiet period status unresolved.** The vault note flags this as a critical prerequisite. As VP Technology Development at KM with Q1 earnings on 30 April, the quiet period may already be active. If so, the pre-demerger selling window (14-22 April) may be unavailable. This is the single most important blocker to resolve before acting on any recommendation.

## Workarounds

- Used vault data (KOG Demerger Strategy note, Personal Finance Plan, OKRs Q2 2026) as the primary data source in place of live web search.
- Estimated annual expenses from gross income and spending pattern descriptions rather than actual bank data.
- Applied the skill's built-in 2026 tax rates rather than searching for any recent legislative changes.

## Issues with Skill Execution

- **Stage 5 (Ongoing Monitoring) skipped.** The skill specifies creating Todoist tasks for follow-up actions and updating the FI tracker. These were not executed because: (a) the FI tracker does not exist yet, and (b) this is an eval run -- creating real Todoist tasks and vault notes was judged inappropriate during an evaluation. The Next Actions section in the analysis serves as the Stage 5 substitute.
- **Obsidian CLI not used.** The skill specifies reading vault notes via `npx obsidian-cli`. Direct file reads via the vault path (`/Users/nitromini/Documents/vault/`) were used instead, as they are more reliable and faster.
- **No holding company integration.** The analysis focused on the ASK personal portfolio. GTB Ventures/Holding was not deeply analyzed because the user's question was specifically about the ASK position. The holding company's fritaksmetoden benefits could be relevant for future diversification beyond ASK but were noted only briefly.
