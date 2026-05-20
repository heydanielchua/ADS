# Pill

Compact, fully-rounded selectable chip (tags / multi-select). Two sizes, six states. Semantic tokens throughout.

## Sizes
| Size | Height | Padding (x, y) | Text |
|------|--------|----------------|------|
| Default | 36px | `spacing.16`, 6px | `font-s-400` (14/20) |
| XS | 25px | `spacing.8`, `spacing.4` | `font-xs-400` (12/17) |

- Radius `radius.full`. Icon+text gap `spacing.4`.

## States
| State | Fill | Border | Text/icon |
|-------|------|--------|-----------|
| Default | transparent | 1px `semantic.border.strong` | `semantic.text.default` |
| Hover | `semantic.surface.hover` | 1px `semantic.border.strong` | `semantic.text.default` |
| On Click | `semantic.surface.pressed` | 1px `semantic.border.strong` | `semantic.text.default` |
| Selected | `semantic.brand.primary` | same | `semantic.brand.onBrand` |
| Cancel Selected | `semantic.brand.primary` | same | `semantic.brand.onBrand` + cancel chip (`semantic.surface.pressed`) |
| Disabled | transparent | 1px `semantic.border.strong` | `semantic.text.default`, 40% opacity |

## Rules
- Always pill-shaped. Selected uses `semantic.brand.primary` (cyan in dark mode).
- Disabled = 40% opacity. Semantic tokens only.
