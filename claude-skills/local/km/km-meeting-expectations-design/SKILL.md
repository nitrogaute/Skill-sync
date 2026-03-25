---
name: km-meeting-expectations-design
description: Design guide for the Meeting Expectations dashboard. Use when building or modifying Meeting Expectations UI components, pages, or visual language.
---

# Meeting Expectations — Design Guide

Reference for replicating the visual language of this dashboard across new pages and components.

---

## Color System

### KM Brand Palette Reference

All colors below are sourced from the Kongsberg Maritime brand palette. Organized by family:

**Slate Neutrals** (cool, dark-to-light):

| Hex       | Role                |
|-----------|---------------------|
| `#1b2428` | Near-black          |
| `#2d3a40` | Dark slate          |
| `#5c6972` | Medium slate        |
| `#c6ced2` | Light cool gray     |
| `#f3f6f7` | Near-white cool     |

**Warm Neutrals** (light-to-dark):

| Hex       | Role                |
|-----------|---------------------|
| `#e6e2dd` | Warm gray light     |
| `#d3cfc9` | Warm gray medium    |
| `#b3ada5` | Warm gray dark      |

**Teal Family** (dark-to-light):

| Hex       | Role                |
|-----------|---------------------|
| `#032a39` | Deepest teal        |
| `#004c56` | Very dark teal      |
| `#08435a` | Dark teal           |
| `#23627a` | Blue-teal           |
| `#4d7a8b` | Muted teal          |
| `#006f84` | Core teal           |
| `#0e8997` | Medium bright teal  |
| `#1d7a85` | Teal                |
| `#3fbac2` | Bright teal         |
| `#9ed0d9` | Light teal          |
| `#d2eff2` | Pale teal           |
| `#00d6e6` | Electric teal       |

**Accent:**

| Hex       | Role                |
|-----------|---------------------|
| `#9a2e2e` | Deep red            |

---

### C Constant — Full Token Map

All colors in the application flow through the `C` object at the top of `dashboard.jsx`. Never use hardcoded hex values outside this object.

| Token           | Hex       | Usage                                                    |
|-----------------|-----------|----------------------------------------------------------|
| `bg`            | `#f3f6f7` | Page background, table row hover, inner fill blocks      |
| `white`         | `#FFFFFF` | Card/panel surfaces                                      |
| `border`        | `#c6ced2` | Card borders, dividers, separators                       |
| `borderLight`   | `#e6e2dd` | Table row borders, subtle fills, progress bar tracks, read-only input bg |
| `text`          | `#1b2428` | Primary text, headings                                   |
| `textSecondary` | `#5c6972` | Descriptions, secondary labels, form labels              |
| `textTertiary`  | `#b3ada5` | Timestamps, hints, axis labels, read-only input text     |
| `cost`          | `#08435a` | Cost Accuracy KPI + system-generated badge text          |
| `time`          | `#0e8997` | Time Accuracy KPI                                        |
| `okrAchieve`    | `#23627a` | OKR Performance KPI + lookup badge text + project selector accent |
| `okrStab`       | `#3fbac2` | OKR Stability KPI                                        |
| `bizCase`       | `#9a2e2e` | Business Case Approval KPI                               |
| `danger`        | `#9a2e2e` | Critical status, negative trends, free-text indicators   |
| `warning`       | `#b3ada5` | Below target, at risk (same value as textTertiary)       |
| `success`       | `#006f84` | On target, approved, strong + calculated badge text      |
| `chartGrid`     | `#e6e2dd` | Chart grid lines                                         |
| `successBg`     | `#d2eff2` | Success badge bg, system badge bg, calculated badge bg   |
| `warningBg`     | `#e6e2dd` | Warning badge bg, constrained input badge bg, free-text callout bg |
| `dangerBg`      | `#f5ebeb` | Danger badge bg, free-text stat bg                       |
| `activeTab`     | `#032a39` | Active tab/section bg, submit button bg                  |
| `required`      | `#4d7a8b` | Required field indicators, input badge text, required borders |

### KPI Colors (Semantic)

Each KPI has a dedicated color used consistently for its gauge, chart line, dot indicator, and badge tint.

