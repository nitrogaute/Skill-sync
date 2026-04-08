# R&D Internal Business Cases

Overlay for internal R&D projects: Stage-Gate integration, TRL, portfolio logic, and probability-weighted analysis. Apply on top of the Five Case Model backbone for R&D-specific business cases.

## Table of Contents

1. [Stage-Gate Framework](#stage-gate-framework)
2. [Mapping Business Case to Stage-Gate](#mapping-business-case-to-stage-gate)
3. [Technology Readiness Levels (TRL)](#technology-readiness-levels)
4. [R&D Financial Analysis](#rd-financial-analysis)
5. [R&D Scoring Models](#rd-scoring-models)
6. [Portfolio Context](#portfolio-context)
7. [Non-Financial Value](#non-financial-value)
8. [Agile-Stage-Gate Hybrid](#agile-stage-gate-hybrid)
9. [Kill Decisions](#kill-decisions)

---

## Stage-Gate Framework

Dr. Robert Cooper's Stage-Gate is the standard framework for R&D project governance. Companies using it achieve 63-78% success rate vs. 24% without it.

| Stage | Name | Purpose | Gate Question |
|-------|------|---------|---------------|
| 0 | Discovery | Ideas, scanning, opportunity recognition | Is this worth investigating? |
| 1 | Scoping | Preliminary market/technical assessment | Does this pass the initial screen? |
| 2 | Build Business Case | Detailed investigation, business justification | Is this worth developing? |
| 3 | Development | Design, build, test prototypes | Is this ready for validation? |
| 4 | Testing & Validation | Customer trials, market testing, production trials | Is this ready for launch? |
| 5 | Launch | Full production, market launch, commercialization | Was this a success? (post-launch review) |

**Each gate is a kill point.** The purpose of gates is not to rubberstamp progress. A healthy R&D portfolio kills 30-50% of concepts before Development (Gate 3) and 10-20% before Launch (Gate 5).

---

## Mapping Business Case to Stage-Gate

The business case deepens through the stages. Early stages need lighter justification; Stage 2 is where the full case is built.

| Stage | Business Case Depth | What's Required |
|-------|-------------------|-----------------|
| Gate 1 (after Scoping) | 1-page screen | Problem statement, rough market size, strategic fit, ballpark cost |
| Gate 2 (after Build BC) | Full business case | Five Case Model with all sections. This is the critical gate. |
| Gate 3 (after Development) | Updated business case | Revised with actual development data. Updated costs, timeline, risks. |
| Gate 4 (after Validation) | Final business case | Refined with validation results. Go/no-go for full launch. |

**Stage 2 = "Build Business Case"** is the most important gate. This is where the organization decides whether to commit significant resources. The business case must be rigorous enough to enable honest kill decisions.

### Adapting the Five Case Model for R&D

| Five Case Section | R&D-Specific Emphasis |
|-------------------|----------------------|
| Strategic Case | Technology strategy alignment, TRL progression, capability building |
| Economic Case | Probability-weighted NPV, scoring model alongside financial metrics |
| Commercial Case | Product-market fit evidence, route to commercialization, IP strategy |
| Financial Case | R&D cost estimation (use reference class), revenue ramp assumptions |
| Management Case | Technical risk, team competency, prototype/validation milestones |

---

## Technology Readiness Levels

TRL maps to uncertainty and determines appropriate analysis depth.

| TRL | Description | Uncertainty | BC Depth |
|-----|------------|-------------|----------|
| 1-2 | Basic principles, concept formulated | Very high | Lean only. Focus on strategic fit + rough sizing. |
| 3-4 | Experimental proof of concept, lab validation | High | Lean-to-medium. Include rough financials, probability ranges. |
| 5-6 | Technology validated in relevant environment | Medium | Full business case with scenarios. |
| 7-8 | System prototype demonstrated, qualified | Low-medium | Full business case with detailed financials. |
| 9 | Actual system proven in operational environment | Low | Update and finalize for launch gate. |

Don't demand IRR precision at TRL 2. Don't accept vague hand-waving at TRL 7.

---

## R&D Financial Analysis

Standard NPV is insufficient for R&D because it ignores the asymmetric risk profile and option value of early-stage projects.

### Probability-Weighted NPV

Instead of a single NPV, calculate expected value across scenarios:

**E[NPV] = P(success) x NPV(success) + P(partial) x NPV(partial) + P(failure) x NPV(failure)**

Typical success probabilities by stage:
| Stage | Cumulative Success Rate |
|-------|----------------------|
| Scoping (Gate 1) | 50-60% pass |
| Business Case (Gate 2) | 30-40% of original ideas survive |
| Development (Gate 3) | 20-30% of original ideas survive |
| Validation (Gate 4) | 15-25% of original ideas survive |
| Launch (Gate 5) | 10-20% of original ideas become successful products |

### Real Options Thinking

Early R&D investment buys options, not commitments. Frame early stages as:
- "For [X cost], we buy the option to learn whether [hypothesis] is true"
- "If the hypothesis is confirmed at Gate 2, the project is worth [Y]"
- "The option value is [Y x probability - X]"

This helps justify exploration-stage projects that NPV analysis would kill prematurely.

### Reference Class Forecasting

R&D cost estimates are notoriously optimistic. Adjust using historical data:
- Average R&D project overrun: 20-50% (varies by industry and TRL)
- Software projects: 30-60% overrun (Standish Group data)
- Hardware/physical products: 20-40% overrun

Always include contingency, scaled to TRL:
| TRL | Recommended Contingency |
|-----|----------------------|
| 1-3 | 50-100% |
| 4-6 | 25-50% |
| 7-9 | 10-25% |

---

## R&D Scoring Models

Use alongside financial metrics, not instead of. Scoring models capture strategic value that NPV misses.

### Example Scoring Rubric

| Criterion | Weight | 1 (Low) | 3 (Medium) | 5 (High) |
|-----------|--------|---------|------------|----------|
| Strategic alignment | 25% | Nice-to-have | Supports strategy | Core to strategy |
| Market attractiveness | 20% | Small/declining | Moderate growth | Large/high growth |
| Technical feasibility | 20% | Unproven, high risk | Demonstrated concept | Proven technology |
| Competitive advantage | 15% | Me-too | Some differentiation | Strong/defensible |
| Resource availability | 10% | Need to hire | Partial team | Team in place |
| Time to revenue | 10% | >3 years | 1-3 years | <1 year |

**Weighted score = sum of (score x weight) for all criteria.**

Scoring models work best when:
- Criteria and weights are agreed before scoring (not adjusted to fit desired outcomes)
- Multiple stakeholders score independently, then discuss divergence
- Scores are compared across the portfolio, not evaluated in isolation

---

## Portfolio Context

An R&D business case should never be evaluated in isolation. Position it within the portfolio:

### Portfolio Balance Questions
- What % of R&D budget goes to incremental vs. breakthrough?
- Are we over-invested in one technology area?
- Does this project compete for the same resources as higher-priority projects?
- What's the portfolio-level risk if this project fails?

### Portfolio Visualization
Plot projects on a 2x2 matrix:
- **X-axis**: Probability of technical success
- **Y-axis**: Expected commercial value

Projects in the high-probability, high-value quadrant justify Full business cases. Projects in the low-probability, high-value quadrant might justify smaller Lean cases to buy options. Projects in the low-probability, low-value quadrant should be killed.

---

## Non-Financial Value

R&D generates value beyond direct revenue. The business case should acknowledge:

- **IP generation**: Patents, trade secrets, know-how
- **Capability building**: Team skills, tooling, infrastructure reusable across projects
- **Strategic optionality**: Keeping doors open for future opportunities
- **Platform effects**: Technology that enables multiple products
- **Talent attraction**: Cutting-edge R&D attracts and retains top engineers
- **Customer relationships**: Co-development deepens customer partnerships
- **Regulatory positioning**: Early work on compliance, standards participation

Don't hide behind non-financial value to avoid hard financial questions. But don't ignore it either. Include a section in the Strategic Case that names the non-financial value explicitly, with a qualitative assessment of significance (high/medium/low).

---

## Agile-Stage-Gate Hybrid

Cooper's research shows Agile-Stage-Gate hybrid gives ~30% better time-to-market than traditional Stage-Gate alone.

### How it works
- **Gates remain**: Go/kill decision points stay in place
- **Stages become sprints**: Instead of long sequential phases, use time-boxed iterations within each stage
- **Build-test-feedback loops**: Each sprint delivers something testable
- **Business case evolves**: The case is updated iteratively, not written once and frozen

### Implications for the business case
- Stage 2 business case is a "living document" -- updated each sprint with new data
- Financial projections tighten as uncertainty reduces through sprints
- The gate review evaluates progress AND updated business case, not just a document written months ago

---

## Kill Decisions

The hardest part of R&D governance. The business case must honestly enable kill decisions.

### Signs a project should be killed
- Technical milestones missed in 2+ consecutive sprints
- Market assumptions invalidated by customer feedback
- Cost estimate increased >50% from Gate 2 approval
- Strategic priority shift makes the project less relevant
- A competitor launched a superior solution
- Key team members left and can't be replaced

### Making it safe to kill
- Frame it as "redirecting resources to higher-value projects", not failure
- Celebrate the learning and IP generated
- Require a brief post-mortem (1 page max)
- Track kill rate as a health metric -- too few kills means gates aren't working

### Business case role in kills
The business case provides the evidence for the kill decision. At each gate, compare:
1. Original assumptions vs. current reality
2. Original cost estimate vs. EAC (Estimate at Completion)
3. Original timeline vs. forecast
4. Original market assumptions vs. current evidence

If the gap is large enough, the business case no longer supports continuation.
