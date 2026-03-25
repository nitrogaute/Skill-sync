# Claude Skills

Personal skills repository for Claude Code and VS Code Copilot, synced across machines.

## Structure

```
global/                        # Installed once per machine → ~/.claude/skills/ + ~/.copilot/skills/
├── universal/  (36 skills)    # Always installed (dev tools, docs, business)
├── work/       (1 skill)      # Work machines only (KM project management)
└── personal/   (3 skills)     # Personal machines only (daily brief, creative)

local/                         # Installed per project → <project>/.claude/skills/
├── km/         (6 skills)     # Kongsberg Maritime (design, domain, presentations)
├── hydepoint/  (4 skills)     # HydePoint (hydrogen, energy, EU GHG)
├── gtb/        (1 skill)      # GTB Ventures (VC presentation design)
└── other/      (0 skills)     # Misc skills for ad-hoc projects
```

## Install

Works on macOS, Linux, and Windows (Git Bash). On Windows, uses directory junctions instead of symlinks (no admin needed).

### Global (one-time per machine)

```bash
# Work machine (Windows or Mac):
./install.sh work        # universal + work → ~/.claude/skills/ + ~/.copilot/skills/

# Personal machine:
./install.sh personal    # universal + personal → ~/.claude/skills/ + ~/.copilot/skills/
```

### Local (skill sets into AI SKILLS folder)

```bash
./install.sh local km        # KM skills
./install.sh local hydepoint # HydePoint skills
```

This links skills into the OneDrive `AI SKILLS` folder (`~/OneDrive - KONGSBERG/Documents/AI SKILLS/<set>/`).

## Adding a skill

1. Create a directory under the right folder
2. Add a `SKILL.md` with YAML frontmatter
3. Run the appropriate install command
4. Commit and push

## Skill format

```yaml
---
name: my-skill
description: What it does and when to trigger it
---

Instructions for Claude...
```

See [Agent Skills docs](https://code.claude.com/docs/en/skills) for full reference.
