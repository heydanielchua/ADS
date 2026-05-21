# Hyperlink

Inline text link. Color + underline convey state. References semantic tokens, so it adapts to dark mode (brand shifts blue->cyan).

## Base
- Text style: `font-m-400` (Open Sans 16/22).

## States
| State | Color | Underline | Opacity |
|-------|-------|-----------|---------|
| Default | `semantic.text.link` | yes | 100% |
| Hover | `semantic.text.link` | no | 100% |
| On Click | `semantic.text.default` | yes | 100% |
| Disabled | `semantic.text.link` | yes | 40% |

## Rules
- Underlined by default; underline removed on hover.
- Pressed shifts to `semantic.text.default` (near-black light / near-white dark).
- Disabled = 40% opacity. Reference semantic tokens only.
