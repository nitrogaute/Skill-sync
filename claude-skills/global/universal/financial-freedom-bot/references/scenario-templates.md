# Scenario Modeling Templates

Calculation frameworks for Stage 3 of the pipeline. Use these when modeling financial decisions.

## FI Number Calculation

The core metric. FI = Financial Independence = passive income covers current lifestyle.

```
FI Number = Annual Lifestyle Expenses / Safe Withdrawal Rate

Default SWR: 3.5% (conservative for Norway, accounts for formuesskatt drag on invested assets)
```

**Adjustments:**
- Formuesskatt reduces effective returns by ~0.3-0.5% annually on assets above threshold
- Verdsettelsesrabatt (20% on listed shares) partially offsets this
- Norwegian inflation target: 2% (Norges Bank)
- Real return assumption (stocks, after inflation): 5-6% nominal - 2% inflation = 3-4% real

**FI number includes only invested/passive-income assets:**
- ASK portfolio (liquid, accessible)
- Holding company portfolio (accessible via dividend, but taxed on extraction)
- Rental income (if applicable)
- Does NOT include primary home equity (you live in it)
- Pension supplements FI but has age restrictions (AFP from 62, folkepensjon from 67)

## Savings Rate to FI Timeline

| Savings Rate | Years to FI (assuming 5% real return, starting from zero) |
|-------------|----------------------------------------------------------|
| 10% | 51 years |
| 20% | 37 years |
| 30% | 28 years |
| 40% | 22 years |
| 50% | 17 years |
| 60% | 12.5 years |
| 70% | 8.5 years |

Adjust for existing assets: subtract (current invested assets / FI number) from the timeline proportionally.

## House Affordability (Norwegian Rules)

Norwegian banks follow Finanstilsynet's lending regulations (utlansforskriften):

```
Max loan = 5x gross household income
Required equity = 15% of purchase price (can use BSU for first-time buyers)
Stress test = Must afford payments at current rate + 3 percentage points
Max debt-to-income = 5x (includes ALL debt: mortgage, studielan, billån, credit)
```

**Full cost of house purchase:**
- Purchase price
- Dokumentavgift: 2.5% of property value (not for borettslagsleilighet)
- Tinglysingsgebyr: ~600 NOK per document
- Moving costs, renovation buffer
- Increased monthly: mortgage payment, kommunale avgifter, forsikring, vedlikehold (~1-2% of home value/year)

**Dual-income calculation:**
- Combined gross income determines max loan
- Both must meet stress test individually if one income disappears

**FI impact of house purchase:**
- Mortgage principal payments = forced savings (builds equity)
- But: illiquid, not investable, opportunity cost vs. stock market returns
- Norwegian housing historically ~3-5% nominal appreciation (varies by region)
- Model both: rent + invest difference vs. buy + build equity

## Investment Projection

```
Future Value = Present Value * (1 + real_return)^years + Annual_Contribution * [((1 + real_return)^years - 1) / real_return]

Conservative real return assumptions:
- Norwegian/global equity index: 4-5% real
- Bonds/fixed income: 0-1% real
- Property: 1-3% real (after maintenance)
- Savings account: -1 to 0% real (below inflation)
```

Always show projections at multiple return assumptions (pessimistic/base/optimistic).

## Pension Modeling

### AFP (Avtalefestet pensjon)
- Available from age 62 (if employed in AFP company at 62)
- Must have been in AFP-covered employment for 7 of last 9 years before 62
- Calculated based on pensjonsbeholdning (accumulated rights)
- Can be combined with continued work
- Claiming early = lower annual amount (actuarial reduction)
- Optimal claiming: model income at 62 vs 65 vs 67, accounting for total lifetime payout

### OTP (Obligatorisk tjenestepensjon)
- Employer contributes typically 2-7% of salary (above 1G, up to 12G)
- KM rate: check with employer (typically higher for large companies)
- Accumulates as defined contribution, invested in funds
- Available from 62, must be drawn over minimum 10 years

### IPS (Individuell pensjonssparing)
- Max contribution: 25,000 NOK/year (from 2026)
- Tax deduction: 22% = 5,500 NOK/year
- Exempt from formuesskatt while in IPS
- Taxed as pension income on withdrawal (lower marginal rate for most)
- Available from 62, must be drawn over minimum 10 years
- Always max out — it's an interest-free loan from the state

### Folkepensjon
- Full rights after 40 years of residence/work in Norway
- Available from 67 (can take from 62 with reduced amount)
- Grunnpensjon + tilleggspensjon based on earnings history
- 2026 base amount (G): ~124,000 NOK

### Pension and FI
Pension income reduces the required portfolio size for FI:
```
Adjusted FI Number = (Annual Expenses - Expected Annual Pension) / SWR
```
Model this at different retirement ages to find the optimal FI date.

## Tax Impact Quick Reference

For scenario modeling (strategic level, not filing):

| Item | Effective Tax Rate |
|------|-------------------|
| Salary (marginal, high income) | ~47% (trinnskatt trinn 4+) |
| Capital gains (shares) | 37.84% (22% * 1.72 oppjusteringsfaktor) |
| Dividend (personal) | 37.84% (after skjermingsfradrag) |
| Dividend via holding (fritaksmetoden) | 0.66% effective (3% of 22%) |
| Rental income | 22% |
| IPS deduction value | 22% (5,500 NOK on max 25,000) |
| Formuesskatt (above threshold) | 1.0% (municipality) + 0.3% (state, above 20M) |
