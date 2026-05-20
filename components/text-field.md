# Text Field

Filled, underline-style input. Label above, helper/error below. Semantic tokens throughout (adapts to dark mode).

## Anatomy
1. **Label** - `font-xs` (12/17), `semantic.text.subtle`. Gap to field `spacing.8`.
2. **Field** - height 40px, background `semantic.field.bg`, no radius, horizontal padding `spacing.16`, bottom-border underline. Optional trailing icon (24px).
3. **Value / placeholder** - `font-m` (16). Placeholder `semantic.field.placeholder`; value `semantic.text.default`.
4. **Helper / error** - `font-xs`, left padding `spacing.16`, gap `spacing.4`.

## States
| State | Bottom border | Text |
|-------|---------------|------|
| Default | `semantic.field.border` | placeholder `semantic.field.placeholder` |
| Hover | `semantic.field.borderHover` | placeholder `semantic.text.subtle` |
| Selected (focus) | `semantic.border.focus` | value `semantic.text.default` |
| Filled | `semantic.border.focus` | value `semantic.text.default` |
| Error | `semantic.feedback.error` | value `semantic.text.default`; helper in `semantic.feedback.error` |
| Disabled | muted, 40% opacity | - |

Field background stays `semantic.field.bg` in every state.

## Variants
Mandatory (asterisk on label, `semantic.feedback.error`), With Measurement Unit (unit shown in field), Number Input (narrower numeric). All across the six states.

## Rules
- Focus/filled use `semantic.border.focus`; error uses `semantic.feedback.error`.
- Disabled = 40% opacity. Semantic tokens only.
