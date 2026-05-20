# Design System - AI Rules

This file tells Claude (and other AI tools) how to use this design system. Read it before generating any UI, component, or design.

## Source of truth
- **Primitive tokens** live in `/tokens/colors.json` (the raw palette), plus `typography.json`, `spacing.json`, `shadow.json`, `icon.json`. These are mode-agnostic.
- **Semantic tokens** live in `/tokens/semantic-light.json` and `/tokens/semantic-dark.json` - the same token names resolving to different primitives per theme.
- **Component specs** live in `/components/*.md`.
- The visual master file is maintained in **Lunacy**. This repo mirrors it.

## Light & dark mode
This system supports two themes. The rule:
- **Primitives never change** between modes (`blue.80` is `#0066FF` in both).
- **Semantic tokens change** by mode. Components reference ONLY semantic tokens (e.g. `semantic.bg.default`, `semantic.text.default`), so they reflow automatically when the theme flips.
- Dark mode is derived from light by **symmetry** (mirror the tonal ladder):
  - `white <-> black`
  - greys: `dark = grey(105 - lightStep)` (so `grey.5 <-> grey.100`, `grey.50 <-> grey.55`)
  - chromatic colors mirror at the 60/50 axis: dark = `step(110 - light)`, so `blue.80 <-> blue.30`, `red.60 <-> red.50`, etc. (see `tokens/THEMES.md`)
- In CSS: map `semantic-light` to `:root` and `semantic-dark` to `[data-theme="dark"]` as CSS custom properties.
- **Accent is the brand ramp and is the unique case:** it shifts hue across the axis (`accent.60` blue in light -> `accent.50` cyan in dark). `semantic.brand.primary` uses the accent ramp. All other families are single-hue and just lighten.

## Hard rules when generating code or designs
1. **Reference semantic tokens, not primitives,** for color in components (so theming works). Use primitives only when defining semantic tokens.
2. **Never invent values.** Every color, size, spacing, radius must trace to a token. No raw hex or random px.
3. If a needed token does not exist, **stop and ask** rather than inventing one.
4. Follow the component specs in `/components` exactly - variants, sizes, states.
5. Default font family is `font.family.sans` (Open Sans). Disabled states use 40% opacity across the system.

## When asked to add or change the system
- Add the primitive and/or semantic token here first, then build with it.
- New semantic tokens must be defined in BOTH `semantic-light` and `semantic-dark` (use the symmetry rule for the dark value).
- Keep naming consistent (category -> role -> scale).

## Out of scope
- Do not change brand colors or the core type scale without explicit instruction.
