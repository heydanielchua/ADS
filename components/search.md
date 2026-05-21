# Search

A search pattern with two parts: the **Search bar** (input) and the **Search Result Item** (rows in the results dropdown). Built on the input foundation; semantic tokens throughout.

## Search bar
A label-less input with a leading search icon and trailing action button(s).
- **Container** - `semantic.field.bg`, height 40px, padding `spacing.8`, icon→text gap `spacing.16`, bottom-border underline (2px). Min width 472px, max ~1826px.
- **Leading icon** - 24px search glyph, `semantic.text.default`.
- **Input / placeholder** - `font-m` (16/22).
- **Trailing buttons** - icon button(s) (e.g. clear); appear once there's input.

| State | Underline | Input text |
|-------|-----------|-----------|
| Enabled (rest) | `semantic.border.strong` | placeholder `semantic.field.placeholder` |
| Hover | `semantic.border.strong` | placeholder `semantic.text.subtle` |
| Active (focus) | `semantic.border.focus` | value `semantic.text.default` |
| Filled | `semantic.border.strong` | value `semantic.text.default` |
| Disabled | `semantic.field.borderFilled`, 40% opacity | placeholder |

Note: unlike the Text Field (which rests on `field.border`), the Search bar rests on the stronger `border.strong` underline, and only the focused **Active** state switches to the accent `border.focus`.

## Search Result Item
A row in the results dropdown. The results panel is elevated with `shadow.default`.
- **Layout** - vertical, padding `spacing.8`, gap `spacing.8`.
- **Title** - `font-s` bold (14/20), `semantic.text.default`.
- **Description** (optional) - `font-xs` (12/17), `semantic.text.default`.

| State | Background |
|-------|-----------|
| Default | `semantic.surface.subtle` |
| Hover | `semantic.surface.hover` |
| On Click | `semantic.surface.pressed` |

These mirror the Dropdown option states, with a two-line title/description layout and the dropdown elevation.

## Rules
- Active/focused search uses the accent underline (`border.focus`); all other states use `border.strong`.
- Result items reuse the surface hover/pressed scale, on an elevated `shadow.default` panel.
- Disabled = 40% opacity (system-wide). Semantic tokens only.
