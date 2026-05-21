# Theme Symmetry

Dark mode is derived from light by mirroring each token across the central axis of the palette (see the Light/Dark diagram in Lunacy). Primitives never change; only which primitive a **semantic** token points to changes by mode.

## Rule
- **Neutrals** (axis between Grey 55 / Grey 50): dark = grey(105 - light), and white <-> black.
  - e.g. grey.100 <-> grey.5, grey.85 <-> grey.20, grey.55 <-> grey.50.
- **Chromatic** (axis between step 60 / 50): dark = step(110 - light).
  - e.g. 60 <-> 50, 70 <-> 40, 80 <-> 30, 90 <-> 20, 100 <-> 10. (05 is an edge tint with no exact mirror; clamp to nearest.)

## Chromatic step pairs
Applies to every chromatic family: accent, amber, blue, cyan, green, lime, pink, punch, purple, red, sky, teal, turquoise, violet, yellow.

| Light | Dark |
|-------|------|
| 100 | 10 |
| 90 | 20 |
| 80 | 30 |
| 70 | 40 |
| 60 | 50 |

## Neutral pairs
| Light | Dark |
|-------|------|
| White | Black |
| grey.100 | grey.5 |
| grey.95 | grey.10 |
| grey.90 | grey.15 |
| grey.85 | grey.20 |
| grey.80 | grey.25 |
| grey.75 | grey.30 |
| grey.70 | grey.35 |
| grey.65 | grey.40 |
| grey.60 | grey.45 |
| grey.55 | grey.50 |

## Accent ramp - the unique case
Every chromatic family except **accent** is a single-hue tint ramp, so the 60->50 swap just lightens it (same hue). The **accent ramp is the brand ramp and shifts hue across the axis**:
| Step | Hex | |
|------|-----|--|
| accent.60 | #0066FF | brand blue (light) |
| accent.50 | #00DCFF | brand cyan (dark) |

So applying the standard 60->50 rule to accent makes the brand color **blue in light mode, cyan in dark mode** - intended, not a bug. `semantic.accent.primary` therefore points at the accent ramp (not the blue tint ramp). Feedback and other roles use their normal `.60 -> .50` family steps.
