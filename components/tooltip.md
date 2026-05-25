# Tooltip (UX 2.0)

> Reconciles with the existing `tooltip.md`. The UX 2.0 master defines two tooltip variants and the padding/scaling rules below.

On hover over a screen element, a tooltip gives users additional information — helper text for an actionable icon, or a more descriptive explanation of a function.

## Variants

| Variant | Use | Surface |
|---------|-----|---------|
| **Primary** | Default tooltip for all elements/components. | `surface.contrast` (always-dark floating surface) |
| **Secondary** | Used **sparingly**, only when the primary colour clashes with the hovered element. | `surface.subtle` |

Text: `body-short-02` in `text.inverted` (Primary) / `text.default` (Secondary).

## Dimensions
- Width and height vary to any suitable size, as long as padding stays fixed.
- Vertical padding: `spacing.16` (16px) [Fixed].
- Horizontal padding: `spacing.8` (8px) [Fixed].
- Radius: `radius.8`.

## Rules
- Tooltips appear on hover only; they are not user-dismissible controls.
- Default to Primary; reach for Secondary only to resolve a colour clash.
- Disabled = 40% opacity. Semantic tokens only.
