---
name: create-presentation
description: >
  Orchestrates a Claude Code Agent Teams workflow to create a professional slide deck 
  (.pptx) and speaker notes manuscript (.docx) from an interactive interview. Spawns 
  specialist agents (Interviewer, Narrative Architect, Slide Designer, Critic/QA) with 
  inter-agent communication via mailbox messaging. Includes three human-in-the-loop 
  checkpoints: narrative variant selection, ASCII layout selection, and optional image 
  review. Use this skill whenever the user asks to create a presentation, pitch deck, 
  slide deck, keynote, or any deliverable that requires both slides and speaker notes. 
  Also trigger when the user mentions "presentation workflow", "slide manuscript", 
  "deck with speaker notes", or references creating presentation material with an 
  agentic or multi-agent approach. Even if the user just says "make me a deck" or 
  "help me build a pitch", this skill applies.
---

# Create Presentation — Agent Teams Skill

## Prerequisites

- **Claude Code Agent Teams** must be enabled:
  ```
  CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
  ```
  Add to your environment or `.claude/settings.json`. If not enabled, inform the user and explain how to enable it before proceeding.

- **Design guide** (required): A design guide skill or template `.pptx` the user provides.

## Dependent Skills — Agents Must Load Before Use

| Skill | Who Loads It | Path | Purpose |
|-------|-------------|------|---------|
| docx creation | Narrative Architect | `/mnt/skills/public/docx/SKILL.md` | Building the manuscript .docx |
| pptx creation | Slide Designer | `/mnt/skills/public/pptx/SKILL.md` | Building the slide deck .pptx |
| Design guide | Slide Designer, Critic/QA | User-provided (required) | Visual design rules |
| Voice skill | Narrative Architect | User-provided (optional) | Speaker's tone and style |
| banana-paper | Lead | User-provided (optional) | Gemini Pro 3 image generation |

**Critical**: Each agent's spawn prompt MUST include explicit instructions to `cat` or read the relevant skill files listed above BEFORE starting any work. Do not assume skills are pre-loaded.

## Outputs

- `<slug>.pptx` — Slide deck following the design guide
- `<slug>-manuscript.docx` — Structured speaker notes per slide

---

## Time, Slide Count & Density Calibration

Use these benchmarks when planning presentations. Based on real delivered presentations.

### Time-to-Slide Ratios

| Format | Slides | Minutes | Min/Slide | Notes |
|--------|--------|---------|-----------|-------|
| Lightning talk | 3 | 5 | 1.7 | No Q&A, tight transitions |
| Short all-hands slot | 3 | 10 | 3.3 | Dense speaker notes, visual anchors only |
| Standard update | 8–12 | 20 | 1.5–2.5 | Room for pausing on data |
| Deep dive / workshop | 15–25 | 45 | 1.5–2 | Interactive, may pause longer |
| Keynote | 30–50 | 60 | 1–1.5 | Often image-heavy, fast pacing |

**Rule of thumb**: Plan 2–3 minutes per content slide. Title/agenda/Q&A slides take <1 minute each.

### Talking Point Density by Slide Type

| Slide Type | Talking Points | Sentences per Point | Total ~Words |
|------------|----------------|---------------------|--------------|
| Opening / WHAT | 4–6 | 2–3 | 150–250 |
| System / SO WHAT | 8–12 | 1–2 | 200–350 |
| CTA / NOW WHAT | 4–6 | 1–2 | 100–180 |
| Visual walkthrough | 6–10 | 1–2 | 150–250 |
| Data slide | 3–5 | 2–3 | 100–200 |

**The SO WHAT slide is typically the densest** — it carries explanation, lists, and spatial navigation. WHAT sets up context; NOW WHAT is action-focused and tighter.

### Compressed vs. Expanded Presentations

**Compressed (3–5 slides, 10 min)**:
- 1 slide per framework section
- Speaker notes carry 80% of the content
- Slides show only: title, one anchor phrase, and visual (if any)
- Transitions are brief verbal bridges

