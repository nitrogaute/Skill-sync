---
name: km-design-guide
description: >
  Kongsberg Maritime "Meeting Expectations" dashboard design system. Use this skill whenever
  building, modifying, or extending React components for the KM Meeting Expectations dashboard
  or any KM-branded UI. Trigger on any mention of "Meeting Expectations", "KM dashboard",
  "Kongsberg Maritime UI", KPI cards, project reporting forms, or when creating new dashboard
  pages/tabs that should match the existing visual language. Also use when the user asks to
  build any teal-themed maritime dashboard component, fix styling inconsistencies in the
  dashboard, or add new data visualizations to the KM system.
---

# KM Meeting Expectations — Design Skill

This skill ensures all new components and pages match the established visual language of the
Kongsberg Maritime "Meeting Expectations" dashboard. Read this file first for the core rules,
then consult `references/full-design-spec.md` for exact values when implementing.

## Core Principles

1. **Everything flows through the `C` color constant.** Never hardcode hex values. Every color
   in the app is a token in the `C` object at the top of `dashboard.jsx`. When adding new
   components, reference `C.tokenName` — never raw hex strings.

2. **The palette is teal-dominant with one red accent.** The entire KM brand palette lives in a
   cool slate-to-teal spectrum. The only warm accent is `#9a2e2e` (deep red), used for the
   Business Case KPI and danger states. There is no amber/yellow — warnings use the warm gray
   family (`C.warning` / `C.warningBg`).

3. **Each KPI owns a color.** Cost Accuracy, Time Accuracy, OKR Performance, OKR Stability,
   and Business Case Approval each have a dedicated teal-shade (or red for biz case). That
   color is used consistently for its gauge arc, chart line, dot indicator, badge tint,
   selected-card border, and shadow.

4. **Typography is Inter only.** All UI text uses `'Inter', sans-serif`. Monospace treatment
   (`'Inter', monospace`) is reserved for data values: trend percentages, axis ticks, field
   names, formulas, target badges, and timestamps.

5. **Minimal shadows, strong borders.** Cards rely on `1px solid C.border` — not drop shadows.
   Shadows are used sparingly (default card: `0 1px 3px rgba(0,0,0,0.04)`). Selected/active
   states use colored borders + tinted shadows.

6. **Consistent radius scale.** Cards/panels = 14px. Inner blocks/tabs = 10px. Inputs/buttons
   = 8px. Badges = 6px. Small pills/bars = 2–4px.

7. **Fade-slide-up entry animation.** All animated elements share a single keyframe
   (`fadeSlideUp`: opacity 0→1, translateY 12px→0). Stagger with `index * 0.06–0.08s` delay.

## Quick Reference — Color Tokens

When implementing, use these semantic tokens:

| Token           | Purpose                                      |
|-----------------|----------------------------------------------|
| `C.bg`          | Page background, hover fills                 |
| `C.white`       | Card surfaces                                |
| `C.border`      | Card borders, dividers                       |
| `C.borderLight` | Subtle borders, read-only input bg, tracks   |
| `C.text`        | Primary text                                 |
| `C.textSecondary` | Labels, descriptions                       |
| `C.textTertiary`  | Hints, timestamps, axis labels             |
| `C.activeTab`   | Active tab bg, submit button bg              |
| `C.success/Bg`  | On target, approved                          |
| `C.warning/Bg`  | Below target, at risk                        |
| `C.danger/Bg`   | Critical, negative                           |
| `C.cost`        | Cost Accuracy KPI color                      |
| `C.time`        | Time Accuracy KPI color                      |
| `C.okrAchieve`  | OKR Performance KPI color                    |
| `C.okrStab`     | OKR Stability KPI color                      |
| `C.bizCase`     | Business Case Approval KPI color             |
| `C.required`    | Required field indicators                    |

## Quick Reference — Typography

| Element           | Size | Weight | Notes                              |
|-------------------|------|--------|------------------------------------|
| Page title        | 30px | 700    | letter-spacing: -0.025em           |
| Section heading   | 20px | 700    |                                    |
| Card heading      | 15px | 700    |                                    |
| Body text         | 14px | 400    | line-height: 1.5                   |
| Overline/category | 11px | 600    | uppercase, letter-spacing: 0.14em  |
| Badge text        | 11px | 600    |                                    |
| Large stat        | 34px | 700    |                                    |
| Form label        | 11px | 600    | letter-spacing: 0.04em             |
| Table header      | 11px | 600    | uppercase, letter-spacing: 0.06em  |

## Implementation Checklist

Before submitting any new KM dashboard component, verify:

- [ ] All colors reference `C.tokenName` — no raw hex values
- [ ] Font is Inter with correct size/weight from the typography scale
- [ ] Cards use `borderRadius: 14`, inner blocks use `10`, inputs use `8`
- [ ] Status badges pair text token with matching `Bg` token
- [ ] KPI-specific elements use that KPI's dedicated color token
- [ ] Entry animations use `fadeSlideUp` with staggered delays
- [ ] Monospace is only used for numeric/data values, not labels
- [ ] Page container is `maxWidth: 1160px`, centered, with `padding: 40px 28px 48px`

## Detailed Specifications

For exact pixel values, spacing tables, component patterns, interaction states, chart
styling, form input specs, and the complete color token map, read:

```
references/full-design-spec.md
```

Read this reference file whenever you need to implement a specific component (gauge, table,
accordion, form input, chart, badge, etc.) or need the precise spacing/border/shadow values.