| KPI                    | Token        | Hex       | KM Name            |
|------------------------|--------------|-----------|---------------------|
| Cost Accuracy          | `cost`       | `#08435a` | Dark teal           |
| Time Accuracy          | `time`       | `#0e8997` | Medium bright teal  |
| OKR Performance        | `okrAchieve` | `#23627a` | Blue-teal           |
| OKR Stability          | `okrStab`    | `#3fbac2` | Bright teal         |
| Business Case Approval | `bizCase`    | `#9a2e2e` | Deep red            |

### Status Colors

| Status    | Token       | Bg Token     | Usage                          |
|-----------|-------------|--------------|--------------------------------|
| Success   | `success`   | `successBg`  | On target, approved, strong    |
| Warning   | `warning`   | `warningBg`  | Below target, at risk, pending |
| Danger    | `danger`    | `dangerBg`   | Critical, negative trends      |

Status badges always pair the text token with the corresponding `Bg` token. The KM palette has no amber/yellow, so warning uses the warm gray family for a muted caution tone.

### Source-Type Badge Colors (Data Requirements)

Used in the Data Requirements tab to visually differentiate field sources:

| Source      | Background     | Text Color     |
|-------------|----------------|----------------|
| System      | `C.successBg`  | `C.cost`       |
| Lookup      | `C.borderLight` | `C.okrAchieve` |
| Input       | `C.warningBg`  | `C.required`   |
| Calculated  | `C.successBg`  | `C.success`    |
| Free text   | `C.dangerBg`   | `C.danger`     |

### Derived Usage Patterns

- **KPI tinted badges:** `background: {kpiColor}12` (hex + `12` for ~7% opacity), `color: {kpiColor}`
- **Selected card shadow:** `0 2px 20px {kpiColor}12`
- **Open accordion border:** `{kpiColor}44` (~27% opacity)
- **Selected project button bg:** `{kpiColor}08` (~3% opacity)
- **Unused brand colors available for future use:** `#004c56`, `#1d7a85`, `#9ed0d9`, `#2d3a40`, `#d3cfc9`, `#00d6e6`

---

## Typography

### Font Stack

**Primary:** `'Inter', sans-serif` — used for all UI text via inline styles + Google Fonts import inside the component.

> Note: `index.html` also loads DM Sans, DM Mono, and Source Serif 4, but the dashboard component uses Inter exclusively.

### Scale

| Element                  | Size  | Weight | Extra                                          |
|--------------------------|-------|--------|-------------------------------------------------|
| Page title (h1)          | 30px  | 700    | `letter-spacing: -0.025em`, `line-height: 1.15` |
| Section heading (h2)     | 20px  | 700    |                                                  |
| Form section heading (h3)| 16px  | 700    |                                                  |
| Card heading (h3)        | 15px  | 700    |                                                  |
| Subheading (h4)          | 13px  | 600    |                                                  |
| Body text                | 14px  | 400    | `line-height: 1.5` or `1.6`                     |
| Small body               | 13px  | 500    |                                                  |
| Table cell value         | 15px  | 600    |                                                  |
| Form input text          | 13px  | 400    |                                                  |
| Large stat number        | 34px  | 700    | `line-height: 1`                                 |
| Medium stat number       | 28px  | 700    |                                                  |
| OKR performance (form)   | 18px  | 700    | monospace                                        |
| Gauge value              | 22px  | 600    |                                                  |
| KPI card label           | 11px  | 600    | `line-height: 1.3`                               |
| Form label               | 11px  | 600    | `letter-spacing: 0.04em`                         |
| Overline / category      | 11px  | 600    | `letter-spacing: 0.14em`, `text-transform: uppercase` |
| Table header             | 11px  | 600    | `letter-spacing: 0.06em`, `text-transform: uppercase` |
| Data req table header    | 10px  | 600    | `letter-spacing: 0.08em`, `text-transform: uppercase` |
| Context bar label        | 10px  | 600    | `letter-spacing: 0.08em`, `text-transform: uppercase` |
| Badge / status text      | 11px  | 600    |                                                  |
| Trend percentage         | 11px  | 600    | monospace                                        |
| Gauge target label       | 10px  | 400    |                                                  |
| Footer                   | 11px  | 400    | monospace                                        |

### Monospace Usage

`'Inter', monospace` is used for:
- Trend values (`+1.8%`)
- Chart axis tick labels
- Data field names in tables
- Example values
- Formula text
- Target badges
- Form context bar values (project ID, percentages)
- Reporting period badges
- Footer timestamp

---

## Spacing & Layout

### Page Container

```
max-width: 1160px
margin: 0 auto
padding: 40px 28px 48px
```

