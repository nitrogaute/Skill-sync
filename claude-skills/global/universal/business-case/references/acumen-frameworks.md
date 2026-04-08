# Business Acumen Frameworks

Toolkit for Mode 2 (Business Acumen Lens). Use the relevant frameworks conversationally -- don't mechanically apply all of them. Pick the 2-3 most relevant to the user's question.

## Table of Contents

1. [Value Proposition Canvas](#value-proposition-canvas)
2. [Unit Economics](#unit-economics)
3. [Porter's Five Forces](#porters-five-forces)
4. [Value Chain Analysis](#value-chain-analysis)
5. [SWOT with So-What](#swot-with-so-what)
6. [TAM/SAM/SOM](#tamsam-som)
7. [Build vs. Buy Decision Matrix](#build-vs-buy-decision-matrix)
8. [First Principles Economics](#first-principles-economics)

---

## Value Proposition Canvas

**When to use:** User is evaluating whether something is worth doing -- does it solve a real problem for real people?

Two sides:
1. **Customer profile**: Jobs to be done, pains, gains
2. **Value map**: Products/services, pain relievers, gain creators

The key question: Is there a fit between what the customer needs and what you're offering? Where are the gaps?

Application prompts:
- Who is the customer and what job are they trying to get done?
- What's the most painful part of their current process?
- Does our solution address the most important pain, or a secondary one?
- What would make the customer switch from their current approach?

---

## Unit Economics

**When to use:** User wants to understand whether something is economically viable at scale.

### Key Metrics
- **CAC** (Customer Acquisition Cost): Total sales+marketing cost / new customers acquired
- **LTV** (Lifetime Value): Average revenue per customer x average customer lifetime
- **LTV:CAC ratio**: Should be >3:1 for sustainable business. <1:1 means you lose money on every customer.
- **Gross margin**: (Revenue - COGS) / Revenue. Tells you how much of each dollar you keep.
- **Contribution margin**: Revenue - variable costs per unit. Is each unit profitable before fixed costs?
- **Break-even point**: Fixed costs / contribution margin per unit. How many units before you're profitable?

### For internal tools/projects (no revenue)
Replace revenue with value delivered:
- **Cost per transaction avoided** (automation projects)
- **Cost per hour saved** x hourly rate (productivity tools)
- **Risk reduction value** = probability x impact (compliance/safety projects)

Application prompts:
- What does it cost to serve one user/customer/unit?
- Does the economics improve or deteriorate at scale?
- What's the marginal cost of the next unit?
- Where is the break-even point?

---

## Porter's Five Forces

**When to use:** User is evaluating a market, competitive landscape, or strategic position.

| Force | Low Threat | High Threat |
|-------|-----------|-------------|
| **Rivalry** | Few competitors, differentiated | Many competitors, commoditized |
| **New entrants** | High barriers (capital, regulation, IP) | Low barriers, easy entry |
| **Substitutes** | No real alternatives | Many ways to solve same problem |
| **Buyer power** | Many buyers, low switching cost | Few buyers, can dictate terms |
| **Supplier power** | Many suppliers, commodity inputs | Few suppliers, critical inputs |

The framework reveals structural profitability of a market. If all five forces are strong, it's a tough market regardless of how good your product is.

Application prompts:
- Who else is solving this problem and how?
- What would it cost a new entrant to compete with you?
- How easy is it for customers to switch away?
- Are you dependent on any single supplier or platform?

---

## Value Chain Analysis

**When to use:** User wants to understand where value is created and where costs accumulate.

Map the activities from input to customer:

**Primary activities:**
1. Inbound logistics (receiving, storing inputs)
2. Operations (transforming inputs to outputs)
3. Outbound logistics (delivering to customer)
4. Marketing and sales (generating demand)
5. Service (post-sale support)

**Support activities:**
- Infrastructure, HR, technology development, procurement

For each activity: What does it cost? What value does it add? Where are the bottlenecks? What could be outsourced without losing competitive advantage?

The key insight: Competitive advantage comes from performing certain activities differently or better than competitors. Identify which activities are truly differentiating vs. table stakes.

---

## SWOT with So-What

**When to use:** Quick situational assessment, but only if followed by actionable implications.

| | Helpful | Harmful |
|----------|---------|---------|
| **Internal** | Strengths | Weaknesses |
| **External** | Opportunities | Threats |

A SWOT without implications is useless. For each quadrant, answer:
- **Strengths**: How do we leverage this? What would make us lose it?
- **Weaknesses**: Can we fix it? Should we work around it? Is it a dealbreaker?
- **Opportunities**: What's required to capture this? What's the window?
- **Threats**: What's the probability? What's our mitigation?

Then cross-reference:
- **S+O**: Strengths that let us capture opportunities (double down)
- **W+T**: Weaknesses that expose us to threats (urgent fix)
- **S+T**: Strengths that protect against threats (defensive advantage)
- **W+O**: Weaknesses that prevent capturing opportunities (investment needed)

---

## TAM/SAM/SOM

**When to use:** User is sizing a market opportunity.

- **TAM** (Total Addressable Market): Everyone who could theoretically use this. Top-down calculation.
- **SAM** (Serviceable Addressable Market): The segment you can actually reach with your current model.
- **SOM** (Serviceable Obtainable Market): What you can realistically capture in 2-3 years.

### Calculation approaches

**Top-down**: Industry reports, total market size, percentage assumptions. Quick but often inflated.

**Bottom-up** (preferred): Number of potential customers x average revenue per customer. More grounded.

**Value-theory**: Total value created for customers x percentage you can capture as revenue. Good for new categories.

Reality check: If SOM > 10% of SAM for a startup, the assumptions are probably too optimistic. For an established company entering an adjacent market, 5-15% SOM in 3 years is aggressive but achievable.

---

## Build vs. Buy Decision Matrix

**When to use:** User is deciding whether to build something internally or acquire/license it.

| Factor | Build | Buy |
|--------|-------|-----|
| **Time to value** | Longer (months-years) | Shorter (weeks-months) |
| **Total 5-year cost** | Development + maintenance | License + customization + integration |
| **Control** | Full | Limited by vendor |
| **Competitive advantage** | If core competency | Rarely |
| **Maintenance burden** | Internal team forever | Vendor handles |
| **Customization** | Unlimited | Constrained |
| **Risk of failure** | Technical risk | Vendor/integration risk |
| **Talent requirements** | Need to hire/retain | Reduced |

Decision heuristic:
- **Build** when: core to competitive advantage, highly customized needs, long time horizon, talent available
- **Buy** when: commodity capability, speed matters, proven solutions exist, not core to strategy
- **Partner** when: complementary expertise needed, shared risk valuable, neither party can do it alone

---

## First Principles Economics

**When to use:** User is stuck in conventional thinking and needs to reason from fundamentals.

Break the problem down to its irreducible components:
1. What does this physically/fundamentally require? (materials, energy, labor, time, capital)
2. What is the theoretical minimum cost to deliver this?
3. Where is the gap between theoretical minimum and current reality?
4. What causes that gap? (inefficiency, middlemen, regulation, legacy systems, information asymmetry)
5. Can technology, process, or business model innovation close that gap?

This is how Elon Musk approached rocket costs, how Netflix disrupted video rental, how Spotify changed music distribution. The current way of doing things is not the only way.

Application prompts:
- What are the fundamental inputs required?
- Why does it currently cost what it costs?
- Where is value being destroyed rather than created?
- What would a solution look like if we started from scratch?
