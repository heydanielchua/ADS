# Multiple Selection (Multi-select)

A multi-select combobox: a field that displays chosen options as removable pills and opens a searchable dropdown to add more. Built on the Text Field / Dropdown foundation; selected items use the Pill component. Width 472px. Composes existing components — no new tokens needed.

## Anatomy
1. **Selection bar** — the field area showing selected pills + placeholder + right buttons.
   - Selected items render as **XS Pills** (`pill.md`, Cancel Selected variant: `accent.primary` fill + × chip to remove). Pills wrap across multiple lines as more are selected.
   - Placeholder (when empty): "Select option(s)", `font-m`, `semantic.field.placeholder`
   - Right buttons (56×24): chevron (open/close) + clear
2. **Bottom border** — underline carrying field state.
3. **Dropdown panel** (when open) — a search bar + scrollable option list.

## States
| State | Height | Bottom border | Notes |
|-------|--------|---------------|-------|
| Default | 42px | `semantic.border.strong` (grey.65) | collapsed, placeholder shown |
| Active | 282px | `semantic.border.focus` (accent.primary) | dropdown open |
| Filled (1 line) | grows | `semantic.border.focus` | pills shown |
| Filled 3 Lines | 341px | `semantic.border.focus` | pills wrap to 3 lines (each ~25px) |
| Filled Expanded | up to 464px | `semantic.border.focus` | more pills + open dropdown |

The selection bar grows in height as pills wrap; the dropdown panel stays a consistent height below it.

## Dropdown panel (open state)
- **Search bar** — label-less input, `semantic.field.bg` (grey.5). Follows `search.md`.
- **Options list** (472×200, scrollable) — option rows follow the Dropdown option pattern:
  - Default: `semantic.surface.subtle` (grey.5)
  - Hover: `semantic.surface.hover` (grey.15)
  - On Click: `semantic.surface.pressed` (grey.20)
  - Multi-select options carry a checkbox (checked = `semantic.accent.primary`)
- **Scrollbar** — 2px, `semantic.field.borderFilled` (grey.35)

## Rules
- Selected options are removable XS pills (`accent.primary` fill + × cancel); they wrap to new lines as the selection grows.
- Default underline `border.strong`; focused/active and filled use `border.focus` (accent).
- The dropdown reuses the Search + Dropdown-option patterns — keep them consistent with those components.
- Multi-select option rows use checkboxes (toggle), unlike single-select Dropdown.
- Disabled = 40% opacity (system-wide). Semantic tokens only.
