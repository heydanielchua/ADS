# Tooltip

Contextual floating labels shown on hover. Four tooltip types plus a **Legend** panel variant. All use `radius.8`, padding `spacing.8`, and appear above the page layer. Semantic tokens throughout.

## Types

### System
For system interactions — "Double-click to...", "Edit", "Delete".
- Background: `semantic.accent.primary` (brand blue → cyan in dark)
- Text: `semantic.accent.onAccent` · `font-s` (14 / 20)

### Module
For module information — displaying entity/unit details on hover.
- Background: `semantic.surface.contrast` (always-dark floating surface: grey.100 light / grey.5 dark)
- Text: `semantic.text.inverted` · `font-s` (14 / 20)

### Error
For error guidance — typically appears on hover of the "i" icon in input fields; content should be instructional.
- Background: `semantic.surface.hover` (grey.15 — intentionally light to read as a non-blocking hint)
- Text: `semantic.feedback.error` (red.60) · `font-s` (14 / 20)

### Rich / Information
A two-column contextual panel for richer entity data (e.g. unit name, type, size).
- Background: `semantic.surface.contrast`
- Layout: labels column (left) + values column (right); padding `spacing.8`, gap `spacing.8`
- Labels: `font-s-600` (14px semibold), `semantic.text.inverted` (kit uses grey.15, close to off-white)
- Values: `font-s-400` (14px regular), `semantic.text.inverted`
- Height grows with content; no fixed height.

## Summary table
| Type | Background | Text | Use for |
|------|------------|------|---------|
| System | `accent.primary` | `accent.onAccent` | System actions |
| Module | `surface.contrast` | `text.inverted` | Entity / module info |
| Error | `surface.hover` | `feedback.error` | Input error hints |
| Rich | `surface.contrast` | `text.inverted` | Detailed entity data |

## Legend panel
A floating bordered panel for map or data legends. Distinct from tooltips — it persists rather than appearing on hover.
- Background: `semantic.surface.subtle`
- Border: 1.5px `semantic.field.borderFilled` (grey.35)
- Shadow: `shadow.elevated` (0px 4px 4px rgba(0,0,0,0.24); stronger than `shadow.default`)
- Title: `font-xs` semibold, `semantic.text.default`
- Body text: `font-xs` regular, `semantic.text.default`
- Color swatches: 14px ovals, filled with the relevant data color

## Rules
- All tooltips use `radius.8` and `spacing.8` padding.
- `surface.contrast` ensures the Module / Rich tooltip reads against both light and dark page backgrounds.
- Tooltip text is always `font-s`; the Legend uses `font-xs`.
- Never hard-code hex values. Reference semantic tokens only.
