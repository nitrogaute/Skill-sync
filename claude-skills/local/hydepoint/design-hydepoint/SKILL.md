---
name: design-hydepoint
description: HydePoint design system - Apple/OpenAI-inspired clean modern UI with color palette, typography, spacing, animations, and motion patterns. Use when building or reviewing HydePoint UI components.
---

# HydePoint Design Guide

A clean, modern design system inspired by Apple and OpenAI. Built for consistency, clarity, and exceptional user experiences across UI and motion graphics.

---

## Color Palette

Our color system is designed to be accessible, harmonious, and expressive across all touchpoints.

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Primary** | `#127369` | rgb(18, 115, 105) | Primary actions, links, key UI elements |
| **Dark** | `#014542` | rgb(1, 69, 66) | Headlines, dark backgrounds, emphasis |
| **Accent** | `#8AA6A3` | rgb(138, 166, 163) | Secondary elements, borders, subtle backgrounds |
| **Neutral Dark** | `#4C5958` | rgb(76, 89, 88) | Body text, icons, secondary content |
| **Neutral Light** | `#BFBFBF` | rgb(191, 191, 191) | Placeholders, disabled states, dividers |
| **Highlight** | `#2AB686` | rgb(42, 182, 134) | Success states, highlights, CTAs |

### Color Usage Guidelines

