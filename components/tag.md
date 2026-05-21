# Tag / Label

Compact non-interactive chips for status, categories, and workspace classification. Two types: **Status** (solid accent) and **Label** (tinted, any palette color). Semantic tokens for the Status tag; primitive palette tokens for Label tags since the color is contextual.

## Shared anatomy
- Height: 21px. Padding: `spacing.8` (x) / 2px (y). Text: `font-xs` (12 / 17).
- Radius differs by type (see below).

## Status tag
For status indicators — "Open", "Active", "In Progress".
- Background: `semantic.accent.primary`
- Text: `semantic.accent.onAccent`
- Radius: `radius.8`
- No border.

## Label / Workspace tag
For categories, classifications, and workspace labels. The fill color is contextual — any chromatic family in the palette using a consistent tint pattern.
- Background: `color.{family}.10` (e.g. `color.yellow.10` = #FEF8D2)
- Border: 1px `color.{family}.50` (e.g. `color.yellow.50` = #FEE75A)
- Text: `semantic.text.default` (grey.100)
- Radius: `radius.4`

The step 10 / 50 pairing works across all 15 chromatic families. Use the same family for bg and border.

> Accessibility note (from the kit): change text to `semantic.text.default` (grey.100) when needed for visual accessibility. For saturated or dark bg tags, switch to `semantic.text.inverted` (grey.5).

## Dark mode
Label tags follow the symmetry rule automatically:
- Background: `color.{family}.10` → `color.{family}.90` in dark (dark tint)
- Border: `color.{family}.50` → `color.{family}.60` in dark

The Status tag re-themes via `accent.primary` (blue → cyan in dark).

## Rules
- Use Status tags for binary/enumerated status values.
- Use Label tags for multi-value categorisation (workspaces, types, priorities).
- Never hard-code hex values; reference palette tokens by step.
- Always meet accessibility contrast with `text.default` (or `text.inverted` for dark fills).
