# Icons

The icon system has two parts: **sizes** (tokens, in `/tokens/icon.json`) and the **glyphs** themselves (SVG assets, stored in `/icons`).

## Sizes
| Token         | Size | Use                                  |
|---------------|------|--------------------------------------|
| `icon.size.xxs` | 16px | Dense UI, small inline icons        |
| `icon.size.xs`  | 24px | **System default** (24x24 frame)    |
| `icon.size.s`   | 32px | Larger touch targets                |
| `icon.size.m`   | 40px | Prominent / standalone icons        |

Rule from the kit: system icons are designed in a **24x24px frame**. These align with the icon-only button sizes (XXS/XS/S/M).

## Categories
| Category        | Purpose                                                      |
|-----------------|--------------------------------------------------------------|
| System icons    | General-purpose UI (actions, navigation, status)             |
| Module icons    | Top-level module/section markers                             |
| Submodule icons | Sub-section markers within a module                          |
| Toast icons     | Notification states (see semantic mapping below)             |
| Unit icons      | Domain taxonomy: CSS, Infantry, Armour, Artillery, C4, GBAD (Main Units / SAM Equipment / SAM), FI, Manoeuvre, Special |

## Toast icon semantics
Toast icons are color-coded to the feedback tokens (inferred from their colors - confirm and adjust):
| Toast    | Color token            |
|----------|------------------------|
| Error    | `semantic.feedback.error`   (red)   |
| Warning  | `semantic.feedback.warning` (amber) |
| Info     | `color.blue.80` / `color.sky` (blue) |
| Success  | `semantic.feedback.success` (green) |

## Storing the glyphs (asset workflow)
SVGs are not stored as tokens. Export them from Lunacy and place them in `/icons`, grouped by category:
```
icons/
  system/
  module/
  submodule/
  toast/
  unit/
```
Export guidance:
- Export at the 24x24 frame; SVG format.
- Name files kebab-case by their icon name (e.g. `arrow-left.svg`, `gbad-sam.svg`).
- Where possible, set fills to `currentColor` so an icon inherits its parent's text color and can be tinted with color tokens. Multi-color unit icons may keep fixed fills.

## Rules
- Reference sizes via `icon.size.*`; default to `icon.size.xs` (24px).
- Tint single-color icons with color tokens, not raw hex.
- Keep the 24x24 design frame for new system icons.
