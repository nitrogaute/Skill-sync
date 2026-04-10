---
name: eurobonus-optimizer
description: >-
  SAS EuroBonus points and tier optimizer for Gaute. Use this skill whenever the user
  mentions eurobonus, levelpoints, nivåpoeng, bonuspoeng, SAS points, gold/diamond status,
  companion ticket, "which card should I use", "hvilket kort", flight booking optimization,
  or any question about maximizing credit card rewards. Also triggers on "SAS booking",
  "bestille fly", "poengoptimering", or general questions about credit card strategy
  for travel rewards. Use this even for simple "should I use Amex or Mastercard?" questions.
version: 1.0.0
user-invocable: true
---

# EuroBonus Optimizer

Gaute holds three SAS EuroBonus credit cards and flies 5-10 SAS/SkyTeam flights per year. This skill helps him maintain Gold tier (minimum), maximize bonus points and level points, and get the most value from his card portfolio.

## Gaute's Current Setup

- **EuroBonus number:** EBG623307212
- **Current tier:** Gold (SkyTeam Elite Plus)
- **Cards held:** DNB Saga MC Upgrade, SAS EB MC Premium, SAS Amex Elite
- **Flight frequency:** 5-10 SAS/SkyTeam flights/year
- **Qualification period:** 1 May 2025 - 30 April 2026 (member since May 2014)
- **Current status expiry:** July 2026
- **Total annual card fees:** 11,263 kr (DNB 2,028 + MC Premium 2,335 + Amex 6,900)
- **Gold benefits:** 750+ SkyTeam lounges, priority check-in, 2x extra bags, 50% bonus points on SAS/Wideroe flights

Read `references/card-data.md` for full card specifications and earning math.
Read `references/optimization-rules.md` for the decision engine, level points modeling, and strategies.

## Quick Card Selection

When Gaute asks "which card?" or is about to make a purchase, use this table:

| Purchase Type | Best Card | Bonus pts/100 | Level pts/100 | Notes |
|---|---|---|---|---|
| **SAS.no tickets** | SAS EB MC Premium | 25 | ~6.25 | Highest earning rate across all cards |
| **Domestic (Amex OK)** | SAS Amex Elite | 20 | 6 | 33% more than MCs domestic rate |
| **Domestic (no Amex)** | DNB Saga MC Upgrade | 15 | threshold | Fallback; contributes to 100k/200k/500k thresholds |
| **Foreign currency** | DNB Saga MC Upgrade | 20 | threshold | Same pts as Amex, lower FX fee |
| **Foreign (near Amex 150k)** | SAS Amex Elite | 20 | 6 | Worth the 2.5% FX fee if close to companion ticket |

**Default rule:** Amex Elite everywhere it's accepted (20 pts vs 15 pts domestically). SAS EB MC Premium only for SAS.no. DNB Saga as Mastercard fallback and for foreign currency.

## Level Points -- The Gold Equation

Gold requires **45,000 level points** per 12-month qualification period (or 45 flights, but Gaute flies 5-10).

Each card earns level points differently:

| Card | Level Point Mechanism | Annual Potential |
|---|---|---|
| DNB Saga | 10k at 100k spend, +10k at 200k, +10k at 500k | Max 30,000 |
| SAS EB MC Premium | 25% of monthly bonus pts, min 500/mo when used | Uncapped |
| SAS Amex Elite | 6 per 100 NOK spent | Uncapped |

### Buying Level Points

Level points CAN be purchased via SAS EuroBonus:
- **1,000 level points = 10,000 bonus points** OR **1,000 SEK**
- Bonus points conversion is almost always better (Gaute has 359k+ bonus points)
- Use this as a backstop when card points or flights fall short

**Important timing:** Card points (Amex, MC Premium, DNB Saga) post on the **7th of each month**. This means spending in the last month of a qualification period won't be credited until after the deadline. Plan ahead or use level point purchases to close the gap.

**Key math for Gold via cards alone (no flights):**
- Amex Elite only: need 750,000 NOK spend (45k / 6 per 100)
- DNB Saga to 200k + Amex for rest: 20k (DNB) + remaining from Amex
- Combined strategy is almost always best -- see `references/optimization-rules.md` for scenarios

