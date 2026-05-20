# Button

Interactive element for triggering actions. The system is a matrix of **size × variant × content × state**, with 209 total component combinations in Lunacy.

All values below reference design tokens (see `/tokens`). Never hard-code raw values.

## Shared properties (all buttons)
- Corner radius: `radius.8`
- Horizontal padding: `spacing.16` (left & right)
- Vertical padding: 11px (tuned to the size's height; not a named token)
- Font: `font.family.sans` (Open Sans), size `font.size.s` (14px), weight `font.weight.regular`
- Icon + text gap: `spacing.8`

## Sizes
| Size | Height | Notes                          |
|------|--------|--------------------------------|
| S    | 32px   | Text and icon+text buttons     |
| M    | 40px   | Text and icon+text buttons     |
| XXS  | 16px   | Icon-only                      |
| XS   | 24px   | Icon-only                      |

## Variants (Default state)
| Variant          | Background          | Border               | Text / icon color   |
|------------------|---------------------|----------------------|---------------------|
| Primary          | `color.accent.60`   | none                 | `color.grey.5`      |
| Secondary        | `color.grey.45`     | none                 | `color.grey.5`      |
| Outlined         | transparent         | 1px `color.grey.65`  | `color.grey.65`     |
| Ghost            | transparent         | none                 | `color.grey.65`     |
| Ghost Blue       | transparent         | none                 | `color.accent.60`   |
| Danger           | `color.red.60`      | none                 | `color.grey.5`      |
| Danger - Outline | transparent         | 1px `color.red.60`   | `color.red.60`      |
| FAB              | `color.accent.60`   | none                 | `color.grey.5`      |

`color.accent.60` resolves to `#0066FF` (your primary blue); `color.grey.5` is the off-white used for text on filled buttons.

## Content types
Each variant exists in three content layouts: **Text only**, **Icon + Text** (icon leads, gap `spacing.8`), and **Icon only** (square; uses the icon-only sizes).

## States
States change color, not geometry. Worked example for **Primary**:
| State    | Background        | Text color     |
|----------|-------------------|----------------|
| Default  | `color.accent.60` | `color.grey.5` |
| Hover    | `color.blue.100`  | `color.grey.5` |
| On Click | `color.grey.95`   | `color.grey.5` |
| Disabled | `color.accent.60` | `color.grey.5` |

Other variants follow the same pattern: hover/pressed shift to a darker step of the variant's own family; outlined/ghost variants darken their text and add a subtle background on hover.

> Disabled is conveyed by **40% opacity** (fill unchanged from Default), consistent with the hyperlink component.

## Rules
- One Primary (or one Danger) per view where possible.
- Use Ghost / Ghost Blue for low-emphasis actions; Outlined for medium emphasis.
- Danger and Danger - Outline are reserved for destructive actions.
- Always reference the tokens above - no literal hex, px, or font values.
