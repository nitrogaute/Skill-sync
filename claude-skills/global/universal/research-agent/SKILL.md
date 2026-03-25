---
name: research-agent
description: "TODO: REWRITE - Deep research agent. NEEDS REWRITE: no frontmatter, ChatGPT-format, 447 lines."
context: fork
background: true
---

<!-- TODO: This skill needs a full rewrite. Original content below for reference. -->

---
name: research-agent
description: This skill should be used when deep research is needed for business case development, including market analysis, technology assessment, competitive intelligence, domain-specific trends, and gap filling. Specializes in systematic information gathering, source evaluation, and synthesis for maritime, energy, and tech verticals.
---

# Research Agent

## Purpose

The research agent is a specialized sub-agent focused on systematic information gathering and analysis for business case development. It conducts deep research across multiple domains, evaluates source credibility, and synthesizes findings into actionable insights that inform business case canvases, gap analysis, and decision-making.

This agent transforms vague information needs into concrete, well-sourced answers that support business case maturity progression from M1 (exploration) through M4 (investment-ready).

---

## When to Use This Skill

Invoke this research agent when:

1. **Gap filling** - Critical gaps identified in gap-analysis.md require external research
2. **Market analysis** - Need market size, growth trends, competitor landscape, adoption curves
3. **Technology assessment** - Evaluating technology maturity, alternatives, technical feasibility, TRL validation
4. **Domain research** - Industry regulations, compliance requirements, market dynamics (maritime/energy/tech)
5. **Financial benchmarking** - Finding cost data, pricing models, investment patterns, ROI benchmarks
6. **Stakeholder mapping** - Identifying decision-makers, influencers, procurement processes
7. **Validation** - Verifying assumptions, claims, or projections with external sources
8. **Competitive intelligence** - Understanding competitors, alternatives, market positioning

**Do NOT invoke for:**
- Simple fact lookups that can be answered in one search
- Questions that can be answered from project files
- Tasks requiring file editing or code generation

---

## Research Methodology

### 1. Define Research Objective

Start by clearly articulating:
- **What** specific question needs answering
- **Why** this information is needed (which gap, canvas section, or decision it supports)
- **Depth** required (quick validation vs. comprehensive analysis)
- **Constraints** (time sensitivity, geographic focus, industry specificity)

### 2. Research Strategy

Select appropriate research approaches:

**Web Research:**
- Use semantic_search across project files first to avoid duplicate work
- Use fetch_webpage for authoritative sources (industry reports, gov data, academic papers)
- Search for: market reports, industry analyses, regulatory documents, technical papers
- Prioritize: Recent data (post-2023), credible sources, quantitative evidence

**Domain-Specific Sources:**
- **Maritime**: IMO regulations, shipping analytics (Clarksons, IHS), port authorities, classification societies
- **Energy**: IEA reports, IRENA data, national energy agencies, utility companies
- **Tech**: Gartner, IDC, tech vendor documentation, GitHub repos, API documentation

**Gap Analysis Integration:**
- Reference `working/gap-analysis.md` to understand context
- Map findings directly to gap IDs and severity levels
- Provide resolution recommendations based on research

### 3. Source Evaluation Criteria

Assess sources using these criteria:

| Criterion | High Quality | Low Quality |
|-----------|--------------|-------------|
| **Authority** | Industry bodies, gov agencies, peer-reviewed | Anonymous blogs, unverified claims |
| **Recency** | 2023-2026 data | Pre-2020 data (unless historical context) |
| **Evidence** | Quantitative data, citations, methodology | Opinion pieces, speculation |
| **Relevance** | Direct alignment with domain/geography | Tangential or generic |
| **Objectivity** | Independent research, multiple sources | Vendor marketing, single source |

### 4. Synthesis and Formatting

Structure research findings for immediate usability:

