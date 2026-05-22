# Loader

Two loading patterns: a **Spinner** (circular dot animation) and a **Loader Bar** (linear progress with title and cancel). Primitive blue-family tokens throughout; no new semantic tokens needed.

---

## Loader Spinner

An 80×80 circular arrangement of 12 dots (each 8×8px oval), designed to animate by rotating clockwise. The colour sequence creates a spinning arc: dark navy builds to the bright head, then trails off to near-invisible grey, then back to dark.

### Dot colour sequence (clockwise from 12 o'clock)
| Position | Colour token | Notes |
|----------|-------------|-------|
| 10 o'clock | `color.blue.100` (#114599) | dark navy — "incoming" |
| 11 o'clock | `color.blue.90` (#1D5BBF) | building to head |
| **12 o'clock** | `color.blue.80` = `semantic.accent.primary` (#0066FF) | **head** — brightest |
| 1 o'clock | `color.blue.70` (#0078FF) | |
| 2 o'clock | `color.blue.60` (#1C86FF) | |
| 3 o'clock | `color.blue.50` (#2D8EFC) | |
| 4 o'clock | `color.blue.40` (#3998FF) | |
| 5 o'clock | `color.blue.30` (#6EB5F6) | trail lightens |
| 6 o'clock | `color.blue.10` (#C5DEFB) | nearly invisible |
| 7 o'clock | `color.blue.10` (#C5DEFB) | |
| 8 o'clock | `color.grey.35` (#B0B0B0) | grey fade — gap |
| 9 o'clock | `color.grey.15` (#E2E2E2) | almost invisible |

The grey.15 at 9 o'clock creates the visual gap that makes the arc read as "spinning" rather than a static ring. In dark mode, apply the symmetry rule to each primitive step (blue ramp mirrors via 110−step; grey mirrors via 105−step).

---

## Loader Bar

A horizontal progress indicator with a title, 2px track, and a Cancel action. Width 345px (flexible).

### Anatomy
- **Title** — e.g. "Loading (item)". `font-m` bold (16/22), `color.accent.80` (#1C1C1C near-black, ≈ `semantic.text.default`).
- **Track** — 2px (4px stroke) full-width path. Colour: `color.grey.25` (`semantic.control.segmentedTrack`).
- **Indicator** — 2px filled path overlaid on the track, showing progress. Colour: `color.blue.50` (#2D8EFC — a mid-blue, lighter than accent.primary).
- **"Please wait..." subtext** — `font-s-400` (14/20), `semantic.text.subtle` (grey.65).
- **Cancel button** — Outlined, `semantic.border.strong`, right-aligned below the bar. 80×32px.

### Layout
Vertical auto-layout, gap `spacing.16` between title and bar section, gap `spacing.8` between bar and subtext. Cancel button right-aligned below.

---

## Rules
- The Spinner uses the **blue tint ramp** (blue.10–blue.100) + `accent.primary` as the head dot. Never hard-code hex values — reference the primitive ramp steps and let the symmetry rule handle dark mode.
- The Loader Bar indicator (`blue.50`) is deliberately lighter than `accent.primary` — a design choice, not an error.
- The bar track reuses `control.segmentedTrack` (grey.25), maintaining consistency with the segmented control.
- Cancel is always Outlined (`border.strong`) — it's a secondary, non-destructive action.
