# Advanced Filter Dialog

A floating panel dialog for filtering and column management. Comes in three responsive-width sizes and two variants: **Advanced Filters** (dropdown-based filter criteria) and **Hide Columns** (checkbox column visibility). Uses a lightly brand-tinted panel surface.

## Panel (shared anatomy)
- Background: `semantic.surface.panel` (`accent.30` light / `accent.80` dark)
- Border: 1px `semantic.field.borderFilled` (grey.35)
- Radius: `radius.8`
- Padding: `spacing.16`
- No drop shadow (separation comes from border + bg tint)
- Close button (×): absolute top-right corner, `icon.size.xs` (24px)

## Sizes
| Size | Width | Min width | Height |
|------|-------|-----------|--------|
| S | 282px | — | responsive |
| M | 472px | 282px | responsive |
| L | 700px | 282px | responsive |

## Advanced Filters variant
For filtering table/list data via dropdown criteria.

**Header**
- Title "Filters" — `font-m` bold (16 / 22), `semantic.accent.primary`

**Filter rows** (stack vertically, gap `spacing.4`)
Each row = label + dropdown trigger + optional error:
- Label: `font-xs` semibold (12 / 17), `semantic.text.subtle`
- Dropdown trigger: `semantic.field.bg`, height 40px, padding `spacing.16`, placeholder `semantic.field.placeholder`, chevron icon. Follows the Dropdown component spec.
- Error text (hidden by default): `semantic.feedback.error`, shown on validation failure

**Footer buttons** (full-width row, space-between)
- **Clear All** — Ghost button (left)
- **Apply** — Primary button (right), `semantic.accent.primary`; starts at 40% opacity (disabled) until at least one filter is set

## Hide Columns variant
For toggling table column visibility.

**Header**
- Title "Hide Columns" — `font-m` bold, `semantic.accent.primary`

**Column list** (gap `spacing.4`)
Each row = checkbox (16px) + label (16px, `semantic.text.default`), gap `spacing.8`

**Footer buttons**
- **Reset** — Ghost button
- **Hide All** — Outlined button (`semantic.border.strong`)
- **Apply** — Primary button (`semantic.accent.primary`)

## Rules
- `surface.panel` (`accent.30`) provides a subtle brand tint that distinguishes the dialog from the page bg without a heavy overlay.
- The Apply button renders at 40% opacity until actionable — consistent with the system-wide disabled convention.
- Dialog dropdowns follow the Dropdown component spec (`dropdown.md`).
- Semantic tokens only; no raw hex.