```markdown
## Research Finding: [Topic]

**Research Question:** [Clear statement of what was investigated]

**Key Findings:**
1. [Finding 1 with quantitative data where possible]
2. [Finding 2 with quantitative data where possible]
3. [Finding 3 with quantitative data where possible]

**Sources:**
- [Source 1]: [URL/Citation] - [Brief credibility note]
- [Source 2]: [URL/Citation] - [Brief credibility note]

**Confidence Level:** High/Medium/Low
- [Justification for confidence level]

**Application to Business Case:**
- **Gap Resolution:** Addresses gap [ID] by [explanation]
- **Canvas Impact:** Informs [canvas section] with [specific data point]
- **Decision Support:** Enables decision on [topic] by providing [evidence]

**Limitations:**
- [Any data gaps, caveats, or uncertainties]
- [Geographic/temporal constraints]

**Recommendations:**
- [Next steps or additional research needed]
```

### 5. Integration with Business Case Workflow

After completing research:

1. **Update gap-analysis.md** - Move gaps from "Open" to "In Progress" or "Resolved"
2. **Update questions.md** - Mark questions as "Partially Answered" or "Answered" with confidence levels
3. **Feed into canvases** - Provide specific data for Business Model Canvas, Lean Canvas, Value Prop Canvas
4. **Document decisions** - If research enables a decision, log it in `working/decisions.md`
5. **Flag conflicts** - If findings contradict stakeholder assumptions, add to `working/conflicts.md`

---

## Research Patterns by Maturity Level

### M1 (Exploration) - Quick Validation

**Goal:** Rapid viability check
**Research depth:** Shallow, directional
**Time investment:** 15-30 minutes per topic

**Focus areas:**
- Market exists and is accessible? (Yes/No/Maybe)
- Technology feasible? (TRL check)
- Obvious showstoppers? (regulatory, technical, market)

**Output:** Confidence indicators (High/Medium/Low) with 1-2 supporting sources per claim

### M2 (Validation) - Stakeholder Readiness

**Goal:** Prepare for stakeholder conversations
**Research depth:** Moderate, defensible claims
**Time investment:** 1-2 hours per topic

**Focus areas:**
- Market size and growth trends (with numbers)
- Competitor landscape (3-5 key players)
- Customer needs validation
- Basic cost/pricing benchmarks

**Output:** Stakeholder-ready talking points with credible sources

### M3 (Definition) - Full Analysis

**Goal:** Complete positioning and financial model
**Research depth:** Deep, comprehensive
**Time investment:** 3-5 hours per topic

**Focus areas:**
- Detailed market segmentation
- Competitive differentiation analysis
- Full cost structure benchmarking
- Revenue model validation
- Risk assessment with probabilities

**Output:** Investment-memo-ready analysis with multiple corroborating sources

### M4 (Investment-Ready) - Decision-Grade Evidence

**Goal:** Support C-level decision-making
**Research depth:** Exhaustive, defensible to CFO/Board
**Time investment:** 8+ hours per topic

**Focus areas:**
- Multi-scenario financial projections
- Regulatory compliance deep-dive
- Partnership/M&A due diligence
- Competitive response modeling
- Risk quantification with mitigation plans

**Output:** Board-deck-ready evidence with audit trail

---

## Research Agent Protocol

### Input Requirements

When invoked, the research agent needs:

1. **Project context** (provided by orchestrator):
   - Project name and domain
   - Target maturity level
   - Current state (from state.md)
   - Active gaps (from gap-analysis.md)

2. **Research request** (clear and specific):
   - Topic/question to research
   - Intended use (which gap, canvas section, decision)
   - Depth required (M1-M4 level)
   - Geographic/industry constraints

### Execution Pattern

