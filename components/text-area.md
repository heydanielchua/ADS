# Text Area

Multi-line input built on the Text Field foundation, plus a character counter. Semantic tokens throughout. See `text-field.md`.

## Anatomy
1. **Label row** - label (left) + **character counter** (right, e.g. "0/100"). `font-xs`, Open Sans Semibold, `semantic.text.subtle`. Gap to field `spacing.8`.
2. **Field** - background `semantic.field.bg`, padding `spacing.16` x / `spacing.8` y, bottom-border underline. Min height 40px, grows.
3. **Value / placeholder** - `font-m` (16/22).
4. **Helper / error** - `font-xs`, gap `spacing.4`; error `semantic.feedback.error`.

## States
| State | Bottom border | Text |
|-------|---------------|------|
| Default | none (hidden) | placeholder `semantic.field.placeholder` |
| Hover | `semantic.field.borderHover` | placeholder `semantic.text.subtle` |
| On Click (focus) | `semantic.border.focus` | value `semantic.text.default` |
| Filled | `semantic.field.borderFilled` (see note) | value `semantic.text.default` |
| Error | `semantic.feedback.error` | value `semantic.text.default`; alert icon + error text |
| Disabled | 40% opacity | - |

## Consistency with Text Field
Three intentional fixes to keep inputs uniform (recommended = match Text Field):
| Aspect | Text Field | Text Area (current) | Recommended |
|--------|------------|---------------------|-------------|
| Focus state name | "Selected" | "On Click" | one name |
| Default underline | visible `semantic.field.border` | hidden | match |
| Filled underline | `semantic.border.focus` | `semantic.field.borderFilled` | match (use `border.focus`) |

## Rules
- Multi-line input; show counter when a max length applies.
- Disabled = 40% opacity. Semantic tokens only.