**Standard (8–12 slides, 20 min)**:
- 2–4 slides per framework section
- More content lives on the slide (bullets, data, diagrams)
- Speaker notes provide context and emphasis cues
- Transitions can be their own micro-moment

**Expanded (15+ slides, 30+ min)**:
- Consider section dividers between framework sections
- Add agenda slide upfront, summary slide at end
- May need a "midpoint recap" slide
- Budget time for audience questions mid-presentation

### Teleprompter Presentations

When the presenter will use a teleprompter, the manuscript format changes significantly:

**Format differences**:
- Phrase-per-line (not paragraph format)
- Max 50–60 characters per line
- Blank lines indicate pauses
- Bold for vocal emphasis
- [PAUSE] markers for dramatic beats

**Why this matters**:
- Traditional paragraphs are hard to track while maintaining eye contact with camera
- Short lines let the presenter glance and look up
- Consistent line length creates predictable reading rhythm

**Output**: When teleprompter is enabled, the Narrative Architect produces a teleprompter-formatted manuscript alongside (or instead of) the standard .docx.

### Structure Within a Slide's Speaker Notes

Each slide's speaker notes should follow this rhythm:

1. **Hook** (optional) — engagement prompt, rhetorical question, or "let me show you..."
2. **Body** — the talking points (4–10 depending on slide type)
3. **Synthesis** (optional) — a one-liner that ties the points together
4. **Transition** — a bridge phrase to the next slide

For visual-heavy slides, replace the body with spatial navigation:
- "It starts at the bottom..."
- "On the left side... On the right..."
- "The data flows upward..."

---

## Workflow Overview

```
Phase 0:  Scaffold       → Lead asks title, design guide, optional skills
Phase 1:  Interview      → Interviewer gathers context, builds brief.yaml
Phase 2:  Plan           → Lead creates task list, spawns agents
Phase 3a: Story Arc      → Narrative Architect creates arc + 3 narrative variants/slide
Phase 3b: Narrative Pick → User selects preferred variant per slide
Phase 3c: Manuscript     → Narrative Architect assembles final .docx from selections
Phase 3d: Layouts        → Slide Designer creates 3 ASCII layout variants/slide
Phase 3e: Layout Pick    → User selects preferred layout per slide
Phase 3f: Images         → Lead generates images via banana-paper (OPTIONAL)
Phase 3g: Image Review   → User approves/rejects images (OPTIONAL)
Phase 3h: Slides         → Slide Designer builds final .pptx
Phase 4:  Critique       → Critic/QA reviews manuscript + slides + consistency
Phase 5:  Deliver        → Lead assembles final output and delivers
```

---

## Phase 0: Scaffolding (Lead)

You are the Lead. Before spawning any agents:

1. Ask the user for a **working title** for the presentation.
2. Slugify the title (e.g., "HydePoint Investor Pitch" → `hydepoint-investor-pitch`).
3. Create the folder structure:
   ```
   presentations/<slug>/
   ├── brief.yaml
   ├── input/
   ├── drafts/
   │   ├── narrative-variants/
   │   ├── slide-layouts/
   │   ├── images/
   ├── review/
   └── output/
   ```
4. Ask the user for:
   - **Design guide path** (required) — path to a design guide skill or template `.pptx`
   - **Voice skill path** (optional) — for manuscript tone
   - **Image generation skill path** (optional) — banana-paper skill for Gemini Pro 3 image gen
5. Spawn the **Interviewer** agent using the prompt in `./prompts/interviewer.md`.

---

## Phase 1: Interview

The Interviewer conducts a structured interview to produce `brief.yaml`. Read `./prompts/interviewer.md` for the full spawn prompt. The Interviewer:

- Asks about purpose, audience, key message, length, content, constraints
- Reads ALL files in `./frameworks/` and proposes 2–3 storytelling frameworks with rationale
- Lets the user approve a framework or suggest an alternative
- Presents a Brief Summary for user approval
- Writes the approved brief to `presentations/<slug>/brief.yaml`

The brief schema template is in `./templates/brief-schema.yaml`.

---

