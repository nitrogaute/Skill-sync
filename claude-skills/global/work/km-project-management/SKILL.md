---
name: km-project-management
description: "Expert on Kongsberg Maritime (KM) project management processes, R&D management, and Product Development & Management (PD&M). Use when asked to: (1) Guide project setup, execution, or closure following KM processes, (2) Help with project mandates, business cases, periodic reports, or checklists, (3) Advise on PD&M lifecycle phases (Feasibility, Specification & Plan, Realisation, Utilisation, Maintenance, Obsolete), (4) Assist with R&D project data, ERP reporting, milestone management, (5) Draft or review project documents using KM templates, (6) Explain KM project roles, governance, change management, or risk management."
---

# KM Project Management & R&D Processes

## Overview

Kongsberg Maritime (KM) uses a structured project management framework tightly integrated with its Product Development & Management (PD&M) process. This skill provides expert knowledge of KM's processes, templates, roles, governance, and reporting standards.

## Quick Reference: KM Document Library

| Doc ID | Type | Description |
|--------|------|-------------|
| KM-PROC-0074 | Process | Project Execution — the core PM process (PDCA cycle) |
| KM-GUI-0174 | Guideline | PD&M Process — lifecycle phases and integration points |
| KM-GUI-0233 | Guideline | Development Project Data — ERP reporting & milestone standards |
| KM-TMPL-2600 | Template | Project Mandate — Development project initiation |
| KM-TMPL-0035 | Template | Business Case (PowerPoint) — financial justification |
| KM-TMPL-0167 | Template | Periodic Report (Excel) — one-page project status |
| KM-CHKL-0007 | Checklist | Specification & Plan Review — phase gate checklist |
| KM-PROC-0149 | Process | IT Service Management — ITSM processes |

Source documents live in `Guiding Documents Project Management/`.

## Product Development & Management (PD&M) Lifecycle

PD&M governs the full product lifecycle. Products include Integrated Solutions, Solutions, Systems, Products, Services, and Common Technology.

### Development Phases (run as separate projects with mandates)

1. **Feasibility Study** — Concepts, ideas, analyses, prototypes. De-risk technology. Low maturity, high uncertainty.
2. **Specification & Plan** — Detailed requirements, business case, development plan. Medium maturity.
3. **Realisation** — Build the product to ship-ready state. High maturity, low uncertainty.

### Management Phases (post-development)

4. **Utilisation** — Actively sold and supported. Changes are "sustainment" (no new capabilities needed).
5. **Standard Maintenance** — Active spare parts and support.
6. **Limited Maintenance** — Spare parts supported, availability not guaranteed.
7. **Obsolete** — End of life.

### Key PD&M Principles

- A **Product Line** is a group of related products — must be fit for market and provide financial return
- Product maturity increases and business uncertainty decreases across development phases
- Sustainment (changes during Utilisation) uses existing capabilities; new capabilities trigger a new product development
- Three integrated processes work together:
  - **PD&M** — profitability, strategic fit, lifecycle perspective
  - **Project Management** (KM-PROC-0074) — PM discipline, based on Metier/ISO 9001
  - **Technical Processes** (KM-GUI-0143) — engineering activities (timelines governed by PD&M, not technical processes)
- The **mandate** from Product Line Management is the start event for each development phase

## Project Execution Process (KM-PROC-0074)

The core PM process follows a **PDCA cycle**: Plan → Do → Check → Act, with Review and Improve loops.

### 1. Plan Project Activities

- Update Project Management Plan (PMP) with scope, timeframe, resources
- Define competence needs
- Project team estimates workload (Azure DevOps / TFS / Jira)
- Plan and allocate resources with Resource Owners

### 2. Do Project Activities

- Execute tasks per PMP
- Record expenses in ERP (weekly)
- **Periodic reporting** (at agreed intervals):
  - Update PMP and apply data to templates: `KM-TMPL-0167` (Excel) or `KM-TMPL-0168` (PowerPoint)
  - Update financial report; store in 'Status Reports' and 'Finance' folders
  - Contributions from: Project Team (progress), Controller (financials), Owner (advice)
  - Present periodic report to STECO; update action log after meeting

