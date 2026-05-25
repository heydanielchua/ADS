# Progress Stepper

Progress steppers show discrete progress through a numbered process — how much is complete and how much remains.

## Variants & dimensions

| Variant | Width | Height | V-pad | H-pad |
|---------|-------|--------|-------|-------|
| Pane | 472px [Fixed] | 82px [Fixed] | `spacing.16` | `spacing.12` |
| Full Screen | 1336px [Fixed] | 82px [Fixed] | `spacing.16` | `spacing.12` |

- Stepper bar height is constant at **4px**; bar width varies with the number of steps.
- Pane variant shows a step title + "Step N of M". Full-screen variant shows all named steps in a row.

## Colour
- Completed / active track: `accent.primary`.
- Remaining track: `border.default`.
- Title `heading-06`; sub-label `body-short-02` `text.muted`.

## Rules
- Keep bar widths in multiples of 4px.
- Disabled = 40% opacity. Semantic tokens only.