## Phase 2: Planning (Lead)

Once the user approves the Brief:

1. Create the shared task list (see Task List below).
2. Spawn three agents using prompts from `./prompts/`:
   - **Narrative Architect** (`./prompts/narrative-architect.md`)
   - **Slide Designer** (`./prompts/slide-designer.md`)
   - **Critic/QA** (`./prompts/critic-qa.md`)
3. Pass each agent: the path to `brief.yaml`, their role prompt, and explicit skill-loading instructions.

### Task List

```
Task 1:  [Narrative]  Create story arc outline                 (depends: Brief)
Task 2:  [Narrative]  Generate 3 narrative variants per slide   (depends: Task 1)
Task 3:  [Lead]       Present narrative variants to user        (depends: Task 2)
Task 4:  [Lead]       Write narrative-selections.yaml           (depends: Task 3)
Task 5:  [Narrative]  Assemble final manuscript .docx           (depends: Task 4)
Task 6:  [Slides]     Generate 3 ASCII layout variants/slide    (depends: Task 1 + Task 4)
Task 7:  [Lead]       Present layout variants to user           (depends: Task 6)
Task 8:  [Lead]       Write layout-selections.yaml              (depends: Task 7)
Task 9:  [Lead]       Generate images via banana-paper           (depends: Task 8, OPTIONAL)
Task 10: [Lead]       Present images to user for review          (depends: Task 9, OPTIONAL)
Task 11: [Slides]     Build final .pptx deck                    (depends: Task 8 + Task 10)
Task 12: [Critic]     Review manuscript against Brief           (depends: Task 5)
Task 13: [Critic]     Review slides against Brief + design      (depends: Task 11)
Task 14: [Critic]     Consistency check slides↔manuscript       (depends: Task 12 + Task 13)
Task 15: [Narrative]  Apply revision feedback                   (depends: Task 12, conditional)
Task 16: [Slides]     Apply revision feedback                   (depends: Task 13, conditional)
Task 17: [Lead]       Final assembly + delivery                 (depends: Task 14 passed)
```

Tasks 5 and 6 can run in parallel. Tasks 9–10 are skipped if banana-paper is not provided.

---

## Phase 3a–3b: Narrative Variants + Selection

The Narrative Architect generates 3 variant `.md` files per slide in `drafts/narrative-variants/slide-NN/`. Each variant differs in both **angle** (emphasis, framing, hook) and **tone** (authoritative, conversational, urgent, etc.).

### Variant file format

```
drafts/narrative-variants/slide-NN/variant-X.md
```

Each file contains:
- Slide number + title
- **Angle** label (1-liner)
- **Tone** label (1-liner)
- 3–8 bullet talking points
- Transition cue to next slide

When variants are ready, notify the user:

> "Narrative variants are ready for review. Open `drafts/narrative-variants/slide-NN/` to compare variants A, B, C for each slide. For each slide, tell me your pick — you can also combine elements ('A's opening + C's data framing') or ask for a re-do."

Write user selections to `drafts/narrative-selections.yaml`:

```yaml
slides:
  - slide: 1
    pick: "variant-b"
    notes: null
  - slide: 2
    pick: "variant-a"
    notes: "Use the opening from variant-c"
```

If user rejects all 3 for a slide, ask Narrative Architect for a targeted re-generation with user feedback.

---

## Phase 3c: Manuscript Assembly

Narrative Architect reads `narrative-selections.yaml`, applies user notes, and assembles `drafts/manuscript-v1.docx`. **Must read `/mnt/skills/public/docx/SKILL.md` first.**

Format: one section per slide with heading, 3–8 talking points, transition cues.

---

## Phase 3d–3e: Layout Variants + Selection

The Slide Designer generates 3 ASCII layout variants per slide in `drafts/slide-layouts/slide-NN/`. Each layout proposes different visual composition using box-drawing characters.

### Layout file format

```
drafts/slide-layouts/slide-NN/layout-X.md
```

