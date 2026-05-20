# Text Field

Filled, underline-style text input. A label sits above the field; a helper/error line sits below. Used for text, numeric (Number Input), and unit-suffixed entry.

## Anatomy
1. **Label** - above the field. `font-xs` (12 / 17), `color.grey.65`. Gap to field: `spacing.8`.
2. **Field** - height 40px, background `color.grey.5`, no corner radius, horizontal padding `spacing.16`. Has a **bottom border** (underline) that carries state. Optional trailing icon (24px).
3. **Value / placeholder text** - `font-m` (16). Placeholder `color.grey.45`; typed value `color.grey.100`.
4. **Helper / error text** - below the field, `font-xs` (12 / 17), left padding `spacing.16`, gap `spacing.4`.

## States (bottom border + text)
| State    | Bottom border     | Text color        | Notes                       |
|----------|-------------------|-------------------|-----------------------------|
| Default  | `color.grey.45`   | placeholder `grey.45` |                         |
| Hover    | `color.grey.65`   | placeholder `grey.65` |                         |
| Selected (focus) | `color.blue.80` | value `grey.100` | active/focused          |
| Filled   | `color.blue.80`   | value `grey.100`  | has content                 |
| Error    | `color.red.60`    | value `grey.100`  | error text shown in `red.60`|
| Disabled | muted, 40% opacity| -                 | per system convention       |

Field background stays `color.grey.5` in every state; only the border (and text) change.

## Variants
- **Mandatory** - appends a required asterisk to the label (`Input Label*`).
- **With Measurement Unit** - shows a unit label (e.g. "L") inside the field alongside the value.
- **Number Input** - narrower numeric field (~100px) with a numeric value.
- Each variant exists across all six states; Mandatory and Measurement Unit also combine.

## Rules
- Focus/active and filled states use the brand blue underline (`blue.80`).
- Error uses `red.60` for both the underline and the helper text.
- Placeholder is `grey.45`; real input value is `grey.100`.
- Disabled is 40% opacity, consistent with the rest of the system.
- Always reference tokens - no raw hex.
