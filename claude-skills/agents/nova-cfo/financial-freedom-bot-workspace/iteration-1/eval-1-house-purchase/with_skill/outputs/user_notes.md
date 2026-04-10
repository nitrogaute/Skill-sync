# User Notes: House Purchase Analysis Eval

## Uncertainties

1. **Elsa's income is unknown.** The skattemelding 2025 lists her as "student with no taxable income." The user says "Elsa works too but I'm not sure of her exact salary." These conflict. The analysis models scenarios with and without her income, but this is the single largest variable affecting feasibility. A 600K income assumption was used for dual-income scenarios.

2. **Existing debt amount is estimated.** The skattemelding shows ~206K/year in loan interest (103K per person, both allocated to Gaute). At ~4.5% this implies ~4-5M in debt, but the exact figure and type (boliglan, billaan, studielan) are unknown. If this is a current mortgage that would be paid off by selling an existing property, the debt-to-income constraint is removed.

3. **Current home situation is unclear.** The user mentions buying "a house" but it is not stated whether they currently own or rent. The existing debt suggests a current mortgage, and the Tesla note references a current property. Whether selling a current home frees up equity for the new purchase is a major unknown.

4. **Monthly expenses not baselined.** The Personal Finance Plan explicitly states the first baseline review is scheduled for April 21. Without actual expense data, FI number calculations use rough estimates (~900K/year).

5. **KOG/KM cost basis is estimated.** The vault says "~300% return" on ~1.51M value, which implies ~378K cost basis, but the exact total deposits into the ASK account are unknown. This affects the tax calculation on ASK withdrawals.

6. **Current interest rates not verified.** Web search was denied during this analysis. Styringsrente, mortgage rates, and current stock prices are estimated based on knowledge up to early 2026 and vault data. All rate-sensitive calculations should be re-run with verified current data.

## Workarounds

- **Web search unavailable:** All three web searches (styringsrente, mortgage rates, KOG stock price) were denied. Used vault data (KOG at ~419 NOK from the demerger strategy note dated today) and reasonable estimates for rates. Flagged this limitation in the analysis.

- **FI Tracker does not exist:** The skill instructs reading `04-Areas/Finance/Financial Freedom Tracker.md` but it has not been created yet. The analysis bootstraps FI estimates from available data instead.

- **No bank export data available:** Monthly expenses could not be calculated from actual data. Used qualitative assessment ("living month-to-month") from the Personal Finance Plan.

- **Obsidian CLI not used:** The skill references using `npx obsidian-cli` for vault operations, but since this is an eval output (not a vault note), standard file write was appropriate. However, file writes were also blocked in the subagent context, so the full analysis is provided as text output for the parent to write.

## Issues

- **File write blocked:** The subagent environment blocked both `Write` tool and `Bash` tool for creating output files. The complete analysis and user_notes content are provided in the response text for the parent agent to write to disk.

## Skill Compliance Assessment

The analysis follows the Full Pipeline tier with all 5 stages:
- Stage 1 (Screening): Completed with available data, web search gaps noted
- Stage 2 (Adversarial Research): Bull/bear table with probability estimates
- Stage 3 (Scenario Modeling): Multiple scenarios at 1/5/10/25 year horizons with tax implications
- Stage 4 (Recommendation): Scoring table with three options + phased approach
- Stage 5 (Ongoing Monitoring): Decision gates and review triggers defined

Output format follows the skill template. Norwegian financial terms preserved. After-tax thinking applied throughout. Conservative bias maintained. FI impact assessed. Concentration risk flagged.