**With flights:** Each flight contributes level points based on fare class and route. 5-10 flights typically add 5,000-15,000 level points, meaning cards need to cover 30,000-40,000.

## Query Types

### "Which card?" (instant answer)
Use the table. One line: card name + reason. Factor in companion ticket proximity.

### Status Check ("am I on track?")
When Gaute asks about progress or provides a SAS app screenshot:
1. Extract current level points, flights, days remaining
2. Calculate gap: 45,000 minus current level points
3. Calculate monthly pace needed: gap / months remaining
4. Compare against estimated monthly earning from cards
5. If behind: recommend shifting spend to Amex (highest continuous level point rate)

Output format:
```
Level points: [current] / 45,000 Gold | [current] / 90,000 Diamond
Days left: [X] | Monthly pace needed: [Y] level pts/month
Amex spend: [X] / 150,000 (companion ticket 1)
DNB Saga spend: [X] / [next threshold]
Status: ON TRACK / NEEDS ATTENTION / AT RISK
```

### Companion Ticket Strategy
Amex Elite thresholds per calendar year:
- 150,000 NOK = 1 companion ticket (buy-one-get-one on bonus flights)
- 300,000 NOK = 2 companion tickets

A companion ticket on a long-haul SAS flight can be worth 50,000+ points (~5,000-7,500 NOK value). Factor this into the card selection when Gaute is within striking distance.

### Flight Booking
- **Always book on SAS.no** with SAS EB MC Premium (25 pts/100 NOK)
- **SAS Plus** earns significantly more level points per flight than SAS Go
- **Gold 50% bonus:** base flight points * 1.5 for SAS/Wideroe
- When choosing between routes/times, the fare class earning rate matters more than small price differences
- For codeshare flights, check the operating carrier's earning table on flysas.com

### Annual Card Review
Calculate whether each card pays for itself:
1. Bonus points earned * ~0.12 NOK/point = point value in NOK
2. Level points contributed toward Gold (value of Gold status: lounges, bags, priority)
3. Companion ticket value (if achieved)
4. Insurance value (Amex travel insurance, DNB rental car)
5. Subtract annual fee
6. If negative and no unique benefit, consider dropping

**Rough breakeven by card:**
- DNB Saga (2,028 kr): ~135k NOK spend at 15 pts/100 = 20,250 pts * 0.12 = 2,430 kr value. Plus level point thresholds.
- MC Premium (2,335 kr): primarily justified by 25 pts/100 on SAS.no bookings
- Amex Elite (6,900 kr): ~345k NOK spend for points alone. But companion ticket + insurance + highest domestic rate often justify it

### Monthly/Quarterly Check-in
Run this proactive assessment:
- Level points pace vs Gold (45k) and Diamond (90k)
- Amex spend vs companion ticket (150k / 300k)
- DNB Saga spend vs next threshold (100k / 200k / 500k)
- Whether any card spending should be redistributed

## Important Caveats

- **Amex acceptance in Norway** is not universal. Grocery stores (Rema, Kiwi, Coop) generally don't take it. Restaurants, hotels, and online merchants usually do. When uncertain, have a Mastercard ready.
- **FX fees:** Amex charges 2.5% on foreign currency. DNB Saga is typically lower (~1.75%). On a 10,000 NOK foreign purchase, that's 75 NOK difference -- usually not worth losing the level points, but calculate if it's a large purchase.
- **Point devaluation:** SAS can change earning rates or redemption tables. Current rates are as of early 2026. Check flysas.com/eurobonus for changes.
- **Business expenses via GTB Holding:** If Gaute uses personal cards for business, the card fees may be partially deductible. Consult revisor.

## Integration

- **financial-freedom-bot:** Card fees (11,263 kr/yr) are tracked as a fixed expense. Points value offsets this.
- **norwegian-tax-expert:** Card fee deductibility for business use.
- When Gaute sends SAS app screenshots, read the image to extract current status numbers.
