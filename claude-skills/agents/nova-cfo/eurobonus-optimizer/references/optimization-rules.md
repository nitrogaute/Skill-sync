# Optimization Rules & Decision Engine

## The Gold Equation

Gold requires 45,000 level points per 12-month qualification period.

Sources of level points:
1. **Flights** (variable, based on fare class and route)
2. **DNB Saga** (threshold-based: 10k/20k/30k)
3. **SAS EB MC Premium** (25% of bonus points, min 500/month)
4. **SAS Amex Elite** (6 per 100 NOK, continuous)
5. **Purchase** (1,000 LP = 10,000 bonus points OR 1,000 SEK)

### Buying Level Points as Backstop

When the qualification deadline is approaching and card points won't post in time (they credit on the 7th of each month), buying level points with bonus points is the most efficient backstop:
- 1,000 LP costs 10,000 bonus points (effective rate: 10 bonus pts = 1 level pt)
- Or 1,000 SEK cash (~1,060 NOK)
- Bonus points are almost always the better option if balance allows
- Check for purchase limits per qualification period before relying on this

### Flight Level Points Estimate

Gaute flies 5-10 SAS/SkyTeam flights per year. Typical level point earnings:

| Route Type | Fare Class | Level Points (approx) |
|---|---|---|
| Domestic (SVG-OSL) | SAS Go | 500-1,000 |
| Domestic (SVG-OSL) | SAS Plus | 1,000-2,000 |
| Intra-Europe | SAS Go | 750-1,500 |
| Intra-Europe | SAS Plus | 1,500-3,000 |
| Long-haul | SAS Go | 2,000-4,000 |
| Long-haul | SAS Plus/Biz | 4,000-10,000 |

**Conservative estimate for 5-10 mixed flights: 5,000-15,000 level points from flights.**

This means cards need to cover: 30,000-40,000 level points.

### Card Level Point Scenarios

**Scenario A: Heavy Amex (default domestic card)**
Assume 300,000 NOK on Amex, 100,000 on DNB Saga, 50,000 on MC Premium

| Card | Spend | Level Points |
|---|---|---|
| Amex Elite | 300,000 | 18,000 (6 per 100) |
| DNB Saga | 100,000 | 10,000 (first threshold) |
| MC Premium | 50,000 | 1,875 (25% of 7,500 bonus pts) + 6,000 min (500*12) = ~6,000 |
| **Card total** | **450,000** | **~34,000** |

Add 5,000-15,000 from flights = **39,000-49,000 level points. Gold likely achieved.**

**Scenario B: Moderate spend**
Assume 200,000 NOK on Amex, 100,000 on DNB Saga, 30,000 on MC Premium

| Card | Spend | Level Points |
|---|---|---|
| Amex Elite | 200,000 | 12,000 |
| DNB Saga | 100,000 | 10,000 |
| MC Premium | 30,000 | ~6,000 (mostly from 500/mo minimum) |
| **Card total** | **330,000** | **~28,000** |

Add 5,000-15,000 from flights = **33,000-43,000 level points. Gold at risk -- need upper end of flights.**

**Scenario C: Low spend**
Assume 100,000 NOK on Amex, 50,000 on DNB Saga, 20,000 on MC Premium

| Card | Spend | Level Points |
|---|---|---|
| Amex Elite | 100,000 | 6,000 |
| DNB Saga | 50,000 | 0 (below first threshold) |
| MC Premium | 20,000 | ~6,000 (mostly minimums) |
| **Card total** | **170,000** | **~12,000** |

Add 5,000-15,000 from flights = **17,000-27,000 level points. Gold NOT achievable.**

### Key Insight: The DNB Saga Threshold Jump

