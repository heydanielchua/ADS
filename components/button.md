# Button

Interactive element for triggering actions. A matrix of **size × variant × content × state** (209 combinations in Lunacy). All colors reference **semantic tokens**, so light/dark mode flow through automatically.

## Shared
- Radius `radius.8`; horizontal padding `spacing.16`; vertical padding 11px (tuned to height).
- Text: `font-s-400` (Open Sans 14/20). Icon+text gap `spacing.8`.

## Sizes
| Size | Height | Notes |
|------|--------|-------|
| S | 32px | text / icon+text |
| M | 40px | text / icon+text |
| XXS | 16px | icon-only |
| XS | 24px | icon-only |

## Variants (default state)
| Variant | Background | Border | Text/icon |
|---------|------------|--------|-----------|
| Primary | `semantic.brand.primary` | none | `semantic.brand.onBrand` |
| Secondary | `semantic.control.secondary` | none | `semantic.brand.onBrand` |
| Outlined | transparent | 1px `semantic.border.strong` | `semantic.text.subtle` |
| Ghost | transparent | none | `semantic.text.subtle` |
| Ghost Blue | transparent | none | `semantic.text.link` |
| Danger | `semantic.feedback.error` | none | `semantic.brand.onBrand` |
| Danger - Outline | transparent | 1px `semantic.feedback.error` | `semantic.feedback.error` |
| FAB | `semantic.brand.primary` | none | `semantic.brand.onBrand` |

## Content types
Text only, Icon + Text (icon leads, gap `spacing.8`), Icon only (square; icon-only sizes).

## States (Primary)
| State | Background | Text |
|-------|------------|------|
| Default | `semantic.brand.primary` | `semantic.brand.onBrand` |
| Hover | `semantic.brand.hover` | `semantic.brand.onBrand` |
| On Click | `semantic.surface.pressedStrong` | `semantic.brand.onBrand` |
| Disabled | `semantic.brand.primary`, 40% opacity | - |

Other variants follow the same logic: hover shifts to a stronger shade of the variant's role; outlined/ghost gain a `semantic.surface.hover` background on hover.

## Rules
- One Primary (or Danger) per view where possible.
- Disabled = 40% opacity (system-wide).
- Reference semantic tokens only - never raw hex.
