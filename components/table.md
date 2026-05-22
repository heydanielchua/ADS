# Table

A data table with two sizes, hierarchical column headers, and six column item types. Every cell has a 2px bottom border that carries row state. Semantic tokens throughout.

## Sizes
| Size | Row height | Text | Padding (x, y) |
|------|-----------|------|----------------|
| M (Medium) | 40px | `font-m-400/600` (16/22) | `spacing.16` / 8px |
| S (Small) | 28px | `font-s-400/600` (14/20) | `spacing.8` / 4px |

Fixed heights per size. Bottom border: 2px path, full width.

---

## Column Headers

### Default header
- Fill: `semantic.surface.pressed` (grey.20)
- Text: `font-m-600` (M) / `font-s-600` (S), `semantic.text.default`
- Leading chevron icon (sort/expand indicator), trailing sub-header optional

### Hierarchy levels (tree headers)
Nested columns shown by progressive left padding + a leading chevron per level. Fill darkens as ancestry rises:

| Level | Fill | Token |
|-------|------|-------|
| Child / Grandchild / Great Grandchild | `color.accent.30` | `semantic.surface.panel` |
| Parent | `color.grey.20` | `semantic.surface.pressed` |
| Grandparent | `color.grey.30` | primitive |
| Great Grandparent | `color.grey.35` | `semantic.field.borderFilled` |

### Special header cells
- **Selection** — surface.pressed + checkbox (default unchecked)
- **Selection & Dropdown** — surface.pressed + checkbox + chevron
- **Icon** — surface.pressed + icon (24px M / 20px S)

---

## Column Items (Row Cells)

### Standard item states
| State | Fill | Bottom border |
|-------|------|--------------|
| Default | `semantic.surface.panel` (accent.30) | `semantic.field.borderFilled` |
| Hover | `semantic.surface.hover` (grey.15) | `semantic.field.borderFilled` |
| Selected | `semantic.accent.subtle` (blue.10) | `semantic.accent.primary` |
| Disabled | `semantic.surface.hover`, 40% opacity | `semantic.field.borderFilled` |

All items: text `semantic.text.default`, `font-m/s-400`.

### In Field (editable cell)
A read/write cell with an inner underline. Outer row border remains `field.borderFilled`.
| State | Inner underline | Text |
|-------|----------------|------|
| Default | `semantic.field.borderFilled` | `semantic.field.placeholder` |
| Active (focus) | `semantic.border.focus` | `semantic.text.default` |
| Error | `semantic.feedback.error` | `semantic.text.default` |

### Dropdown cell
A cell containing an inline dropdown trigger.
- Background: `semantic.surface.subtle` (grey.5)
| State | Inner underline |
|-------|----------------|
| Default | `semantic.field.borderFilled` |
| Hover | `semantic.border.strong` |
| Active | `semantic.border.focus` |
| Disabled | `semantic.field.borderFilled`, 40% opacity |

### Selection cell (checkbox column)
- Fill: `semantic.surface.panel`
- Default bottom border: `semantic.field.borderFilled`
- Selected bottom border: `semantic.accent.primary`

### Icon cell
- Fill: `semantic.surface.panel`
- Icon: `semantic.text.default`
- Default/Selected bottom border mirrors selection cell.

---

## Row Bottom Borders
The 2px bottom border is the primary row-state indicator:
| Row state | Border color |
|-----------|-------------|
| Default | `semantic.field.borderFilled` (grey.35) |
| Selected | `semantic.accent.primary` |
| Active field | `semantic.border.focus` |
| Error field | `semantic.feedback.error` |
| Hover dropdown | `semantic.border.strong` |

---

## Rules
- Default cell background is `surface.panel` (accent.30) — the same lightly brand-tinted surface as the filter dialog, keeping table cells distinct from the page bg.
- Selected rows use `accent.subtle` (blue.10) fill + `accent.primary` bottom border.
- Default selection type is checkbox. Note from kit: "Default Box selection is checkbox selection."
- Hierarchy headers use fill to encode depth — Great Grandparent is darkest (grey.35), children lightest (surface.panel).
- Disabled = 40% opacity (system-wide). Semantic tokens only.