Each file contains:
- Slide number + title
- **Layout type** label
- **Rationale** (why this layout fits the content)
- ASCII wireframe using `┌ ─ ┐ │ └ ┘` and `█` for image placeholders
- Element list with design notes

### ASCII art quality standards

- Show element placement (titles, text blocks, images, charts, logos)
- Show relative sizing (hero image vs. small icon should be visibly different)
- Show information hierarchy (primary, secondary, tertiary)
- Include element labels where wireframe alone isn't clear
- Do NOT render fonts or colors — focus on composition

When layouts are ready, present to user same as narrative selection. Write picks to `drafts/layout-selections.yaml`.

---

## Phase 3f–3g: Image Generation (OPTIONAL)

**Skip if no banana-paper skill was provided in Phase 0.**

1. Read approved layouts from `layout-selections.yaml` and manuscript.
2. Identify every image placeholder from the ASCII wireframes.
3. Generate a descriptive prompt for each image, informed by:
   - Slide narrative content
   - Layout element description
   - Design guide visual style
   - Brief audience and tone
4. Load the **banana-paper** skill and invoke Gemini Pro 3 for each image.
5. Save images to `drafts/images/` with descriptive filenames.
6. Write `drafts/image-prompts.yaml` tracking prompts, paths, and approval status.
7. Present images to user for review: approve, reject + re-prompt, or skip.
8. Max 2 re-generation rounds per image. If still rejected, skip that image.

---

## Phase 3h: Final Slide Assembly

Slide Designer reads `layout-selections.yaml` + approved images (if any) + manuscript. **Must read `/mnt/skills/public/pptx/SKILL.md` first.** Builds `drafts/slides-v1.pptx`:

- User-selected layout per slide
- Design guide strictly (colors, fonts, spacing, logo)
- Approved images embedded in designated positions
- Minimal text — visuals and key phrases only
- PowerPoint speaker notes: "See manuscript slide N"

---

## Phase 4: Critique & Revision

Critic/QA performs three review passes. Read `./prompts/critic-qa.md` for full details.

**Pass 1 — Manuscript**: Framework adherence, audience fit, key message, tone, content coverage, transitions.
**Pass 2 — Slides**: Design guide compliance, layout fidelity to selections, image integration (if applicable), text density, mandatory slides.
**Pass 3 — Consistency**: Every slide has notes, titles match, flow matches, no content mismatches.

Feedback written to `review/critique-round-N.md`. Specific items sent via mailbox. Max 2 revision rounds, then escalate to user.

---

## Phase 5: Delivery

Copy final files to `presentations/<slug>/output/`:
- `<slug>.pptx`
- `<slug>-manuscript.docx`

Present to user with summary: slide count, time estimate, framework used, any open Critic notes.

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Agent Teams not enabled | Inform user how to enable, stop |
| Design guide path invalid | Ask user for correct path |
| Voice skill path invalid | Warn, continue without |
| banana-paper path invalid | Warn, continue without images |
| banana-paper API key missing | Report error, offer to proceed without images |
| Gemini API failure | Retry once, skip image on second failure |
| Image rejected after 2 rounds | Skip, note in final summary |
| Critic >5 issues per pass | Top 3 mandatory, rest suggestions |
| Revision round 2 fails | Escalate to user with full report |
| Contradictory Brief | Interviewer flags before finalizing |
| Teammate idle | Use TeammateIdle hook to re-engage |
| >30 slides | Split: arc in chunks, slides in batches of 10 |

---

## Storytelling Frameworks

Available in `./frameworks/`. The Interviewer reads all of them and proposes 2–3 based on context.

| Framework | File | Best For |
|-----------|------|----------|
| Situation → Complication → Resolution | `situation-complication-resolution.md` | Executive, business cases |
| Problem → Solution → Benefit | `problem-solution-benefit.md` | Product pitches, proposals |
| Burning Platform | `burning-platform.md` | Change management, urgency |
| Hero's Journey | `heros-journey.md` | Keynotes, customer stories |
| What → So What → Now What | `what-so-what-now-what.md` | Data updates, status reports |
| STAR | `star.md` | Case studies, retrospectives |
