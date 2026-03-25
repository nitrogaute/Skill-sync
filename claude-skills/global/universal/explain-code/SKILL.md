---
name: explain-code
description: Explain how code works with diagrams and clear walkthrough. Use when asked "how does this work", "explain this", or when onboarding to a codebase.
---

# Explain Code

When explaining code, follow this structure:

## 1. One-liner
Start with a single sentence: what does this code do, in plain language.

## 2. Architecture diagram
Draw an ASCII diagram showing the flow, structure, or relationships.

## 3. Step-by-step walkthrough
Walk through the code in execution order. For each key step:
- What happens
- Why it matters
- What would break if removed

## 4. Key design decisions
Note any non-obvious choices: why this pattern, tradeoffs made, alternatives considered.

## 5. Gotchas
Common mistakes or edge cases someone maintaining this code should know about.

## Rules
- Match explanation depth to complexity. Simple function = short answer.
- Use concrete examples with actual values flowing through the code.
- Reference specific file:line when discussing code.
- If the code is bad, say so. Don't pretend clever hacks are good design.
