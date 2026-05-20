# Hyperlink

Inline text link. Built on the body text style with color + underline conveying state.

## Base
- Text style: `font-m-400` (Open Sans, `font.size.m` 16px / `font.lineHeight.m` 22px, `font.weight.regular`)

## States
| State    | Color                         | Underline | Opacity |
|----------|-------------------------------|-----------|---------|
| Default  | `semantic.brand.primary` (`#0066FF`) | yes  | 100%    |
| Hover    | `semantic.brand.primary` (`#0066FF`) | no   | 100%    |
| On Click | `color.grey.100` (`#121212`)         | yes  | 100%    |
| Disabled | `semantic.brand.primary` (`#0066FF`) | yes  | 40%     |

## Rules
- Default and disabled links are underlined; underline is removed on hover.
- Pressed (On Click) shifts the text to near-black (`grey.100`) while keeping the underline.
- Disabled is conveyed by 40% opacity, not a different color.
- Always use the brand primary token for link color - never a raw hex.
