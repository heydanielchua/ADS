# Dialog

Modal dialogs for confirmations, errors, and transactional form actions. Three variants — all share the same panel anatomy; the title colour and the action button distinguish them. Width 504px.

## Shared anatomy
- Background: `semantic.surface.panel` (accent.30 — the brand-tinted panel surface)
- Border: 1px `semantic.field.borderFilled` (grey.35), inside edge
- Radius: `radius.8`
- Padding: `spacing.16` all sides
- Vertical layout; footer buttons right-aligned

## Variants

### Acknowledgment
For confirmations and informational acknowledgements.
- **Title**: `font-m` bold (16/22), `semantic.accent.primary`
- **Content row**: 20px icon + subtitle (`font-m-600`, `semantic.text.default`) + indented body (`font-m-400`, `semantic.text.default`, 32px left indent)
- **Footer**: Cancel (Outlined, `semantic.border.strong`) + OK (Primary, `semantic.accent.primary`)

### Error
For destructive or error-state confirmations.
- **Title**: `font-m` bold (16/22), `semantic.feedback.error`
- **Content row**: same as Acknowledgment
- **Footer**: Cancel (Outlined, `semantic.border.strong`) + OK (Danger, `semantic.feedback.error`)

The only difference from Acknowledgment is the title and action button use `feedback.error` instead of `accent.primary`.

### Transactional
For form-based dialogs that collect input before confirming an action. Kit guidance: "Padding between transactional fields — 8px."
- **Title**: `font-m` bold (16/22), `semantic.accent.primary`
- **Body text**: `font-m-400` (16/22), `semantic.text.default`
- **Form fields** (dropdown, gap `spacing.8` between fields):
  - Label: `font-xs` semibold, `semantic.text.subtle`
  - Dropdown: `semantic.surface.subtle` (grey.5) bg, placeholder `semantic.field.placeholder`, chevron. Follows Dropdown spec.
  - Error text (hidden by default): `semantic.feedback.error`, shown on validation failure
- **Footer**: Cancel (Outlined, `semantic.border.strong`) + Confirm (Primary, `semantic.accent.primary`)

## Comparison table
| | Acknowledgment | Error | Transactional |
|--|---------------|-------|--------------|
| Title colour | `accent.primary` | `feedback.error` | `accent.primary` |
| Content | icon + text | icon + text | body + form fields |
| Action button | Primary | Danger | Primary |
| Action label | OK | OK | Confirm |

## Rules
- All dialogs use `surface.panel` (accent.30) — the same brand-tinted surface as the Advanced Filter Dialog, creating visual consistency across all floating panels.
- Cancel is always an Outlined button with `border.strong`; the action button variant reflects the dialog's semantic type.
- Transactional field gap: `spacing.8` between form fields (per kit guidance).
- Error text in Transactional dialogs is hidden (`opacity: 0`) by default; reveal on validation failure.
- Semantic tokens only.
