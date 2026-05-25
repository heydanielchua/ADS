# Descriptive Buttons

Descriptive Buttons give users additional guidance when choosing between several options. A short description inside the button concisely states the function.

## Anatomy
- **Function** title + **description** (maximum 3 lines).
- Padding: `spacing.12` (12px).
- Height and width vary with content.

## States

| State | Border | Fill |
|-------|--------|------|
| Default | `border.default` | `surface.subtle` |
| Hover | `border.default` | `surface.hover` |
| On-click | `border.default` | `surface.pressed` |
| Active (selected) | `border.focus` | `accent.subtle` |

Title uses `body-short-01`; description uses `body-short-02` in `text.muted`.

## Usage
Use when a plain label is not enough to disambiguate options (e.g. "Draw — Mark out a boundary directly on the map" vs "Select from overlay — Select a boundary object from an existing overlay").

## Rules
- Keep descriptions to 3 lines maximum.
- Reserve `accent.subtle` + `border.focus` for the selected state.
- Disabled = 40% opacity. Semantic tokens only.
