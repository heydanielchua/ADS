# Selected Text

The text-selection pattern: a highlight behind selected text plus a small **selection context menu** that appears after the user selects text. No new tokens required.

## Text selection highlight
When the user selects text, the selected run is highlighted.
- **Highlight background**: `color.blue.50` (#2D8EFC) — a legible mid-blue (lighter than `accent.primary`, the same shade used by the loader bar)
- **Selected text colour**: `semantic.text.inverted` (near-white) — white text reads cleanly on the blue highlight
- Text style unchanged otherwise (e.g. `font-s-400`)

This maps to the CSS `::selection` role. In dark mode, apply the symmetry rule: `blue.50` → `blue.60`.

## Selection context menu
A compact menu that appears after a selection is made.

**Behaviour** (from kit annotation): the menu appears **0.75s after the user releases the mouse**, or immediately on **right-click**.

**Container & options**
- Background: `semantic.surface.subtle` (grey.5)
- Shadow: `shadow.default` (12% — floats above the text)
- Layout: vertical stack of options, each padding `spacing.16` horizontal
- Option text: `font-m`, `semantic.text.default`

**Options**
| Option | State |
|--------|-------|
| Copy selected text | enabled |
| Paste selected text | hidden / 40% opacity until applicable |

Options follow the Context Menu option styling (`context-menu.md`) — hover `surface.hover`, on-click `surface.pressed`.

## Rules
- Selection highlight uses `blue.50` + `text.inverted` — a deliberate mid-blue, not `accent.primary`, for legibility behind text.
- The selection menu reuses the Context Menu option pattern on a `surface.subtle` panel with `shadow.default`.
- Paste is shown disabled (40% opacity) when there is nothing to paste.
- Semantic tokens where available; `blue.50` is a documented primitive reference for the selection colour.