The DNB Saga card awards 10,000 level points the moment you cross 100,000 NOK in a calendar year. This is by far the most efficient level point earning at that spend level (10 pts per 1,000 NOK, compared to Amex's 6 pts per 1,000 NOK).

**Strategy:** Route enough spend to DNB Saga to cross the 100k threshold. That single threshold gives you 10,000 level points -- equivalent to spending 166,667 NOK on Amex Elite.

The second threshold (200k) is also worth targeting if spend allows: another 10,000 for only 100k incremental spend.

The third threshold (500k) requires 300k incremental spend for 10,000 points -- less efficient than Amex at that point.

### Optimal Spend Distribution

For typical household spend of 300k-500k NOK/year across cards:

1. **First 100k on DNB Saga** -- hit the first threshold for 10,000 level points
2. **All SAS.no purchases on MC Premium** -- 25 pts/100 is unbeatable. Use monthly for 500 level point minimums.
3. **Everything else on Amex Elite** -- 20 pts/100 domestically (vs 15 on MCs), plus 6 level pts/100 continuous, plus progress toward companion ticket

**If total spend exceeds 300k:** Consider routing 200k through DNB Saga for 20,000 level points, then Amex for the rest.

**If total spend exceeds 500k:** The DNB Saga 500k threshold gives diminishing returns. Better to split between DNB (200k for 20,000 level pts) and Amex (rest, for continuous 6/100 plus companion ticket progress).

---

## Card Selection Decision Tree

```
Is this a SAS.no purchase?
  YES -> SAS EB MC Premium (25 pts/100)
  NO -> Continue

Is Amex accepted at this merchant?
  NO -> Is DNB Saga close to next threshold?
    YES -> DNB Saga MC Upgrade
    NO -> DNB Saga MC Upgrade (still better than MC Premium for domestic)
  YES -> Continue

Is this a foreign currency transaction?
  YES -> Is Amex within 20k of companion ticket threshold?
    YES -> Amex Elite (worth the FX fee premium)
    NO -> DNB Saga MC Upgrade (same 20 pts, lower FX fee)
  NO -> Continue

Is the purchase domestic?
  YES -> SAS Amex Elite (20 pts/100, best domestic rate)
```

**Exception override:** If Amex Elite is within 20,000 NOK of the 150k companion ticket threshold, use Amex for EVERYTHING until the threshold is crossed. The companion ticket value (3,000-9,000 NOK) far exceeds the lost points or FX fees.

---

## Companion Ticket Strategy

The Amex Elite companion ticket is the highest-value single perk:

| Threshold | Ticket | Best Use |
|---|---|---|
| 150,000 NOK/year | 1 companion ticket | Long-haul bonus flight (saves 40-60k points) |
| 300,000 NOK/year | 2 companion tickets | Two trips or one round-trip |

**Tracking:** At any point, calculate: (Amex annual spend to date) / 150,000.
If above 70% with 3+ months left, it's achievable naturally.
If below 70%, consider routing extra spend to Amex.

**Redemption tip:** Use companion tickets on the most expensive bonus routes (long-haul business class) to maximize value per ticket.

---

## Monthly Pace Calculator

For Gold maintenance, use this formula:

```
remaining_level_points = 45,000 - current_level_points
months_remaining = days_remaining / 30
monthly_pace_needed = remaining_level_points / months_remaining

estimated_monthly_earning = (monthly_amex_spend * 0.06)
                          + (monthly_mc_premium_spend * 0.15 * 0.25)
                          + dnb_saga_threshold_expected / months_remaining
                          + estimated_flight_level_points / months_remaining

if estimated_monthly_earning >= monthly_pace_needed:
    status = "ON TRACK"
elif estimated_monthly_earning >= monthly_pace_needed * 0.8:
    status = "NEEDS ATTENTION"
else:
    status = "AT RISK"
```

---

## Annual Fee Justification

Total annual cost: 11,263 kr (DNB 2,028 + MC Premium 2,335 + Amex 6,900)

**Value extraction checklist:**

### DNB Saga (2,028 kr)
- [x] Hit 100k threshold? -> 10,000 level points (critical for Gold)
- [ ] Hit 200k threshold? -> +10,000 level points
- [ ] Used 4 lounge visits? -> ~800 kr value (200 kr/visit)
- [ ] Used rental car insurance? -> variable value

Breakeven: If DNB Saga threshold contributes 10k level points toward Gold, and Gold status is worth >2,028 kr to Gaute (it is -- lounges alone), the card pays for itself.

### MC Premium (2,335 kr)
- [ ] Booked flights on SAS.no? -> 25 pts/100 vs 20 (next best) = 5 extra pts/100
  - Need 46,700 NOK on SAS.no for the 5 extra pts to cover the fee (at 0.12 NOK/pt)
- [x] Used monthly for 500 level point minimum? -> 6,000 level points/year
  - These 6,000 level points are "free" from just one small purchase per month

Breakeven: The 6,000 guaranteed level points plus the SAS.no bonus rate justify the fee if Gaute books even moderate SAS flights.

### Amex Elite (6,900 kr)
- [ ] Achieved companion ticket? -> 3,000-9,000 kr value
- [x] Used as primary domestic card? -> 5 extra pts/100 vs MC domestic
  - At 200k domestic spend: 10,000 extra bonus points = ~1,200 kr value
- [x] Travel insurance used/valued? -> comprehensive coverage worth ~1,500-3,000 kr
- [x] Supplementary cards for family? -> Elsa earning points too

Breakeven: Companion ticket alone can cover the fee. Without it, the combination of higher earning rate + insurance + family cards typically justifies 6,900 kr at 200k+ annual spend.

---

## Seasonal Considerations

- **January-February:** New qualification period starts. Set up auto-payments on each card to ensure MC Premium earns 500/month minimum.
- **March-April:** Tax refund season. If receiving refund, consider large purchases on DNB Saga to hit 100k threshold early.
- **Summer (June-August):** Travel season. Foreign purchases increase. Route through DNB Saga (lower FX fee) unless chasing companion ticket.
- **September-October:** Check Gold progress. If behind, shift all possible spend to Amex Elite (highest continuous level point rate).
- **November-December:** Final push for Gold. Also check companion ticket status. Holiday shopping can push over thresholds.
- **Year-end:** DNB Saga thresholds reset on calendar year. Ensure any near-threshold spend happens before Dec 31.
