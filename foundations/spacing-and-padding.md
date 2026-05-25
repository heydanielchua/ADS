# Spacing & Padding

All spacing and padding values are **multiples of 4px** and map onto the `spacing.*` token scale.

## Spacing (between elements)

| Value | Token | Usage |
|-------|-------|-------|
| 4px | `spacing.4` | Fine adjustments. |
| 8px | `spacing.8` | Between status components in the System Status Centre; between icon buttons **with** fill or border (toolbar, floating buttons); between a static icon and its text; between an activated button and text. |
| 12px | `spacing.12` | Between icon buttons with **no** fill or border (Action Bar, overlay opacity/visibility icons); Floating Pane header padding. |
| 16px | `spacing.16` | Between icon buttons at the **Top Bar**. |
| 24px | `spacing.24` | Between sections. |
| 32px | `spacing.32` | Between icon buttons at the **Side Bar**. |

## Padding (inside components)

| Value | Token | Usage |
|-------|-------|-------|
| 8px | `spacing.8` | Padding for the Search Bar and Action Bar. |
| 12px | `spacing.12` | Padding for Floating Pane headers. |
| 16px | `spacing.16` | **Default** padding for dialogues, cards and rows; horizontal padding for cards. When vertical space is tight, 12px vertical padding is acceptable. |

## Rules

- Never use arbitrary px values — every gap and pad traces to `spacing.*`.
- Default radius is `radius.8`; full-screen dialogues use `radius.10`.
