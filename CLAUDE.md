# Design System — AI Rules

This file tells Claude (and other AI tools) how to use this design system. Read it before generating any UI, component, or design.

## Source of truth
- **Tokens** live in `/tokens/*.json` (W3C Design Token format).
- **Component specs** live in `/components/*.md`.
- The visual master file is maintained in **Lunacy**. This repo is the machine-readable mirror of it. If they ever disagree, the Lunacy file wins for visuals — but update this repo to match.

## Hard rules when generating code or designs
1. **Never invent values.** Every color, font size, spacing, and radius must reference a token from `/tokens`. No raw hex codes, no random pixel values.
2. If a needed token does not exist, **stop and ask** rather than inventing one.
3. Follow the component specs in `/components` exactly — variants, sizes, and states as listed.
4. Default font family is `font.family.sans`. Default text color is `color.text.default`.
5. Prefer existing components over building new ones from scratch.

## How to apply tokens in code
- For CSS/HTML: expose tokens as CSS custom properties, e.g. `--color-brand-primary`.
- For React/Tailwind: map tokens into the theme config; use semantic names, not hex.
- Token references like `{color.neutral.900}` mean "use the value of that other token."

## When asked to add or change the system
- Add the token/component here first, then build with it.
- Keep naming consistent with the existing structure (category → role → scale).

## Out of scope
- Do not change brand colors or core type scale without explicit instruction.
