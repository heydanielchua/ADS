# Dropdown

A select control: a **trigger** (built on the Text Field foundation) that opens a **menu** of options. Three types — plain, Checkbox (multi-select), and Color — each with a Mandatory variant and five states. Semantic tokens throughout.

## Trigger
Same anatomy and state model as the Text Field, plus a trailing chevron icon:
- **Label** above - `font-xs`, `semantic.text.subtle`.
- **Field** - `semantic.field.bg`, horizontal padding `spacing.16`, bottom-border underline, height 40px, trailing chevron (24px).
- **Value / placeholder** - `font-m`; placeholder `semantic.field.placeholder`, value `semantic.text.default`.

| State | Underline | Notes |
|-------|-----------|-------|
| Default | `semantic.field.border` | closed |
| Hover | `semantic.field.borderHover` | |
| On Click | `semantic.border.focus` | menu open |
| Filled | `semantic.border.focus` | has a selection |
| Disabled | muted, 40% opacity | |

Mandatory variant appends a required asterisk (`semantic.feedback.error`).

## Types
- **Dropdown** - single select; trigger shows the chosen value.
- **Dropdown Checkbox** - multi-select; options carry checkboxes, trigger summarises the count/selection.
- **Dropdown Color** - select a color; options show a swatch.

## Menu options
Option rows, height 40px, horizontal padding `spacing.16`, text `font-m`.
| Option state | Background | Text |
|--------------|------------|------|
| Default | `semantic.surface.subtle` | `semantic.text.default` |
| Hover | `semantic.surface.hover` | `semantic.text.default` |
| On Click | `semantic.surface.pressed` | `semantic.text.default` |

- **Selection option** (Checkbox type) - same backgrounds, with a checkbox; checked uses `semantic.accent.primary` + `semantic.accent.onAccent`.
- **Ghost Blue option** - text in `semantic.text.link`, for an inline action (e.g. "Clear" / "Select all").

## Rules
- Trigger mirrors the Text Field; keep them visually consistent.
- Open/active and filled states use `semantic.border.focus`.
- Disabled = 40% opacity (system-wide). Semantic tokens only.