- **Primary (#127369)** — Use for primary buttons, active states, links, and key interactive elements
- **Dark (#014542)** — Reserve for headlines, footer backgrounds, and high-contrast sections
- **Accent (#8AA6A3)** — Apply to secondary buttons, card borders, and hover states
- **Highlight (#2AB686)** — Use sparingly for success messages, badges, and important callouts

### Motion Graphics Color Usage

- **Primary → Highlight** gradients work well for animated progress indicators
- **Dark (#014542)** is ideal for motion backgrounds—provides contrast without harshness
- Use **Accent (#8AA6A3)** for secondary animated elements and trails
- **Highlight (#2AB686)** for attention-grabbing animated accents and pulses

---

## Typography

**Font Family:** Inter

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
```

### Type Scale

| Style | Size | Weight | Letter Spacing | Line Height | Usage |
|-------|------|--------|----------------|-------------|-------|
| **Display** | 64px | 600 | -0.035em | 1.1 | Hero headlines |
| **H1** | 48px | 600 | -0.03em | 1.15 | Page titles |
| **H2** | 36px | 600 | -0.025em | 1.2 | Section headers |
| **H3** | 28px | 600 | -0.02em | 1.3 | Subsection headers |
| **H4** | 22px | 600 | -0.015em | 1.4 | Card titles, labels |
| **Body Large** | 18px | 400 | 0 | 1.6 | Lead paragraphs |
| **Body** | 16px | 400 | 0 | 1.6 | Default body text |
| **Body Small** | 14px | 400 | 0 | 1.5 | Secondary text |
| **Caption** | 12px | 500 | 0.08em | 1.4 | Labels, metadata |

### Typography Guidelines

- Use **negative letter-spacing** on headlines for a refined, modern feel
- Body text should maintain comfortable **1.5-1.6 line height** for readability
- Reserve **weight 600** for headings; use **400** for body copy
- Captions and labels may use **uppercase** with increased letter-spacing

### Motion Typography Scale

For video and motion graphics at 1920x1080:

| Style | Size | Weight | Usage |
|-------|------|--------|-------|
| **Hero** | 120-180px | 600 | Full-screen titles, intro text |
| **Title** | 72-96px | 600 | Section titles, key messages |
| **Subtitle** | 48-60px | 500 | Supporting headlines |
| **Body** | 32-42px | 400 | Descriptions, longer text |
| **Label** | 24-28px | 500 | Tags, small labels, timestamps |
| **Micro** | 16-20px | 500 | Fine print, legal text |

---

## Spacing System

A consistent 4px base unit creates rhythm and hierarchy throughout the interface.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight gaps, icon padding |
| `--space-2` | 8px | Inline spacing, small gaps |
| `--space-3` | 12px | Input padding, compact spacing |
| `--space-4` | 16px | Default component padding |
| `--space-5` | 24px | Card padding, section gaps |
| `--space-6` | 32px | Component groups |
| `--space-7` | 48px | Section padding |
| `--space-8` | 64px | Large section breaks |
| `--space-9` | 96px | Page sections |
| `--space-10` | 128px | Hero/footer padding |

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 6px | Buttons, tags, small inputs |
| `--radius-md` | 10px | Cards, inputs, dropdowns |
| `--radius-lg` | 16px | Modals, large cards |
| `--radius-xl` | 24px | Hero sections, feature cards |
| `--radius-full` | 50% | Avatars, circular buttons |

---

## Buttons

### Variants

#### Primary Button
```css
background: #127369;
color: #FFFFFF;
padding: 12px 24px;
border-radius: 10px;
font-weight: 500;
```
Use for main actions and CTAs.

#### Secondary Button
```css
background: #F5F7F7;
color: #014542;
padding: 12px 24px;
border-radius: 10px;
font-weight: 500;
```
Use for secondary actions alongside primary buttons.

#### Ghost Button
```css
background: transparent;
color: #127369;
border: 1px solid rgba(18, 115, 105, 0.08);
padding: 12px 24px;
border-radius: 10px;
```
Use for tertiary actions or within cards.

#### Outline Button
```css
background: transparent;
color: #127369;
border: 1.5px solid #127369;
padding: 12px 24px;
border-radius: 10px;
```
Use when you need visual emphasis without solid fill.

### Button Sizes

| Size | Padding | Font Size | Radius |
|------|---------|-----------|--------|
| Small | 8px 16px | 13px | 6px |
| Medium | 12px 24px | 14px | 10px |
| Large | 16px 32px | 16px | 10px |

### Hover States

- **Primary:** Darken to `#014542`, subtle lift with shadow
- **Secondary:** Transition to accent color `#8AA6A3`
- **Ghost:** Light background fill `#F5F7F7`
- **Outline:** Fill with primary color, text becomes white

---

## Input Fields

### Default Input
```css
font-size: 15px;
padding: 12px 16px;
border: 1.5px solid rgba(18, 115, 105, 0.08);
border-radius: 10px;
background: #FFFFFF;
```

### States

| State | Border Color | Shadow |
|-------|--------------|--------|
| Default | `rgba(18, 115, 105, 0.08)` | None |
| Hover | `#8AA6A3` | None |
| Focus | `#127369` | `0 0 0 3px rgba(18, 115, 105, 0.1)` |
| Error | `#E53935` | `0 0 0 3px rgba(229, 57, 53, 0.1)` |
| Success | `#2AB686` | `0 0 0 3px rgba(42, 182, 134, 0.1)` |

### Input Guidelines

- Always include a visible label above the input
- Placeholder text should be `#BFBFBF`
- Helper text appears below in `12px` muted color
- Error messages replace helper text in red

---

## Cards

### Default Card
```css
background: #FFFFFF;
border: 1px solid rgba(18, 115, 105, 0.08);
border-radius: 16px;
padding: 24px;
```

### Elevated Card
```css
background: #FFFFFF;
border: none;
border-radius: 16px;
box-shadow: 0 4px 20px rgba(1, 69, 66, 0.08);
```

### Minimal Card
```css
background: #F5F7F7;
border: none;
border-radius: 16px;
padding: 24px;
```

### Card Hover States

- **Default:** Border transitions to accent, subtle shadow appears
- **Elevated:** Shadow deepens and expands
- **Minimal:** Background becomes white, shadow appears

---

## Shadows

| Level | Value | Usage |
|-------|-------|-------|
| **sm** | `0 2px 8px rgba(1, 69, 66, 0.04)` | Subtle elevation |
| **md** | `0 4px 20px rgba(1, 69, 66, 0.08)` | Cards, dropdowns |
| **lg** | `0 20px 40px rgba(1, 69, 66, 0.08)` | Modals, popovers |
| **xl** | `0 24px 48px rgba(1, 69, 66, 0.12)` | Feature highlights |

---

## Motion Design System

### Frame Rates

| Context | FPS | Usage |
|---------|-----|-------|
| **Web/UI** | 60 fps | UI animations, micro-interactions |
| **Video Standard** | 30 fps | Social media, general video |
| **Video Smooth** | 60 fps | Product demos, premium content |
| **Cinematic** | 24 fps | Storytelling, dramatic sequences |

### Standard Durations

| Duration | Frames @30fps | Usage |
|----------|---------------|-------|
| **Instant** | 100ms | 3 frames | Micro-feedback, button states |
| **Fast** | 200ms | 6 frames | Hover states, small transitions |
| **Normal** | 300ms | 9 frames | Standard UI transitions |
| **Moderate** | 500ms | 15 frames | Card reveals, panel slides |
| **Slow** | 800ms | 24 frames | Page transitions, large reveals |
| **Dramatic** | 1200ms | 36 frames | Hero animations, intros |

### Easing Curves

#### Standard Easings
```javascript
// Smooth deceleration — most common, natural feel
easeOut: [0.0, 0.0, 0.2, 1.0]

// Acceleration then deceleration — entering/exiting
easeInOut: [0.4, 0.0, 0.2, 1.0]

// Acceleration — elements leaving the screen
easeIn: [0.4, 0.0, 1.0, 1.0]

// Linear — constant speed, mechanical motion
linear: [0.0, 0.0, 1.0, 1.0]
```

#### Expressive Easings
```javascript
// Snappy — quick settle, modern UI feel
snappy: [0.2, 0.0, 0.0, 1.0]

// Bounce — playful overshoot
bounce: [0.68, -0.55, 0.265, 1.55]

// Elastic — spring-like settle
elastic: [0.5, 1.8, 0.5, 0.8]

// Smooth — gentle, premium feel
smooth: [0.25, 0.1, 0.25, 1.0]
```

#### Remotion Spring Presets
```javascript
// Default smooth spring
spring({ damping: 15, mass: 1, stiffness: 100 })

// Snappy response
spring({ damping: 20, mass: 0.5, stiffness: 200 })

// Gentle float
spring({ damping: 30, mass: 1.5, stiffness: 80 })

// Bouncy
spring({ damping: 10, mass: 1, stiffness: 150 })
```

### Animation Patterns

#### Fade In
```javascript
opacity: 0 → 1
duration: 300-500ms
easing: easeOut
```

#### Fade Up (Reveal)
```javascript
opacity: 0 → 1
translateY: 20px → 0
duration: 500ms
easing: easeOut
```

#### Scale In
```javascript
opacity: 0 → 1
scale: 0.95 → 1
duration: 400ms
easing: snappy
```

#### Slide In
```javascript
translateX: -100% → 0 (from left)
translateX: 100% → 0 (from right)
duration: 500ms
easing: easeOut
```

#### Stagger Reveal
```javascript
// Each item delays by offset
delay: index * 50ms
opacity: 0 → 1
translateY: 30px → 0
duration: 500ms
easing: easeOut
```

### Text Animation Patterns

#### Character Stagger
```javascript
// Per-character reveal
delay: charIndex * 30ms
opacity: 0 → 1
translateY: 20px → 0
```

#### Word Stagger
```javascript
// Per-word reveal
delay: wordIndex * 80ms
opacity: 0 → 1
translateY: 15px → 0
```

#### Line Reveal
```javascript
// Mask wipe per line
clipPath: inset(0 100% 0 0) → inset(0 0% 0 0)
duration: 600ms
easing: easeInOut
```

#### Typewriter
```javascript
// Character-by-character
delay: charIndex * 50ms
opacity: 0 → 1
```

### Transition Types

#### Cut
Instant switch between scenes. Use for:
- Fast-paced sequences
- Dramatic reveals
- Matching action cuts

#### Crossfade
```javascript
outgoing: opacity 1 → 0
incoming: opacity 0 → 1
overlap: 300-500ms
```
Use for: Smooth scene transitions, mood changes

#### Wipe
```javascript
clipPath: inset(0 0 0 0) → inset(0 0 0 100%)
duration: 500-800ms
easing: easeInOut
```
Use for: Directional transitions, reveals

#### Zoom
```javascript
outgoing: scale 1 → 1.1, opacity 1 → 0
incoming: scale 0.9 → 1, opacity 0 → 1
duration: 600ms
```
Use for: Focus shifts, dramatic emphasis

#### Morph
Elements transform smoothly between states. Use for:
- Logo animations
- Icon transitions
- Shape morphing

### Motion Principles

#### 1. Purpose Over Decoration
Every animation should serve a function—guide attention, show relationships, or provide feedback.

#### 2. Natural Physics
Motion should feel real. Objects accelerate and decelerate naturally. Use springs for organic feel.

#### 3. Hierarchy Through Timing
Important elements animate first or most prominently. Secondary elements follow with stagger.

#### 4. Consistent Rhythm
Use the defined duration scale. Similar actions should have similar timing.

#### 5. Spatial Continuity
Elements should enter from logical origins and exit toward logical destinations.

#### 6. Anticipation & Follow-Through
For expressive animations, add subtle wind-up before action and settle after.

---

## Motion Graphics Compositions

### Lower Third
```
Duration: 3-5 seconds
Enter: 500ms slide + fade from left
Hold: 2-4 seconds
Exit: 300ms fade out

Layout:
├── Background bar (Primary #127369, 80% opacity)
├── Name text (White, Title size)
└── Title text (Accent #8AA6A3, Body size)
```

### Title Card
```
Duration: 4-6 seconds
Enter: Stagger fade-up, 100ms between elements
Hold: 3-4 seconds
Exit: Simultaneous fade out

Layout:
├── Overline (Caption, Highlight #2AB686)
├── Main title (Hero size, Dark #014542)
└── Subtitle (Body Large, Neutral Dark #4C5958)
```

### Data Visualization
```
Enter: Draw-on effect for lines/shapes
       Count-up for numbers
       Stagger for multiple data points
Duration: 800-1200ms per element
Easing: easeOut

Colors:
├── Primary data: Primary #127369
├── Secondary data: Accent #8AA6A3
├── Highlight data: Highlight #2AB686
└── Background: Dark #014542 or White
```

### Logo Animation
```
Total duration: 2-3 seconds
Build-up: 1-1.5 seconds (elements assemble)
Settle: 500ms (final position with overshoot)
Hold: 500ms-1s

Techniques:
├── Path drawing (stroke-dashoffset)
├── Scale with bounce
├── Rotation with snap
└── Color fill wipe
```

### Outro/End Card
```
Duration: 5-8 seconds
Enter: 800ms scale-up from center
Hold: 4-6 seconds
Elements:
├── Logo (centered, scale animation)
├── CTA text (fade-up, 200ms delay)
├── URL/Social (fade-up, 400ms delay)
└── Background (gradient Dark → Primary)
```

---

## Gradient Definitions

### Primary Gradients
```css
/* Brand gradient */
linear-gradient(135deg, #127369 0%, #014542 100%)

/* Highlight gradient */
linear-gradient(135deg, #127369 0%, #2AB686 100%)

/* Subtle surface gradient */
linear-gradient(180deg, #FAFBFB 0%, #F5F7F7 100%)
```

### Motion Background Gradients
```css
/* Dark cinematic */
radial-gradient(ellipse at center, #014542 0%, #011f1e 100%)

/* Ambient glow */
radial-gradient(ellipse at 30% 50%, rgba(42, 182, 134, 0.15) 0%, transparent 50%),
radial-gradient(ellipse at 70% 50%, rgba(18, 115, 105, 0.1) 0%, transparent 50%),
#014542

/* Light premium */
linear-gradient(180deg, #FFFFFF 0%, #F5F7F7 50%, #E8EDEC 100%)
```

---

## CSS Variables

```css
:root {
  /* Colors */
  --hp-primary: #127369;
  --hp-dark: #014542;
  --hp-accent: #8AA6A3;
  --hp-neutral-dark: #4C5958;
  --hp-neutral-light: #BFBFBF;
  --hp-highlight: #2AB686;

  /* Surfaces */
  --hp-white: #FFFFFF;
  --hp-off-white: #FAFBFB;
  --hp-surface: #F5F7F7;
  --hp-border: rgba(18, 115, 105, 0.08);

  /* Typography */
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --space-9: 96px;
  --space-10: 128px;

  /* Radius */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;

  /* UI Transitions */
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

---

## Design Principles

### 1. Clarity Over Complexity
Every element should serve a purpose. Remove anything that doesn't contribute to the user's understanding or task completion.

### 2. Generous Whitespace
Let content breathe. Whitespace is not empty space—it's a design element that creates focus and hierarchy.

### 3. Subtle Motion
Animations should feel natural and purposeful. Use transitions to provide feedback, not decoration.

### 4. Consistent Rhythm
Apply spacing and timing systematically. Consistent use of scales creates visual and temporal harmony.

### 5. Accessible by Default
Maintain WCAG AA contrast ratios. All interactive elements should have clear focus states. Respect reduced-motion preferences.

---

*HydePoint Design System v1.0*
