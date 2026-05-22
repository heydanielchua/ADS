# Date Picker

A calendar panel for selecting a single date or a date range. Composed of a calendar grid, month/year dropdowns, navigation arrows, and date cells. Width 296px. Semantic tokens throughout — no new tokens needed.

## Calendar panel (296×308)
- Background: `semantic.surface.subtle` (grey.5)
- Two variants: **Calendar** (single date) and **Calendar - Range** (start/end + in-between range)

### Structure
1. **Dropdowns row** — month selector + year selector (Dropdown Cal components)
2. **Day-of-week headers** — Sun–Sat, 7 columns × 36px
3. **Date grid** — rows of Date Button cells
4. **Footer buttons** — Cancel (ghost/outlined) + action button (Primary, `semantic.accent.primary`)

---

## Date Button (day cell, 24×24, radius 2)
| State | Fill | Border | Text |
|-------|------|--------|------|
| Default | transparent | none | `semantic.text.subtle` |
| Hover | `semantic.surface.hover` (grey.15) | `semantic.border.strong` | `semantic.text.subtle` |
| On Click (selected) | `semantic.surface.pressed` (grey.20) | `semantic.border.strong` | `semantic.text.default` |
| Range - On Click (in-range) | `semantic.field.borderFilled` (grey.35) | `semantic.border.strong` | `semantic.text.default` |
| Low Opacity | transparent, dimmed | none | adjacent-month days |

Selected dates use the pressed-grey fill with a `border.strong` ring; range selection uses the slightly stronger `field.borderFilled` fill for in-between days.

---

## Navigation arrows (Button / Cal / Ghost - Icon, 18×18)
Previous/next month icon buttons.
| State | Background |
|-------|-----------|
| Default | transparent |
| Hover | `semantic.surface.hover` |
| On Click | `semantic.surface.pressed` |
| Disabled | transparent, 40% opacity |

---

## Month / Year dropdowns (Dropdown Cal, 78×28)
Compact dropdowns for jumping to a month or year.
- States: Default, Hover, Filled, Disabled (follow the Dropdown spec)
- On Click: expands to 78×216 — a scrollable option list
- Year variant: same, listing years

### Dropdown Cal Option (60×40)
| State | Background |
|-------|-----------|
| Default / Pre-selected | `semantic.surface.subtle` (grey.5) |
| Hover | `semantic.surface.hover` (grey.15) |
| On Click | `semantic.surface.pressed` (grey.20) |

---

## Rules
- The calendar reuses the standard surface scale (`surface.subtle → hover → pressed`) for cells and options — consistent with dropdown, table, and menu components.
- Selected date = `surface.pressed` fill + `border.strong` ring; range in-between = `field.borderFilled` fill.
- The footer action button uses `accent.primary` (the only accent colour in the picker).
- Adjacent-month days render at low opacity to de-emphasise them.
- Disabled = 40% opacity (system-wide). Semantic tokens only.
