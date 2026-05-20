# Pill

A compact, fully-rounded chip used for selectable tags/filters (e.g. multi-select). Comes in two sizes, each with six states. Includes a trailing icon; selected pills can carry a cancel/remove control.

## Sizes
| Size        | Height | Padding (x, y)            | Text style              |
|-------------|--------|---------------------------|-------------------------|
| Default     | 36px   | `spacing.16`, 6px         | `font-s-400` (14 / 20)  |
| XS          | 25px   | `spacing.8`, `spacing.4`  | `font-xs-400` (12 / 17) |

- Corner radius: fully rounded (`radius.full`; the kit uses 32px).
- Icon + text gap: `spacing.4` (`spacing.2` on XS hover).

## States
| State           | Fill              | Border              | Text / icon        |
|-----------------|-------------------|---------------------|--------------------|
| Default         | transparent       | 1px `color.grey.65` | `color.grey.100`   |
| Hover           | `color.grey.15`   | 1px `color.grey.65` | `color.grey.100`   |
| On Click        | `color.grey.20`   | 1px `color.grey.65` | `color.grey.100`   |
| Selected Default| `semantic.brand.primary` (`blue.80`) | same blue | `color.grey.5` (icon white) |
| Cancel Selected | `semantic.brand.primary` (`blue.80`) | same blue | `color.grey.5` + cancel chip |
| Disabled        | transparent       | 1px `color.grey.65` | `color.grey.100`, 40% opacity |

## Behavior
- Unselected pills are outlined (grey border, dark text); hover/press fill with a light grey (`grey.15` → `grey.20`).
- Selecting fills the pill with brand blue and flips text/icon to off-white (`grey.5`).
- **Cancel Selected** adds a small remove control (light-grey chip, `color.grey.20`) so users can deselect.
- Disabled = 40% opacity, matching the button and hyperlink convention.

## Rules
- Always pill-shaped (`radius.full`); never square corners.
- Selected state uses the brand primary token, not a raw hex.
- Keep the two sizes consistent: Default for standard density, XS for compact rows.
