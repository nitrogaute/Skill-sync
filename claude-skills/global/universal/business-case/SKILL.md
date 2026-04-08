---
name: business-case
description: >
  Build structured business case documents and apply business acumen thinking. Use this skill when the user
  wants to write a business case, justify an investment, build a case for a project or initiative, analyze
  commercial viability, think through business economics, evaluate ROI, or needs help with cost-benefit analysis.
  Trigger phrases include "write a business case", "business case for", "justify this investment", "what's the
  business angle", "business mindset", "is this viable", "business acumen", "commercial viability", "make the
  case for", "cost-benefit", "ROI analysis", "build the case", "put together a case", "NPV", "payback period".
  Also use when the user mentions R&D stage-gate business cases, Five Case Model, or needs to justify a project
  at a steering committee or phase gate. This skill does NOT do quick Go/No-Go scoring (use
  strategic-business-advisor for that) or change narratives (use burning-platform-strategic-narrative for those).
context: fork
---

# Business Case Skill

Two modes: produce a structured business case document, or apply a business acumen lens to think through commercial realities without a formal deliverable.

## Mode Detection

Determine the mode from the user's request:

**Mode 1 -- Full Business Case Document** when the user wants a deliverable: "write a business case", "build a case for the steering committee", "I need a business case document", "justify this investment". The output is a structured markdown document (convertible to .docx via the docx skill on request).

**Mode 2 -- Business Acumen Lens** when the user wants structured thinking, not a document: "what's the business angle", "help me think about the economics", "is this viable", "think through this commercially". The output is conversational analysis using business frameworks.

If unclear, ask: "Do you need a formal business case document, or do you want to think through the business side of this together?"

## Mode 1: Business Case Document

### Step 1: Interview (3-5 questions)

Determine the case type and depth through focused questions. The goal is to load only the relevant reference file rather than applying everything generically.

**Case type detection questions:**
1. What is the investment/project/initiative? (one sentence)
2. Who is the audience? (steering committee, board, team lead, VP, external partner)
3. What's the context?
   - Internal R&D project (new product, feasibility, technology development) -> read `references/rd-internal.md`
   - External R&D (joint venture, co-development, consortium) -> read `references/rd-external.md`
   - External company evaluation (acquisition, partnership, vendor selection) -> read `references/external-company.md`
   - Small internal initiative or idea pitch -> read `references/initiative-pitch.md`
   - Other/general -> read `references/five-case-model.md`

**Depth detection:**
- Lean (1-3 pages): small initiatives, early-stage ideas, quick internal pitches. Use the initiative-pitch template.
- Full (5-15 pages): major investments, board-level decisions, phase-gate approvals. Use the Five Case Model backbone with the relevant domain overlay.

The audience and stakes determine depth. A 50K NOK internal tool doesn't need a Five Case Model. A 10M NOK R&D program does.

4. What's the approximate budget/investment size?
5. What constraints or concerns should the case address? (timeline pressure, regulatory, competitive, political)

Wait for answers before writing.

### Step 2: Write the Business Case

After the interview, read the relevant reference file and produce a structured markdown document.

**For lean cases:** Follow `references/initiative-pitch.md` -- 4 sections, 1-3 pages.

**For full cases:** Follow `references/five-case-model.md` as the backbone (Strategic, Economic, Commercial, Financial, Management cases), with domain-specific overlays from the relevant reference file.

Writing principles:
- Lead with the "so what" -- every section should answer why the reader should care
- Quantify where possible, be honest about uncertainty where you can't
- Include "do nothing" as an explicit option in the alternatives analysis
- State assumptions explicitly so they can be challenged
- Risk assessment should include likelihood AND impact, not just a list of scary things
- Recommendations should be actionable with clear next steps and decision points

### Step 3: Offer Next Steps

After producing the document:
- Offer to convert to .docx (uses the docx skill)
- Offer to refine specific sections
- Offer to run a devil's advocate critique (if the user wants stress-testing, point them to strategic-business-advisor for a structured Go/No-Go evaluation)

## Mode 2: Business Acumen Lens

Apply structured business thinking without producing a formal document. Read `references/acumen-frameworks.md` for the framework toolkit.

Work through relevant dimensions conversationally:
1. **Value creation**: Who benefits and how? What problem is being solved?
2. **Unit economics**: What are the costs vs. revenue/savings per unit? Does it scale?
3. **Market dynamics**: Size, growth, competition, barriers to entry
4. **Strategic fit**: Does this align with organizational goals and capabilities?
5. **Risk/return**: What could go wrong? What's the upside? Is the risk proportional?
6. **Timing**: Why now? What's the cost of delay? First-mover advantage?

Don't mechanically walk through all six. Focus on the dimensions most relevant to what the user is thinking about. If they're asking "should we build or buy", unit economics and strategic fit matter most. If they're asking "is this market worth entering", market dynamics and timing matter most.

Be direct. If the economics don't work, say so. If a key assumption is shaky, call it out. Business acumen means seeing clearly, not optimistically.

## Skill Boundaries

This skill builds the case and does the commercial thinking. Adjacent skills handle different concerns:

- **Strategic-business-advisor**: Quick structured Go/No-Go scoring with a 6-dimension rubric. Use when the user wants a recommendation, not a document. ("Should we do this?" vs. "Build me the case for doing this.")
- **Burning-platform-strategic-narrative**: Crafts change narratives to drive adoption. Use when the user needs to communicate a change, not justify an investment. ("How do I get the organization on board?" vs. "Why should we invest in this?")
- **Km-project-management**: KM-specific project processes, templates, and governance. Use for KM internal docs (mandates, periodic reports, phase-gate checklists). The business-case skill handles the business justification that feeds into those KM processes.
- **Tech-domain**: Technology sector domain knowledge. Complements business-case when the subject is a tech investment -- no boundary conflict, they work together.