### Grid Patterns

| Context                  | Columns             | Gap   |
|--------------------------|---------------------|-------|
| KPI cards row            | `repeat(5, 1fr)`    | 14px  |
| Charts row               | `3fr 2fr`           | 16px  |
| Input safety breakdown   | `repeat(5, 1fr)`    | 12px  |
| Summary stat cards       | `repeat(3, 1fr)`    | 14px  |
| Key principles callout   | `repeat(3, 1fr)`    | 20px  |
| Responsibility matrix    | `repeat(3, 1fr)`    | 12px  |
| Formula/meta row         | `1fr 1fr 1fr`       | 14px  |
| Project context bar      | `repeat(5, 1fr)`    | 12px  |
| KR form fields           | 6 columns (`1fr` each) | 12px |
| Cost form fields         | `1fr 1fr 1fr`       | 12px  |
| Milestone form fields    | `1fr 1fr 1fr 1fr`   | 12px  |
| KR change form fields    | `1fr 1fr 1fr`       | 14px  |

### Common Spacing Values

| Context                              | Value   |
|--------------------------------------|---------|
| Card internal padding                | 28px (or 24px 28px for form intro) |
| KPI card padding                     | 24px 16px 20px |
| Accordion header padding             | 22px 28px |
| Accordion body padding               | 0 28px 28px |
| Info card padding                    | 28px 32px |
| Stat block padding                   | 16px 20px |
| Meta block padding                   | 14px 18px |
| Context bar cell padding             | 14px 18px |
| Gap between section heading and chart | 20px (marginBottom on heading wrapper) |
| Gap between major sections           | 36px    |
| Gap between card sections            | 14px    |
| Gap between form sections            | 20px (marginBottom) |
| Tab bar padding                      | 16px 0 28px |
| Section tabs marginBottom            | 24px    |
| Header bottom padding                | 24px    |
| Footer top margin/padding            | 36px / 20px |

---

## Borders & Corners

### Border Radius

| Element                        | Radius |
|--------------------------------|--------|
| Cards, panels, accordions      | 14px   |
| KPI detail banner              | 12px   |
| Data flow step boxes           | 12px   |
| Inner stat/meta blocks         | 10px   |
| Project selector buttons       | 10px   |
| Section tab buttons            | 10px   |
| Form field sections            | 10px   |
| Form inputs / selects          | 8px    |
| Tab buttons (main)             | 8px    |
| Info badges (period, mockup)   | 8px    |
| Free-text callout              | 8px    |
| Status badges                  | 6px    |
| Progress bar (form, 6px tall)  | 3px    |
| Type pills (in tables)         | 4px    |
| Safety score bar               | 4px    |
| Percentage badges (project)    | 4px    |
| Bar chart bar tops             | 3px    |
| Mini progress bars (table)     | 2px    |
| Legend color squares            | 2px    |

### Borders

- **Default card:** `1px solid ${C.border}`
- **Selected KPI card:** `1.5px solid {kpiColor}`
- **Selected project button:** `1.5px solid ${C.okrAchieve}`
- **Active section tab:** `1.5px solid ${C.activeTab}`
- **Dashed "more" button:** `1.5px dashed ${C.border}`
- **Header bottom:** `1.5px solid ${C.border}`
- **Tab bar bottom:** `1px solid ${C.border}`
- **Footer top:** `1px solid ${C.border}`
- **Table header row:** `2px solid ${C.border}` bottom
- **Table body rows:** `1px solid ${C.borderLight}` bottom
- **Responsibility card left accent:** `3px solid {roleColor}`
- **Form input:** `1px solid ${C.border}`
- **Read-only input:** `1px solid ${C.borderLight}`
- **Required input:** `borderColor: ${C.required}`
- **Free-text callout:** `1px solid ${C.border}`
- **Form inner sections:** `1px solid ${C.borderLight}`

---

## Shadows

| Context              | Value                              |
|----------------------|------------------------------------|
| Default card         | `0 1px 3px rgba(0,0,0,0.04)`      |
| Selected KPI card    | `0 2px 20px {kpiColor}12`         |
| Chart tooltip        | `0 4px 20px rgba(0,0,0,0.08)`     |

Shadows are minimal throughout. Most cards rely on borders, not shadows.

---

## Animation

### Entry Animation

All animated elements use the same keyframe:

```css
@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

Applied via: `animation: fadeSlideUp {duration} ease {delay} both`

| Element              | Duration | Delay pattern          |
|----------------------|----------|------------------------|
| Header               | 0.5s     | 0s                     |
| KPI cards            | 0.5s     | 0.1s + index * 0.08s   |
| Accordion items      | 0.4s     | 0.1s + index * 0.06s   |
| Expanded content     | 0.3s     | 0s                     |

### Transitions

| Property                | Duration | Easing                       |
|-------------------------|----------|------------------------------|
| Card border/shadow      | 0.35s    | `ease`                       |
| Gauge arc fill          | 1s       | `cubic-bezier(0.4, 0, 0.2, 1)` |
| Tab button styles       | 0.25s    | `ease`                       |
| Section tab / form btn  | 0.2s     | default                      |
| Accordion border color  | 0.3s     | `ease`                       |
| Chevron rotation        | 0.3s     | `ease`                       |
| Table row hover bg      | 0.2s     | default                      |
| Expand accordion inner  | 0.15s    | default                      |
| Progress bar width      | 0.8s     | `ease`                       |
| Form progress bar       | 0.5s     | default                      |
| Form input border       | 0.2s     | default                      |
| Page mount opacity      | 0.5s     | `ease`                       |

---

## Component Patterns

### Card (Panel)

The default container for any section of content:

```
background: C.white
border: 1px solid C.border
border-radius: 14px
padding: 28px (or 24px 28px for form sections)
```

Cards contain a heading group (h3 + subtitle) with `marginBottom: 20px`, then content.

### Section Heading Group

```jsx
<h3 style={{ fontSize: 15, fontWeight: 700 }}>Title</h3>
<p style={{ fontSize: 12, color: C.textTertiary, marginTop: 3 }}>Subtitle</p>
```

### Status Badge

A small inline pill showing state:

```
padding: 3px 8px  (small) or 4px 12px (standard)
border-radius: 6px
font-size: 10-11px
font-weight: 500-600
background: C.successBg / C.warningBg / C.dangerBg
color: C.success / C.warning / C.danger
```

Content format: `{icon} {label}` where icon is `✓` (success), `↓` (below), `○` (pending).

### Main Tab Bar

Horizontal row of pill buttons. Active: `C.activeTab` bg, white text. Inactive: transparent bg, secondary text. Each button has a Unicode glyph icon and label.

```
padding: 10px 22px
border-radius: 8px
font-size: 13px
font-weight: 600
gap: 8px (icon to label)
```

### Section Tabs (PM Reporting Form)

Larger bordered tab buttons with emoji icons and sub-count text. Active: `C.activeTab` bg + border, white text. Inactive: `C.white` bg, `C.border` border, secondary text.

```
padding: 12px 20px
border-radius: 10px
border: 1.5px solid (activeTab or border)
font-size: 13px / 10px sub-count
gap: 8px (icon to text)
```

### Table

- Header row: uppercase, 11px, weight 600, tertiary color, letter-spacing 0.06em, 2px bottom border
- Header color dots: 6px circles with KPI color at 0.7 opacity
- Body cells: 14-15px, weight 600 for values
- Row hover: `C.bg` background
- Mini progress bars in cells: 48px wide, 3px tall, borderLight track, status-colored fill

### Arc Gauge

SVG-based, 120px default size. A 240-degree arc (from -210deg to +30deg). Supports values > 100% via dynamic `maxVal` (caps at 120 when target > 100 or value > 100):
- Track: 6px stroke, `C.borderLight`, round caps
- Value fill: 6px stroke, KPI color, round caps, animated with cubic-bezier
- Target marker: 4px radius white circle with 2px stroke (`C.success` if met, `C.warning` if not)
- Center text: value at 22px/600, target label at 10px/400

### Tooltip (Charts)

```
background: C.white
border: 1px solid C.border
border-radius: 10px
padding: 10px 14px
box-shadow: 0 4px 20px rgba(0,0,0,0.08)
```

Label in tertiary color (11px), values in entry color (13px, weight 600).

### Chart Styling

- Grid: dashed (`strokeDasharray: "3 3"`), `C.chartGrid`, vertical lines hidden
- Axes: no axis line, no tick line, tertiary color, 11px, monospace
- Area chart: 2.5px stroke, gradient fill from 12% to 1% opacity of KPI color
- Area dots: 3px radius, white fill, 2px KPI-colored stroke. Active: 5px, filled, white stroke.
- Target line: tertiary color, 1px, dashed (`5 4`), no fill, no dots
- Bar chart: 10px bar width, 3px top radius
- Y-axis domain adapts: 50–100 for biz_case, 75–115 for okr_achieve, 75–100 for others

### Accordion (Data Requirements)

Collapsed: card with clickable header row containing color dot (12px), title, field count + constraint summary, and rotate-able chevron (`▾`).

Expanded: reveals meta grid (formula, frequency, owner in `10px` uppercase labels), full data field table with source-type and input-type badges, and optional free-text callout box.

### Input Safety Score Bar

Stacked horizontal bar showing field source distribution:
```
height: 8px, borderRadius: 4, background: C.borderLight
```
Each segment is colored by source type (see Source-Type Badge Colors). Includes legend below and percentage label.

### KPI Detail Banner

A thin horizontal bar between KPI cards and charts:

```
border-radius: 12px
padding: 16px 24px
display: flex, alignItems: center, gap: 16px
```

Contains: 10px color dot, bold label + tertiary description, italic purpose text on the right.

### Data Flow Diagram

Horizontal chain of step boxes connected by arrows. Each box: `border-radius: 12px`, `padding: 18px 24px`, `border: 1px solid C.border`, emoji icon, bold label, tertiary subtitle. Arrows built from a 40px x 2px line + CSS triangle.

### Legend

Inline flex row, centered, with colored squares (8px, 2px radius) or circles (5-6px) and 11px labels in secondary color.

### Form Inputs

Three input styles defined in `ProjectInputFormTab`:

**Standard input:**
```
width: 100%, padding: 9px 12px, borderRadius: 8
border: 1px solid C.border, fontSize: 13
background: C.white, color: C.text
transition: border-color 0.2s
```

**Read-only input:** Extends standard with `background: C.borderLight`, `color: C.textTertiary`, `cursor: not-allowed`, `border: 1px solid C.borderLight`.

**Required input:** Standard input with `borderColor: C.required`.

**Form labels:** `fontSize: 11, fontWeight: 600, color: C.textSecondary, letterSpacing: 0.04em`, displayed as block.

### Field Indicator Icons

Inline icons appended to form labels to indicate field behavior:
- 🔒 Locked after approval — `color: C.textTertiary`
- ⚙ System-generated — `color: C.cost`
- ∑ Auto-calculated — `color: C.success`
- `● REQUIRED` text — `color: C.required`, fontSize 9

### Project Selector

Horizontal flex-wrap row of selectable project cards:
- `borderRadius: 10, border: 1.5px solid`, selected uses `C.okrAchieve` border + `{color}08` tinted bg
- Contains project name (13px/600), metadata line (11px), and percentage badge
- Includes a dashed `+ N more projects…` ghost button

### Context Bar

Row of small info cells in a 5-column grid:
```
background: C.white, border: 1px solid C.border
borderRadius: 10, padding: 14px 18px
```
Label: 10px uppercase with optional indicator icon. Value: 14px/600 monospace.

---

## Interaction States

| Element               | Default                  | Hover / Active                              |
|-----------------------|--------------------------|---------------------------------------------|
| KPI card              | 1px border, light shadow | 1.5px colored border, tinted shadow         |
| Main tab button       | Transparent bg           | `C.activeTab` bg, white text                |
| Section tab button    | White bg, gray border    | `C.activeTab` bg + border, white text       |
| Project selector      | White bg, gray border    | `C.okrAchieve` border, tinted bg            |
| Table row             | Transparent              | `C.bg` background                           |
| Accordion header      | Default border           | Border tints to `{kpiColor}44`              |
| Chevron               | 0deg rotation            | 180deg rotation when open                   |
| Submit button         | `C.activeTab` bg         | `opacity` transition                        |

---

## Responsive Notes

- The page uses a fixed `maxWidth: 1160px` centered container.
- KPI cards grid uses `repeat(5, 1fr)` — would need breakpoints for smaller screens.
- Charts grid is `3fr 2fr` — also fixed ratio.
- Header uses `flexWrap: wrap` with `gap: 20px` for narrow viewports.
- Tables use `overflowX: auto` for horizontal scrolling.
- Data flow diagram uses `flexWrap: wrap`.
- Project selector uses `flexWrap: wrap`.
- Form intro bar uses `flexWrap: wrap` with `gap: 16px`.