### 3. Check Project Activities

- Verify progress against PMP; describe deviations
- **Risk assessment**: Identify new risks, update current risk levels
- **Lessons observed**: Assess applicability, define avoidance measures
- Record deviations in Action Log

### 4. Act on Deviations

- Discuss impact and possible solutions
- If change request needed:
  1. Create change request (store in 'Change Management' folder)
  2. Call mitigation assessment meeting
  3. Present to STECO / Project Owner / Sponsor for approval
  4. Route to Change Management process

### 5. Review Project Delivery

- Project Quality Responsible calls review meeting
- Project Manager presents delivery report
- Owner/Sponsor/STECO review and approve

### 6. Improve

- Assess issues from review
- Conclude on improvement measures and schedule

## Project Roles

| Role | Responsibility |
|------|---------------|
| **Project Owner** | Accountable for project. Appoints PM. Owns budget, defines strategic goals. |
| **Project Manager** | Day-to-day management. Delivers within scope, time, cost, quality. |
| **Project Sponsor** | Ensures strategic alignment. Approves mandate. Communication bridge to stakeholders. Approves scope changes and deliverables. |
| **Project STECO** | Steering Committee. Decides priorities and manages course of operations. |
| **Project Controller** | Financial support — creates project in ERP, invoicing, estimate follow-up. |
| **Project Quality Responsible** | Ensures quality throughout project. Leads delivery reviews. |
| **Resource Owner** | Manages a pool of human resources. |
| **Project Team** | All assigned resources. Executes tasks, estimates workload, contributes to reports. |

## Project Mandate (KM-TMPL-2600)

The mandate initiates a project and forms the basis for planning. It is completed by Product Line Managers or higher. Required fields:

- Product Line, Project Name, Product Life Cycle Phase
- Project Owner, Project Manager, Project Sponsor
- Product Line Expectations (need definition / background & purpose)
- Scope (in/out)
- Enterprise Risk (initial threats & opportunities)
- Risk escalation threshold (e.g., 3% of cost EMV)
- Cost frame (X MNOK) and Project contingency (Y MNOK)
- Time frame (start/end dates from Product Roadmap)
- STECO composition (roles + names)
- Approval signatures from Sponsor and PM acceptance

## Business Case (KM-TMPL-0035)

PowerPoint format, ~20 slides max. Evolves over PD&M phases (less detail in Feasibility, more in later phases). Mandatory slides:

1. **Executive Summary** — Current situation, proposed solution, business objectives, addressable market, strategic fit, competitive landscape
2. **Executive Summary — Business Case Evaluation** — Investment needs, key financial metrics (NPV at 10% WACC, IRR, payback, ROACE/ROCE), P&L forecast, sensitivity analysis, risk assessment
3. **Setting the Scene** (2 slides) — Market trends, STEEPLE/PESTELE, customer pain points, existing alternatives, ESG/human rights
4. **Proposed Solution** — Innovation, technology maturity, IP strategy, critical success factors
5. **Strategic Fit** — Alignment with KM strategy, SWOT, GE McKinsey Matrix, sustainability
6. **Market Analysis** — TAM/SAM/SOM, OEM + Aftermarket split, segments, early adopters, entry considerations
7. **Competitive Landscape** — Competitor shares, strengths, weaknesses, reaction analysis
8. **Pricing & Placement** — Revenue model, pricing method, supply chain strategy, distribution, product portfolio fit
9. **Value Proposition & Objectives** — SMART objectives aligned with market analysis and KM strategy
10. **Timeline & Resources** — Sales, product dev, supply chain, aftermarket milestones; critical path
11. **Financials** — Investment summary, OPEX/CAPEX/external funding breakdown, P&L (5-10 years), scenarios
12. **Risk Assessment** — Risk factor, probability, EBITDA consequence, mitigating actions
13. **Recommendation** — Recommended way forward; approval sought