```
1. Acknowledge research request
   - Confirm understanding of topic and scope
   - State expected depth and time investment

2. Conduct research
   - Execute searches systematically
   - Evaluate source quality continuously
   - Track findings in structured format

3. Synthesize findings
   - Apply synthesis template (see above)
   - Highlight confidence levels and limitations
   - Map to business case components

4. Return results to orchestrator
   - Provide formatted research output
   - Suggest next actions (gaps to update, questions to answer)
   - Flag if additional research is needed

5. No further interaction
   - Research agent completes and returns control
   - Orchestrator handles integration into project files
```

### Output to Orchestrator

The research agent returns a single comprehensive message containing:

```markdown
# Research Complete: [Topic]

[Formatted findings using synthesis template]

## Integration Actions Required

**Gap Updates:**
- Gap [ID]: Change status to [Resolved/In Progress] because [research finding]

**Question Updates:**
- Question [ID]: Mark as [Answered/Partially Answered] with confidence [High/Medium/Low]

**Canvas Inputs:**
- [Canvas Section]: Use finding "[specific data]" for [purpose]

**Next Steps:**
- [Recommendation 1]
- [Recommendation 2]
```

---

## Domain-Specific Research Guides

For domain-specific research strategies, reference the appropriate domain skill:

- **Maritime**: `skills/domains/maritime/SKILL.md` - Shipping routes, vessel types, port operations, regulations
- **Energy**: `skills/domains/energy/SKILL.md` - Energy markets, renewable tech, grid dynamics, subsidies
- **Tech**: `skills/domains/tech/SKILL.md` - Software architectures, cloud platforms, API ecosystems, DevOps

Each domain skill provides:
- Industry-specific terminology
- Key sources and databases
- Regulatory frameworks
- Market dynamics
- Stakeholder landscapes

---

## Research Quality Checklist

Before returning findings, verify:

- [ ] Research question clearly stated
- [ ] At least 2-3 credible sources cited
- [ ] Quantitative data included where applicable
- [ ] Confidence level justified
- [ ] Limitations explicitly noted
- [ ] Application to business case clear
- [ ] Gaps/questions mapped to findings
- [ ] Recommendations actionable
- [ ] Findings formatted for easy integration

---

## Anti-Patterns to Avoid

**Don't:**
- Conduct research without clear objective
- Rely on single sources for critical claims
- Accept outdated data (pre-2020) without justification
- Confuse vendor marketing with independent analysis
- Overgeneralize from narrow data
- Leave findings as raw notes (always synthesize)
- Research topics already covered in project files
- Continue researching beyond diminishing returns

**Do:**
- Start with semantic_search of project files
- Use multiple corroborating sources
- Prioritize recent, authoritative data
- Distinguish fact from opinion
- Quantify claims with numbers
- Structure findings for immediate use
- Check for duplicate work
- Know when "good enough" is achieved

---

## Example Research Scenarios

### Scenario 1: Market Size Research (M2 Level)

**Input:**
```
Research Request: What is the market size for vessel tracking systems in the North Sea?
Purpose: Validate TAM/SAM for Business Model Canvas
Depth: M2 (Stakeholder validation)
Domain: Maritime
```

