# Monthly Review Template

Use this template when producing the monthly financial review. Write to `04-Areas/Finance/Monthly Reviews/YYYY-MM.md` in the Obsidian vault.

## Template

```markdown
---
title: "Financial Review — {Month} {Year}"
type: review
area: "[[Finance]]"
tags:
  - "#nova/output"
  - "#financial"
  - "#monthly-review"
date: {YYYY-MM-DD}
savings_rate: {percentage}
net_worth: {NOK amount}
fi_progress_pct: {percentage}
fi_number: {NOK amount}
---

# Financial Review — {Month} {Year}

## Executive Summary

{2-3 sentence overview: key theme of the month, savings rate trend, notable events}

**Freedom Ladder Position:** Level {N} — {level name}
**FI Progress:** {current invested assets} / {FI number} = {percentage}%
**Projected FI Date:** {date at current trajectory}

## Income

| Source | Amount (NOK) | Notes |
|--------|-------------|-------|
| KM salary (net) | | |
| HydePoint | | |
| GTB Holding | | |
| Other | | |
| **Total** | **{total}** | |

## Expenses by Category

| Category | Amount (NOK) | % of Income | vs Last Month | Budget Target |
|----------|-------------|-------------|---------------|---------------|
| Housing (mortgage, utilities, insurance) | | | | |
| Food & groceries | | | | |
| Transport (car, fuel, parking) | | | | |
| Children (activities, equipment, clothes) | | | | |
| Subscriptions & SaaS | | | | |
| Savings & investments | | | | |
| Discretionary / other | | | | |
| **Total Spending** | **{total}** | | | |

## Savings Rate

```
Income:     {income} NOK
Spending:   {spending} NOK
Saved:      {saved} NOK
Rate:       {rate}%
Target:     50%
Trend:      {up/down/flat} from {last month rate}%
```

## Investment Portfolio

| Asset | Value (NOK) | Allocation % | Change |
|-------|------------|--------------|--------|
| KOG (ASK) | | | |
| KM (ASK) | | | |
| Other investments | | | |
| GTB Holding (book value) | | | |
| IPS | | | |
| **Total Invested** | **{total}** | 100% | |

**Concentration alert:** {flag if any position >30%}

## Freedom Ladder Progress

| Level | Description | Target | Status |
|-------|------------|--------|--------|
| 1 | Buffer — 1 month ahead | {amount} | {check/gap} |
| 2 | Security — 6-12 month emergency fund | {amount} | {check/gap} |
| 3 | Flexibility — 2 year liquid reserve | {amount} | {check/gap} |
| 4 | Independence — passive income covers basics | {amount} | {check/gap} |
| 5 | Abundance — passive income covers lifestyle | {FI number} | {check/gap} |

## Goal Progress

| Goal | Target | Current | Gap | On Track? |
|------|--------|---------|-----|-----------|
| 1-month buffer | Q3 2026 | | | |
| House deposit | {target} | | | |
| FI number | {FI number} | {invested assets} | | |

## Anomalies & Flags

- {List anything unusual: spending spikes, missed transfers, subscription creep, etc.}

## Next Actions

- {Actionable items — will be created as Todoist tasks}

---

**Previous:** [[{previous month link}]]
**Connected:** [[Personal Finance Plan]] | [[Financial Freedom Tracker]]
```

## Usage Notes

- Populate from bank CSV data in Google Drive (`Finance/Bank Exports/dnb-YYYY-MM.csv`)
- Compare against previous month's review from `04-Areas/Finance/Monthly Reviews/`
- After writing the review, update `04-Areas/Finance/Financial Freedom Tracker.md`
- Create Todoist tasks for each item in "Next Actions"
- If bank CSV is not available, work with whatever data the user provides