## Periodic Report (KM-TMPL-0167)

One-page Excel report with these sections:

- **Header**: Project name, number, phase, PM, Owner, Sponsor, review period
- **Financial summary**: YTD (Budget, Actual, Remaining) + Project Total (Budget, EAC prev., EAC curr.) + CPI/SPI
- **Status indicators** (RAG): Overall, Resources, Quality, Risk, Finance, Milestone, Progress
- **Key Milestones** (up to 8): Planned date, forecast date, status
- **Sections**: Activities, Benefits, Concerns, Do's, Resources, Quality
- **Progress/Burndown chart area**
- **Risk table**: Title, Consequence, Mitigation, Owner, P×C=Risk Level
- **Links to**: Project mandate, finance report, milestone chart, risk matrix

## Specification & Plan Review Checklist (KM-CHKL-0007)

Phase gate checklist to confirm readiness before Realisation. Approval outcomes: Approved (no changes / with agreed changes) or Not approved (major changes / review not completed).

Verification points cover:
- **Project execution** — Schedule, cost, risk management, stakeholder management
- **Detailed business case** — Product-market proposition, competitor assessment, financial viability
- **Development plan** — WBS, OBS, stakeholder analysis, funding/resource confirmation
- **Market strategy** — Sales forecast, product calculation, market launch plan (value proposition, segments, partners, budget)
- **Product specification** — Requirements management, certification, IP protection, lifecycle plan
- **Technical solution design** — Technology assessment, system architecture, BoM, safety assessments, V&V plan, proof of concept
- **Manufacturing & supply chain** — Supply chain design, DfX, capability/capacity planning, sustainability goals
- **Delivery plan** — Delivery model, documentation, export control, security
- **Service & support plan** — Service model, maintenance/disposal needs, logistics
- **Risk management** — Risks identified, documented, addressed

## R&D Project Data & ERP Reporting (KM-GUI-0233)

For detailed ERP (EPM/AX) data entry procedures, see [references/erp-reporting.md](references/erp-reporting.md).

### Key Standards

- **All R&D projects** (Dev, NewOpp, Maint, Util, RDPRO) must have: Budget, Project Start MS, Project Complete MS
- **Project naming**: `[Number] [Product X] [Development Y] [Phase]` — Phase appended: Feasibility / Specification / Realisation. Funding projects append "Funding"
- **Milestone WBS IDs**: Project Start = 10099, Project Complete = 99999
- **Baselines**: Baseline 1 = original mandate budget (never changes); Baseline 2 = revised per approved change requests (used for predictability measurement)
- **Monthly updates**: Update EAC, EstHours, item/expense estimates, validate milestones
- **Change events** requiring BMS change management: down-prioritization, scope changes, budget changes, dependency issues, incorrect data

## IT Service Management (KM-PROC-0149)

For IT-related project work, KM follows ITIL-aligned processes. For detailed process descriptions, see [references/itsm-processes.md](references/itsm-processes.md).

Key processes: Information Security, IT Project Management (Analyse & Plan → Execute → Archive), Access Management, Incident Management, IT Change Management (CAB approval flow), Configuration Management, Service Continuity, Knowledge Management, Release & Deployment Management, Service Level Management, Service Catalogue Management.

## Workflow: Helping with KM Project Tasks

1. **Identify the task type**: Is the user asking about process guidance, document creation, reporting, or review?
2. **For document creation**: Use the appropriate skill (docx, pptx, xlsx) with the matching KM template from `Guiding Documents Project Management/`
3. **For process questions**: Reference the relevant section above and cite the source document
4. **For phase gate reviews**: Walk through the KM-CHKL-0007 verification points relevant to the project's current phase
5. **For ERP/reporting**: Reference KM-GUI-0233 standards and the [erp-reporting.md](references/erp-reporting.md) procedures
