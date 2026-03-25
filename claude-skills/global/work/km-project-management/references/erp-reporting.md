# ERP Reporting Procedures for R&D Projects

Detailed step-by-step procedures for managing project data in ERP (EPM and AX).

## Table of Contents
- [Establishing a New Project](#establishing-a-new-project)
- [Setting Baselines](#setting-baselines)
- [EPM Data Entry](#epm-data-entry)
- [AX Data Entry (without EPM)](#ax-data-entry-without-epm)
- [Monthly Updates](#monthly-updates)
- [Continuous Reporting](#continuous-reporting)
- [Precision Reporting Guidelines](#precision-reporting-guidelines)

## Establishing a New Project

Establish in ERP after mandate approval (during Project Start-up phase).

**Controller responsibilities:**
- Establish the project in ERP
- Set accounts/budget in ERP
- Secure and set a unique Project Number

**Project Manager responsibilities:**
- Select an intuitive Project name

### Project Name Format
`[Project Number] [Product X] [Development Y] [Phase]`

Phase tags (appended to name):
- Feasibility
- Specification
- Realisation
- Funding (for financial-only projects)

Example: `6800000000 Product X Development Y Feasibility`
Example: `6800000001 Product 1 Development Y Realisation Funding`

## Setting Baselines

### Baseline 1 (S-CALC / Mandate budget)
- Original milestone dates before any approved changes
- Set once at project establishment — **never updated**

### Baseline 2 (P-CALC)
- Updated milestones per approved change requests
- Used to measure PM predictability
- Revised during execution with documented, approved changes

Both Baseline 1 and Baseline 2 are set simultaneously at project establishment.

## EPM Data Entry

### Milestone WBS IDs
- Project Start MS = WBS ID **10099**
- Project Complete MS = WBS ID **99999**

### Reporting Flags
In EPM Column "AX Task WBS Type": Add Flag **MS** for milestones that should be reported.

Access this column: right-click in EPM column bar → Insert Column

Optionally add "Customer Milestone" flag for customer-critical milestones.

### Verification
After setup, verify data appears correctly in Power BI: R&D Project Reporting Integrated Solutions.

## AX Data Entry (without EPM)

### Creating Activities/WBSs
1. Go to My Projects in AX, select correct project
2. Click Plan → Work Breakdown Structure
3. Click New Task
4. **Always create these first:**
   - `10099 - Project start`
   - `99999 - Project complete`
5. Enter number in "KM WBS" field
6. Format: `[number] - [task name]`
7. Enter **9999** as category for milestones
8. Add additional activities as needed with correct categories for hours

### Planning Hours and Dates
1. Click Plan → Hour Forecasts
2. Click New (or Ctrl+N)
3. Enter forecast model **EST**
4. Choose correct activity number
5. For milestones: enter correct project date
6. For activities with hours: enter planned hours
7. Optionally edit description

### Copying to PCALC from EST
- Hours can be copied from EST to PCALC within the same project
- Items can be copied from SCALC to PCALC and from EST to PCALC
- Expense is manually registered per project
- **Not possible** in EPM-planned projects

Steps:
1. Verify destination project has same activities as source
2. Go to destination sub-project → Hour or Item Forecasts
3. Click Edit
4. Choose model to copy to (PCALC or EST), tick box
5. Enter project number including sub-project number, tick box
6. Click Select
7. Choose source model and project → OK → OK

## Monthly Updates

**Update EST forecast model only — never change PCALC lines.**

- Update estimated hours in EST field
- For expense/item estimate changes: contact Project Controller
- Update via Plan → Expense Forecast → change amount in EST

## Continuous Reporting

Monthly walkthrough with Controller:
- Update EAC (Estimate at Completion)
- Update EstHours (total estimated hours)
- Update estimated item cost and other costs
- Validate milestones:
  - Still valid?
  - New ones needed?
  - Approved changes documented?
- Ensure milestone updates reflected with deviation in PowerBI Project Reporting

**Documentation requirements for changes:**
- Project Change Request (KM-TMPL-0048) — signed by Sponsor and Project Owner
- Action Log / Decision Log (KM-TMPL-0049)
- Project Change Register (KM-TMPL-0199)

## Precision Reporting Guidelines

| # | Issue | Mitigation |
|---|-------|-----------|
| 1 | Project gets down-prioritized (resources moved away) | Start change management per BMS; update project data in AX/EPM |
| 2 | Scope is changed | Start change management per BMS; update project data in AX/EPM |
| 3 | Change in budget | Start change management per BMS; update project data in AX/EPM |
| 4 | Dependencies to other projects have delivery problems | Collaborate between projects. If milestones/budget affected, start change management per BMS; update AX/EPM |
| 5 | Project data is incorrect in system | Update project data; inform respective customers |
