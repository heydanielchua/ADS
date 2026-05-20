# Selection Controls

Checkbox, radio, toggle (switch), composed rows (control + label), and a color swatch. Consistent state language; semantic tokens throughout.

## Shared
- Label: `font-m-400` (16/22). Control->label gap `spacing.8`; toggle+text gap `spacing.16`.
- Disabled: 40% opacity. Active accent: `semantic.brand.primary`.

## Checkbox (12x12)
| State | Box | Check |
|-------|-----|-------|
| Default | outline `semantic.text.default` | none |
| Hover | `semantic.border.focus` | none |
| Selected | filled `semantic.brand.primary` | `semantic.brand.onBrand` |
| Disabled | as above, 40% opacity | - |

## Radio button (12x12)
| State | Ring | Dot |
|-------|------|-----|
| Default | `semantic.text.default` | none |
| Hover | `semantic.border.focus` | none |
| Selected | `semantic.brand.primary` | `semantic.brand.primary` |
| Disabled | as above, 40% opacity | - |

## Toggle / Switch (35x20)
| State | Track | Knob |
|-------|-------|------|
| Off | `semantic.control.toggleTrackOff` | `semantic.control.toggleKnobOff` |
| On | `semantic.control.toggleTrackOn` | `semantic.brand.primary` |
| Disabled | as above, 40% opacity | - |

## Selection row (control + label)
- Label `semantic.text.default` by default; shifts to `semantic.text.link` on hover and when selected.

## Color swatch (16x16)
Empty outlined box (`semantic.text.default`) by default; filled shows the chosen color token + a check (`semantic.brand.onBrand`).

## Rules
- Checkbox = multi-select, radio = single, toggle = on/off.
- Selected = `semantic.brand.primary`. Disabled = 40% opacity. Semantic tokens only.
