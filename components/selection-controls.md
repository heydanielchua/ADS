# Selection Controls

The family of controls for choosing options: **checkbox**, **radio button**, **toggle (switch)**, plus composed rows (control + label) and a **color swatch** selector. They share a consistent state language.

## Shared
- Label text: `font-m-400` (Open Sans 16 / 22).
- Control-to-label gap: `spacing.8` (selection rows); `spacing.16` (toggle + text).
- Disabled: **40% opacity** across all controls.
- Active/selected accent: `semantic.brand.primary` (`blue.80`).

## Checkbox (12x12)
| State    | Box                         | Check mark        |
|----------|-----------------------------|-------------------|
| Default  | outline `color.grey.100`    | none              |
| Hover    | `color.blue.80`             | none              |
| Selected | filled `color.blue.80`      | light (`#ECECEC`) |
| Disabled | as above, 40% opacity       | -                 |

Slightly rounded square corners.

## Radio button (12x12)
| State    | Ring                     | Dot              |
|----------|--------------------------|------------------|
| Default  | `color.grey.100`         | none             |
| Hover    | `color.blue.80`          | none             |
| Selected | `color.blue.80`          | `color.blue.80`  |
| Disabled | as above, 40% opacity    | -                |

## Toggle / Switch (35x20; track 30x12, knob 20x20)
| State        | Track             | Knob              |
|--------------|-------------------|-------------------|
| Off          | `color.grey.50`   | `color.grey.95`   |
| On           | `color.blue.100`  | `color.blue.80`   |
| Disabled     | as above, 40% opacity | -             |

Knob slides left (off) to right (on); track shifts grey -> blue.

## Selection row (control + label)
- Layout: control + `spacing.8` + label.
- Label color: `color.grey.100` by default; shifts to `color.blue.80` on **hover** and when **selected**.
- Disabled: 40% opacity on the whole row.

## Color swatch selector (16x16)
For color-coded multi-select. Default is an empty outlined box (`color.grey.100`); filled shows the chosen color (any palette token, e.g. `color.yellow.60`) with a check overlay.

## Rules
- Use checkbox for multi-select, radio for single-select, toggle for on/off settings.
- Selected = brand blue; never a raw hex.
- Disabled is always 40% opacity, consistent with buttons, hyperlinks, and pills.
