# My Design System

The single source of truth for our product's look and feel. Designed in **Lunacy**, mirrored here as structured tokens and specs so it can drive code and AI-assisted design.

## What's in here
```
tokens/        Design tokens (colors, typography, spacing) in W3C JSON format
components/     Written specs for each component (anatomy, variants, states)
CLAUDE.md       Rules that tell AI tools how to use this system
```

## How to use it
- **Designers:** keep the Lunacy file as the visual master; reflect changes into `tokens/`.
- **Developers / AI:** read `CLAUDE.md`, then build using tokens only — never hard-coded values.

## Workflow
Lunacy (visual) → tokens + specs (this repo) → code & AI-generated UI that matches.
