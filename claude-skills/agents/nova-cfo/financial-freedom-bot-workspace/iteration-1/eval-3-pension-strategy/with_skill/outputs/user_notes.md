# User Notes -- Pension Strategy Analysis

## Uncertainties

1. **Web search unavailable.** The skill specifies running web searches for current Norges Bank styringsrente, stock prices, and policy changes (Stage 1 Screening). WebSearch tool was denied permission. All rates used are from the skill's built-in 2026 knowledge base rather than live data. This means styringsrente, exact G-amount for 2026, and AFP reform status were not independently verified.

2. **FI Tracker note does not exist.** The vault routing table points to `04-Areas/Finance/Financial Freedom Tracker.md` as the baseline for all analyses. This file does not exist yet in the vault. The skill instructs creating it on first invocation, but file-write tools were restricted. FI progress numbers were estimated from the KOG Demerger Strategy note (~1.5M in ASK) and the tax return (~320k net wealth).

3. **Expense baseline not yet established.** The Personal Finance Plan note shows all spending category targets as "?" with the first review scheduled for April 21. The 600k annual expense assumption used throughout the analysis is a rough estimate. The real FI number and pension adequacy assessment depend on establishing this baseline.

4. **KM OTP contribution rate unknown.** The skill knowledge base says KM likely offers 5-7% but the exact rate was not found in any vault note. The analysis models both ends of this range. HR verification is flagged as a next action.

5. **AFP reform risk.** AFP rules may change post-2028. The analysis uses current rules. For someone born ~1991 reaching 62 in ~2053, there is meaningful risk that the AFP system will have been reformed by then.

6. **Obsidian CLI not functional.** The skill specifies using `npx obsidian-cli` for vault read/write. This tool failed in the execution environment. Direct file reads via the Read tool against the vault path worked as a fallback.

7. **Todoist task creation not attempted.** The skill pipeline Stage 5 specifies creating Todoist tasks for follow-up actions. This was not executed as the analysis tier (Stages 1-4 only) does not require Stage 5, and the focus was on producing the analytical output.

## Workarounds

- Read vault notes directly from filesystem instead of using obsidian-cli
- Used skill knowledge base tax rates and pension rules instead of live web search data
- Estimated expense baseline at 600k kr/year based on context clues (1.5M income, "low savings rate" noted in Personal Finance Plan, house purchase target of 10-12M suggesting moderate-to-high living standard)

## Skill Adherence

- Followed the Analysis query tier (Stages 1-4) as pension strategy is a tradeoff-based decision
- Applied after-tax thinking throughout -- all pension projections are post-tax
- Included FI impact assessment per skill requirements
- Covered all four pension pillars (folkepensjon, AFP, OTP, IPS)
- Modeled at multiple ages (62, 65, 67, 72) and time horizons (1, 5, 10, 25 years)
- Included adversarial research (bull/bear table) and scoring table with three options
- Flagged concentration risk (85% KOG position) indirectly through vault data
- Conservative bias applied (3.5% SWR, 5% real return, ranges rather than point estimates)
- Flagged professional advice needed for execution
