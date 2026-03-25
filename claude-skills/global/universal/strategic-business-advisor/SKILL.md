---
name: strategic-business-advisor
description: Structured advisory for business decisions. Use when evaluating opportunities, investments, strategic pivots, partnerships, or any strategic business question requiring systematic analysis and a Go/No-Go recommendation. For full business case documents or business acumen analysis, use the business-case skill instead.
context: fork
---

# Strategic Business Advisor

Transforms business notes into actionable Go/No-Go recommendations through systematic evaluation and self-critique.

## Workflow

### 1. Discovery
Read the business note. Identify:
- **Decision type**: Opportunity | Investment | Strategic pivot | Partnership
- **Stakeholders**: Who decides, who is affected
- **Time horizon**: Immediate (<6mo) | Near-term (6-18mo) | Long-term (18mo+)
- **Resources**: Capital, team capacity, existing commitments

### 2. Success Definition
Ask the user:
1. What outcome = clearly successful?
2. What outcome = clearly failure?
3. What timeframe?

Offer evaluation framework:

| Framework | Best for |
|-----------|----------|
| McKinsey 3 Horizons | Growth/innovation |
| OKR Alignment | Operational decisions |
| IRR/NPV Threshold | Investment decisions |
| Strategic Fit Matrix | Partnership/M&A |
| Risk-Adjusted Return | High-uncertainty bets |

### 3. Clarifying Questions
3-5 questions max, prioritized by:
1. Assumptions that would flip the decision if wrong
2. Missing data that affects scoring
3. Unrepresented stakeholder perspectives

Wait for answers before proceeding.

### 4. Evaluation
Score against 6-dimension rubric (1-5 scale):

| Dimension | Score | Key Factor |
|-----------|-------|------------|
| Financial Viability | /5 | |
| Strategic Fit | /5 | |
| Risk Profile | /5 | |
| Resource Requirements | /5 | |
| Time to Impact | /5 | |
| Competitive Position | /5 | |
| **Weighted Total** | **/5** | |

For each: score + justification + evidence + critical assumption.

### 5. Self-Critique
**Simple**: List 3 biggest weaknesses in recommendation.

**Devil's Advocate** from 4 angles:
1. **Financial Skeptic**: What if the numbers are wrong?
2. **Operational Realist**: What execution risks are underweighted?
3. **Market Pessimist**: What if competition responds differently?
4. **Opportunity Cost Hawk**: What else could these resources achieve?

State explicitly: initial recommendation, post-critique recommendation, what changed and why.

### 6. Synthesis
Produce recommendation memo:

```
RECOMMENDATION: [GO / NO-GO / CONDITIONAL GO]
CONFIDENCE: [X]% (base 60%, adjust +-15% data quality, +-10% clarity, +-15% critique severity, cap 95%)

EXECUTIVE SUMMARY: [2-3 sentences]
EVALUATION SUMMARY: [table from Phase 4]
KEY STRENGTHS: [top 3]
KEY RISKS & MITIGATIONS: [top 3 with mitigations]
SELF-CRITIQUE FINDINGS: [weaknesses + impact on recommendation]
CONDITIONS FOR GO: [if conditional]
NEXT STEPS: [immediate + near-term + validation milestone]
```

Verify before saving: completeness, internal consistency, logical coherence, actionability, critique integration.

## References

- [EVALUATION-RUBRIC.md](references/EVALUATION-RUBRIC.md) - Detailed scoring criteria
- [SUCCESS-FRAMEWORKS.md](references/SUCCESS-FRAMEWORKS.md) - Framework details and examples
- [SELF-CRITIQUE-PROTOCOL.md](references/SELF-CRITIQUE-PROTOCOL.md) - Devil's advocate methodology
