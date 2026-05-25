# Clock Pane (Date & Time)

The Clock Pane lets users view and manage multiple time formats. It opens/closes by clicking the clock section in the Top Bar's System Status Centre.

Plane `z-system` (30). All values reference tokens.

## Dimensions
- Width: 384px [Fixed]
- Height: 341px [Min] → 900px [Max]
- Vertical padding: `spacing.16`
- Horizontal padding: `spacing.12`

## Anatomy
A stacked list of time blocks:
1. **Real Time** (e.g. GMT+8) — date + time
2. **Exercise Time** (e.g. GMT+8) — date + time
3. **L-Time / H-Time** — exercise reference times (e.g. L+12 / L+13)
4. **Time Conversion** — conversion utility

A "Set Date & Time" affordance sits at the top-right.

## States

| State | Treatment |
|-------|-----------|
| Default | All blocks populated (Real, Exercise, L-Time, H-Time). |
| No H-Time | H-Time shows an em dash (—); layout otherwise unchanged. |

## Rules
- Labels use `caption-01`; values use `body-short-01`.
- Surface `surface.contrast` so the pane reads against any map background.
- Disabled = 40% opacity. Semantic tokens only.