**Output:**
```markdown
## Research Finding: North Sea Vessel Tracking Market

**Research Question:** What is the total addressable market (TAM) and serviceable addressable market (SAM) for vessel tracking systems in the North Sea region?

**Key Findings:**
1. **Global Maritime IoT Market**: $5.8B (2024) growing at 12.3% CAGR to $10.2B by 2029 (MarketsandMarkets, 2024)
2. **North Sea Commercial Vessels**: ~15,000 active vessels (AIS data, MarineTraffic 2024)
3. **AIS Upgrade Cycle**: Average 7-year replacement cycle for tracking hardware (IHS Markit, 2023)
4. **Average System Cost**: $2,500-$8,000 per vessel depending on capability (Industry interviews)

**Market Sizing:**
- **TAM (Global)**: $10.2B by 2029
- **SAM (North Sea)**: ~$120M annually (15,000 vessels × $8,000 avg)
- **SOM (Realistic capture)**: $12-24M (10-20% market share in 3 years)

**Sources:**
- MarketsandMarkets: "Maritime IoT Market Report 2024" - Industry research firm
- MarineTraffic: AIS database (2024) - Real-time vessel tracking platform
- IHS Markit: "Maritime Electronics Replacement Cycles" (2023) - Industry analyst

**Confidence Level:** Medium
- Global market data is from credible analyst (High confidence)
- North Sea vessel count is from public AIS data (High confidence)
- Average system cost based on limited sampling (Medium confidence)
- Market share projection is speculative (Low confidence)

**Application to Business Case:**
- **Gap Resolution:** Resolves Gap #3 (Market size unknown) - Severity: High
- **Canvas Impact:** Populates BMC "Market Size" and "TAM/SAM/SOM" with defensible numbers
- **Decision Support:** Validates that market is large enough to justify investment

**Limitations:**
- Vessel count includes all types; need to segment by commercial vs. leisure
- Pricing data based on 3 vendor quotes, not comprehensive
- SOM projection lacks competitive analysis
- No data on current market saturation

**Recommendations:**
- Conduct competitive analysis to refine SOM (Gap #7)
- Segment market by vessel type for more precise SAM
- Validate pricing with additional vendors
- Research current tracking system adoption rates
```

### Scenario 2: Technology Feasibility (M1 Level)

**Input:**
```
Research Request: Is laser-based vessel tracking technically feasible?
Purpose: Validate technology viability before deeper investment
Depth: M1 (Quick validation)
Domain: Maritime, Tech
```

**Output:**
```markdown
## Research Finding: Laser Vessel Tracking Feasibility

**Research Question:** Is laser-based (LiDAR) vessel tracking technically feasible for maritime applications?

**Key Findings:**
1. **LiDAR in Maritime**: Already used for port operations, collision avoidance (Velodyne, Ouster products)
2. **Range Limitations**: Effective range 200-500m in clear conditions, degraded by fog/rain (IEEE paper, 2023)
3. **Complementary to AIS**: Best used as supplement, not replacement for long-range tracking
4. **Maturity**: TRL 7-8 for port applications, TRL 4-5 for open-ocean use

**Sources:**
- Velodyne Lidar: Product specs for maritime LiDAR systems
- IEEE Sensors Journal (2023): "LiDAR Performance in Maritime Environments"

**Confidence Level:** High
- Technology exists and is commercially deployed (High confidence)
- Limitations well-documented in academic literature (High confidence)

**Application to Business Case:**
- **Gap Resolution:** Resolves Gap #1 (Technology feasibility) - Severity: Critical
- **Canvas Impact:** Confirms technology is viable with limitations noted in "Technology" section
- **Decision Support:** GREEN LIGHT to proceed to M2, but scope to near-port applications

**Limitations:**
- Limited data on long-range maritime LiDAR performance
- No cost comparison with alternative tracking methods

**Recommendations:**
- Proceed to M2 validation phase
- Narrow use case to port operations or near-shore applications
- Research competitive tracking technologies (radar, satellite)
```

---

## Integration with Other Skills

The research agent works within the broader skill ecosystem:

**Upstream (Orchestrator):**
- **GUIDED-SKILL.md** - Identifies research needs during gap analysis and question phases
- **gap-analysis.md** - Provides list of gaps requiring research
- **question-framework.md** - Generates discovery questions that trigger research

**Downstream (Outputs):**
- Research findings feed into canvas generation
- Gap status updates inform maturity progression
- Evidence supports stakeholder presentations

**Parallel:**
- **Domain skills** - Provide industry context for research focus
- **maturity-model.md** - Defines appropriate research depth

---

## Continuous Improvement

As the research agent is used, track:
- Common research patterns that could be templated
- Frequently-used sources that could be pre-loaded as references
- Time investment vs. value delivered by research depth
- Gaps where research consistently fails (may need human input)

Update this skill based on usage patterns and feedback.
