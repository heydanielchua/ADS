# Callout & Tips

Three education/onboarding patterns grouped together: **Callout** (a feature-tour popup), **Active Learning Cue** (a numbered tip card), and **Informative Cue** (an inline feedback banner). All use primitive purple or feedback tokens — these are purpose-built UI for learning flows, not general-purpose components.

---

## Callout
A floating popover with a directional arrow, used for guided feature tours.

**Arrow**: triangle pointing toward the target element. Fill matches the content panel.

**Content panel**: radius `radius.8`, padding `spacing.16`, vertical layout, gap 24px.
| Part | Token | Style |
|------|-------|-------|
| Background + arrow | `color.purple.80` (#620AA5) | primitive |
| Heading | `semantic.text.inverted` (grey.5) | `font-m-600` (16/22) |
| Body text | `semantic.text.inverted` (grey.5) | `font-m-400` (16/22) |
| Pagination "1 of 3" | `semantic.text.inverted` (grey.5) | `font-s-400` (14/20) |
| Skip button | Ghost, `semantic.text.inverted` | text only |
| Next button | Outlined, white border + text | 1px `#FFFFFF` border |

Dark mode: `purple.80` → `color.purple.30` (110 − 80 = 30) by symmetry — a light lavender panel.

---

## Active Learning Cue
A numbered tip card for interactive learning steps.

**Card**: radius `radius.8`, padding `spacing.16`, vertical layout, gap `spacing.16`.
| Part | Token | Style |
|------|-------|-------|
| Card background | `color.purple.10` (#F9ECFE) | primitive |
| Icon (32px) | `color.purple.50` (#AB47F4) | primitive |
| Header text | `color.purple.50` | `font-size 22 / lh 32`, bold, max 2 lines |
| Number badge | 24×24 circle, `color.purple.50` fill, `semantic.text.inverted` number | `font-s-400` |
| Tip title | `semantic.text.default` | `font-m-600` (16/22) |
| Tip body | `semantic.text.subtle` | `font-m-400` (16/22) |

Each tip row = numbered badge + tip title / tip body (vertical, gap 4px).

Dark mode: `purple.10` → `purple.90`; `purple.50` → `purple.60` by symmetry.

---

## Informative Cue
Inline feedback banner. Transparent background, 2px coloured inside border, left-aligned icon + body text.

**Layout**: horizontal, gap `spacing.8`, vertically centred, padding `spacing.16`, radius `radius.8`.
| Type | Border | Icon |
|------|--------|------|
| Success | 2px `semantic.feedback.success` (green.60) | success icon |
| Warning | 2px `color.yellow.60` (#FFE233) | warning icon |
| Error | 2px `semantic.feedback.error` (red.60) | error icon |

- **Body text**: `font-m-400` (16/22), `semantic.text.default`. Max 2–3 lines.
- **Icon**: 24px, vertically centred.

> Note: the Warning cue uses `yellow.60` (bright canary yellow), not `feedback.warning` (amber.60). This is intentional — Informative Cue warnings are low-urgency notices; amber is reserved for higher-urgency toast / field warnings.

---

## Rules
- Callout and Active Learning Cue use `purple.*` primitives — not wired into the semantic layer, as these are education-specific UI.
- Informative Cues use semantic feedback tokens (except Warning — see note above).
- All copy max 2–3 lines. Semantic tokens where available, primitives otherwise.
