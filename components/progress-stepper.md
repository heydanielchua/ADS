# Progress Stepper

A horizontal bar of step segments that shows progress through a multi-step flow. Individual segments are 4px-tall pills; the number of segments and their width are adjustable per context.

## Segment anatomy
- Size: 4px tall × 80px wide (default, adjustable). Keep width in multiples of 4.
- Radius: `radius.8`
- Gap between segments: `spacing.8`

## Segment states — 9 variants (3 semantic × 3 interactive)

### Default (not yet reached)
| Interaction | Fill | Token |
|-------------|------|-------|
| Rest | `color.grey.20` | `semantic.surface.pressed` |
| Hover | `color.grey.30` | primitive |
| Click | `color.grey.40` | primitive |

### Completed (step done)
| Interaction | Fill | Token |
|-------------|------|-------|
| Rest | `color.blue.100` (#114599 dark navy) | primitive |
| Hover | `color.blue.60` (#1C86FF mid blue) | primitive |
| Click | `semantic.accent.primary` (#0066FF → cyan in dark) | semantic |

### Incomplete (mandatory step not yet filled)
| Interaction | Fill | Token |
|-------------|------|-------|
| Rest | `color.red.30` (#FD9996 light red) | primitive |
| Hover | `color.red.50` (#FC605B medium red) | primitive |
| Click | `color.red.100` (#810805 dark red) | primitive |

### Disabled
`color.grey.35` (`semantic.field.borderFilled`), 40% opacity.

## Dark mode (symmetry mirrors)
| Segment | Light | Dark |
|---------|-------|------|
| Default rest | grey.20 | grey.85 |
| Default hover | grey.30 | grey.75 |
| Default click | grey.40 | grey.65 |
| Completed rest | blue.100 | blue.10 |
| Completed hover | blue.60 | blue.50 |
| Completed click | accent.primary | accent.50 (cyan) |
| Incomplete rest | red.30 | red.80 |
| Incomplete hover | red.50 | red.60 |
| Incomplete click | red.100 | red.10 |

## Container card (Content & Stepper)
The stepper lives inside a bordered card, 472×124px (width adjustable).
- Border: 1px `semantic.field.borderFilled` (grey.35), inside
- No background fill (transparent, shows page surface)
- Radius: `radius.8`
- Padding: `spacing.16` all sides
- Vertical layout, gap 14px between title block and stepper bar

### Content
- **Title**: `font-m-600` (16 / 22), `semantic.text.default`
- **Description** (optional): `font-s-400` (14 / 20), `semantic.text.subtle`
- **Step counter** e.g. "Step 1 of 5": `font-s-400`, `semantic.text.subtle`

### Stepper bar
Row of segments at the bottom of the card. Gap `spacing.8` between segments.
Example: 5 steps at 80px each = 432px total bar width.

## Rules
- Use the **Incomplete** state only for mandatory fields users must complete.
- Adjust individual segment width to accommodate the number of steps; keep widths in multiples of 4.
- Completed segments use dark navy (`blue.100`) at rest, lightening to brand blue on hover/click — intentionally different from the accent ramp to read as "permanent/done".
- Semantic tokens only where available; primitive references documented above follow the symmetry rule in dark mode.
