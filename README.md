# C3 System (ORMR UX 2.0) — extracted specs

These specs were extracted from the **ORMR UX 2.0 Master** and rewritten to reference your existing design system's **semantic tokens only** — no raw hexes, no PDF-specific `$tokens`, no new tokens. Dark mode comes for free via your light→dark symmetry rule.

## How this slots into your repo
```
foundations/        NEW — system structure & rules
  system-layout.md      spatial depth (z-planes) + pane dimensions
  module-layout.md      card pattern, view modes, side-bar states
  spacing-and-padding.md  4px spacing & padding usage

tokens/
  typography.json     NEW/REPLACES — the UX 2.0 type scale (heading-01..06, body, caption)

components/
  top-bar.md          REPLACES/EXTENDS existing
  tooltip.md          RECONCILES with existing (adds Primary/Secondary)
  button.md           EXTENDS existing (adds Alert variant + size scale) — merge, don't duplicate
  clock-pane.md       NEW
  floating-buttons.md NEW
  descriptive-buttons.md NEW
  snackbar.md         NEW
  progress-stepper.md NEW
  search-bar.md       NEW
  action-bar.md       NEW
  card.md             NEW
  widget.md           NEW
  dialogue.md         NEW
```

## Token mapping applied (PDF → your tokens)
- Text: `$text-default`→`text.default` · `$text-weak`→`text.muted` · `$text-invert`/`$text-snack`→`text.inverted`
- Icons: `$icon-default`→`text.muted` · `$icon-strong`→`text.default` · `$icon-weak`→`text.inverted` · `$icon-hover`/`$icon-onclick`→`accent.hover`
- Brand: `#0066FF`→`accent.primary` · `$system`/`$highlight`→`accent.primary`/`accent.subtle`
- Floating button: rest/hover `#ECECEC`→`surface.hover` · onclick `#D1D1D1`→`surface.pressed` · active `#1C1C1C`→`surface.contrast`
- Surfaces: `$background-secondary`→`surface.subtle` · `$background-snack` `#1C1C1C`→`surface.contrast`
- Borders: `$border` `#DEDEDE`→`border.default` · active border→`border.focus`
- Feedback: `$critical` `#FF5E5D`→`feedback.error` · `$warning` `#FFF02A`→`feedback.warning` (amber) · `$success`→`feedback.success`
- Scrim: `#15233B @60%`→`color.black` @ 60% (mode-invariant)
- Type: `$header-5/6`→`heading-05/06` · `$body-short-1/2`→`body-short-01/02`
- Layout: Top Bar 84→`topbar-h` · Side Bar 72→`sidebar-w` · Module Pane 504→`pane-compact`
- Depth: Z 0/+1/+2/+3 → `z-base`/`z-overlays`/`z-module`/`z-system` (0/10/20/30)
- Spacing/padding 4/8/12/16/24/32 → `spacing.*`; radius 8/10 → `radius.8`/`radius.10`

## Open items to confirm before final
1. **Max pinned modules** — deck says both "up to 10" and "up to five". Pick one (see `top-bar.md`).
2. **Scrim tint** — currently neutral `color.black` @ 60%. If you want the original navy kept, switch to `color.blue.100` @ 60%.
3. Source page p108 (full-screen dialogue) is annotated as pending scaling rules in the original — revisit when those exist.

## Using with Claude design
Drop these into the repo, then point Claude / Claude Code at it. Your `CLAUDE.md` rule still holds: **reference semantic tokens, never invent values; if a token is missing, stop and ask.** Every value in these specs already obeys that.
