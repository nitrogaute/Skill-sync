---
name: gtb-design
description: "GTB Ventures AS presentation and slide design skill. This skill should be used when creating slides, presentations, or visual assets for GTB Ventures - a Nordic venture capital firm. Includes the neumorphic design system, Venture Red color palette, Inter typography, and component patterns."
---

# GTB Ventures Design System

This skill provides the design system, component patterns, and visual guidelines for creating presentations and slides for GTB Ventures AS.

## When to Use

- Creating pitch deck slides for GTB Ventures
- Building presentation components with neumorphic styling
- Designing financial dashboards, charts, or metrics displays
- Creating process flowcharts or timeline visualizations
- Any visual asset that needs to follow GTB Ventures brand guidelines

## Design Philosophy

GTB Ventures uses a **Neumorphic (Soft UI)** design system characterized by:
- Soft shadows creating depth illusion
- Single base color for all surfaces (shadows create depth, not different colors)
- Clean, modern aesthetic with technical precision
- Dark and light theme support

## Quick Reference

### Primary Colors

| Name | Hex | Usage |
|------|-----|-------|
| Venture Red | `#e94560` | Primary accent, CTAs, highlights |
| Venture Red Hover | `#ff5a75` (dark) / `#d63850` (light) | Hover states |

### Theme Colors

**Dark Theme** (default):
- Background/Surface: `#1e1e2e`
- Shadow Light: `#2a2a3e`
- Shadow Dark: `#141420`

**Light Theme**:
- Background/Surface: `#e0e5ec` (ALL surfaces same color)
- Shadow Light: `#ffffff`
- Shadow Dark: `#a3b1c6`

### Typography

- **Font Family**: Inter, -apple-system, BlinkMacSystemFont, sans-serif
- **Display**: 72px, weight 700, tracking -0.03em
- **H1**: 48px, weight 700, tracking -0.02em
- **H2**: 36px, weight 600, tracking -0.02em
- **H3**: 24px, weight 600, tracking -0.01em
- **Body**: 16px, weight 400
- **Caption**: 12px, weight 500, tracking 0.02em

## Neumorphic Shadow Patterns

### Raised Element (default)
```css
box-shadow: 6px 6px 12px ${shadowDark}, -6px -6px 12px ${shadowLight};
```

### Pressed/Inset Element
```css
box-shadow: inset 4px 4px 8px ${shadowDark}, inset -4px -4px 8px ${shadowLight};
```

### Accent Glow (for primary buttons)
```css
box-shadow: 4px 4px 8px ${shadowDark}, -4px -4px 8px ${shadowLight}, 0 0 20px ${accentShadow};
```

## Component Patterns

### NeuCard
Raised card component with hover and press states.
- Use `rounded-2xl` for border radius
- Padding: `p-6` default
- Interactive cards lift on hover (`translateY(-2px)`)

### NeuButton
Button with neumorphic shadows.
- Sizes: sm (`px-4 py-2`), md (`px-6 py-3`), lg (`px-8 py-4`)
- Accent variant adds glow effect
- Press state uses inset shadow

### NeuProgress
Progress bar with inset track and gradient fill.
- Track uses inset shadow
- Fill uses accent gradient with glow

### NeuBadge
Small label/tag component.
- Colors: default, accent, green, blue
- Use for status indicators, labels

## Slide Templates

### Title Slide
- Large headline (Display size)
- Subtitle in muted text
- Stage selection pills (Pre-Seed, Seed, Series A)
- Decorative neumorphic element

### Content Slide
- Section badge
- H2 title
- Two-column layout with NeuCards
- Bullet lists with check icons

### Process Slide
- Flowchart layout
- Numbered step cards with icons
- Arrows connecting steps
- Color-coded by phase:
  - Brainstorming: Amber `#f59e0b`
  - Specification: Blue `#4a90d9`
  - Planning: Purple `#8b5cf6`
  - Execution: Accent Red `#e94560`
  - Testing: Green `#22c55e`

### Metrics Slide
- 4-column grid of metric cards
- Each card: icon, value, label, trend badge
- Hover interaction shows toast

## Chart Styling

For financial charts using Recharts:
- Use theme colors for data series
- Custom tooltip with neumorphic styling
- Grid lines use `theme.border` color
- Accent color for primary data series
- Gradient fills for area charts

## Live Reference

The **gtb-design-showcase** project is the source of truth for this design system. When creating GTB Ventures slides or presentations, refer to the showcase for the latest implementation:

**Primary Reference** (always check this first):
- `.claude/skills/artifacts-builder/gtb-design-showcase/src/App.tsx` - Complete working implementation with all components, themes, charts, and slide examples

The showcase includes:
- Theme system with dark/light mode toggle
- All neumorphic components (NeuCard, NeuButton, NeuProgress, NeuBadge, MetricCard)
- Financial charts with Recharts (AreaChart, BarChart, PieChart)
- Process flowchart slide example
- Analytics dashboard with investment timeline
- Toast notifications with Sonner

To see the showcase in action:
```bash
cd .claude/skills/artifacts-builder/gtb-design-showcase
npm install
npm run dev
```

## Implementation Notes

1. **Always use the same base color** for bg, bgAlt, and surface in neumorphism
2. **Shadows create ALL depth** - never use different surface colors for hierarchy
3. **Inter font** must be loaded from Google Fonts or locally
4. **Theme toggle** should be fixed position, top-right corner
5. **Toast notifications** use Sonner library with neumorphic styling
