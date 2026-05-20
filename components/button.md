# Button

The primary interactive element for triggering actions.

## Anatomy
- Container (background, padding, radius)
- Label (text)
- Optional leading/trailing icon

## Variants
| Variant   | Background            | Text color           | Use for                |
|-----------|-----------------------|----------------------|------------------------|
| Primary   | `color.brand.primary` | `color.text.inverted`| Main action on a screen|
| Secondary | `color.neutral.100`   | `color.text.default` | Secondary actions      |
| Ghost     | transparent           | `color.brand.primary`| Low-emphasis actions   |
| Danger    | `color.feedback.error`| `color.text.inverted`| Destructive actions    |

## Sizes
| Size | Height | Padding (x) | Font size      |
|------|--------|-------------|----------------|
| sm   | 32px   | `spacing.3` | `font.size.sm` |
| md   | 40px   | `spacing.4` | `font.size.base`|
| lg   | 48px   | `spacing.6` | `font.size.lg` |

## States
- Default, Hover, Active, Focus (visible focus ring), Disabled (50% opacity, no pointer events).

## Rules
- Radius: `radius.md`. Font weight: `font.weight.semibold`.
- Only one Primary button per view where possible.
- Never hard-code a hex value — always reference a token above.
