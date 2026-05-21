# Tabs

Two types: **Line** (primary, for pages/panes) and **Contained** (secondary, nested in cards/panels). Semantic tokens throughout — no new tokens needed.

---

## Line Tabs
Primary navigation between related content groups at the same hierarchy level. Height 40px; the 2px bottom-border underline carries state.

**Anatomy**
- Text centered, `font-m` (16 / 22). Optional leading icon (16px) or trailing action icon.
- Bottom border: 2px path, full width.
- No fill; background is transparent.
- Padding: 8px bottom, content centred vertically.

**States**
| State | Fill | Bottom border | Text |
|-------|------|--------------|------|
| Default | transparent | `semantic.border.strong` (grey.65) | `semantic.field.placeholder` (grey.45) |
| Hover | `semantic.surface.hover` | `semantic.border.strong` | `semantic.text.subtle` (grey.65) |
| On Click | `semantic.surface.hover` | `semantic.border.strong` | `semantic.text.subtle` |
| Active | transparent | `semantic.accent.primary` | `semantic.accent.primary`, **bold** (`font-m-600`) |
| Disabled | transparent | `semantic.border.strong` | `semantic.field.placeholder`, 40% opacity |

Active tab text is bold and coloured `accent.primary`; all others are regular weight.

**Variants**
- **Text only** — label centred.
- **Custom (icon + text)** — leading 16px icon + label; bottom border hidden at rest (shown on hover/active).
- **Custom & Icon** — label + trailing action icon button (`surface.pressed` bg on hover).

---

## Contained Tabs
Secondary navigation; used nested inside cards and panels. Height 30px; no bottom border. Tabs connect as a group with shared dividers.

**Anatomy**
- Padding: `spacing.16` (x) / 4px (y).
- Corner radius by position — Left: `radius.8` on left corners; Center: no radius; Right: `radius.8` on right corners.
- Vertical dividers between tabs: 1px `semantic.field.borderFilled` (grey.35), absolute-positioned (height = container − vertical padding).

**States**
| State | Fill | Text |
|-------|------|------|
| Default | `semantic.surface.pressed` (grey.20) | `semantic.text.default` |
| Hover | `semantic.surface.hover` (grey.15) | `semantic.text.default` |
| Active | `semantic.surface.contrast` (grey.100 light / grey.5 dark) | `semantic.text.inverted` |
| Disabled | `semantic.surface.pressed` (grey.20) | `semantic.text.default`, 40% opacity |

The active tab uses `surface.contrast` — the always-dark floating surface — giving an inverted appearance (dark bg + light text) that stands out inside the panel.

**Variants**
- Text only.
- Icon only: 52px wide, 20px icon centred.

---

## When to use each
| | Line | Contained |
|-|------|-----------|
| Context | Pages, panes, main layout | Cards, dialogs, nested panels |
| Kit description | Primary | Secondary (MARIK) |
| Active indicator | Accent underline | Inverted dark fill |

## Rules
- Only one active tab per group at a time.
- Line tabs use accent colour for active; Contained tabs use the inverted surface.
- Disabled = 40% opacity (system-wide). Semantic tokens only.
