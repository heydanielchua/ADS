# Context Menu (Overflow Menu)

An overflow menu: a **trigger** (the ⋮ icon button) that opens a menu of **Context Option** rows. Width is responsive; rows are 40px tall. Semantic tokens throughout.

## Trigger (overflow icon button)
40×40, padding `spacing.8`, corner radius `radius.8`, holds the overflow (⋮) icon.
| State | Background | Icon |
|-------|------------|------|
| Default | transparent | `semantic.text.default` |
| Hover | `semantic.surface.pressed` | `semantic.text.default` |
| Active | transparent | `semantic.accent.primary` (highlighted, menu open) |

## Context Option (menu rows)
Rows on an elevated panel (`shadow.default`). Height 40px, horizontal padding `spacing.16`, text `font-m` (16/22).
| State | Background | Text |
|-------|------------|------|
| Default | `semantic.surface.subtle` | `semantic.text.default` |
| Hover | `semantic.surface.hover` | `semantic.text.default` |
| On Click | `semantic.surface.pressed` | `semantic.text.default` |
| Warning | `semantic.surface.subtle` | warning/destructive action (see note) |
| Disabled | `semantic.surface.subtle`, 40% opacity | `semantic.text.default` |

These match the Dropdown option and Search result hover/pressed scale, on a `shadow.default` panel.

## Rules
- Trigger highlights its icon (`accent.primary`) while the menu is open (Active).
- Option rows reuse the surface hover/pressed scale; the menu panel uses `shadow.default`.
- Disabled = 40% opacity (system-wide). Semantic tokens only.

> Note: the **Warning** option is the slot for destructive/warning actions, but in the kit it currently renders with `text.default` (same as a normal row). Recommend coloring its label `semantic.feedback.warning` (or `feedback.error` for destructive) so it reads as distinct. Confirm and update.
