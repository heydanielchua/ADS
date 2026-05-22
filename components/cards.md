# Cards

Contextual information surfaces. Two families: **Cards** (standalone content containers, 467px wide) and **Card Belts** (compact expandable rows for grouped entity data). Semantic tokens throughout.

---

## Cards

All cards share the same 467px width, 16px padding, and a leading icon + text area layout. The card state is expressed through background fill; there is no explicit border or shadow on the card frame itself.

### States
| State | Background | Notes |
|-------|-----------|-------|
| Default | `semantic.surface.default` (white) | |
| Hover | `semantic.surface.subtle` (grey.5) | |
| On Click | `semantic.surface.panel` (accent.30) | lightly brand-tinted |
| Disabled | `semantic.surface.default`, 40% opacity | |

### Card types (same state behaviour)

**Card / Default** (94px) — base card. Leading icon + title + body.
- Title: `font-m-600` (16/22), `semantic.text.default`
- Body: `font-m-400` (16/22), `semantic.text.default`

**Card / Navigation** (94px) — same layout as Default; used as a navigable link card.

**Card / Overlay** (157px) — expanded card with metadata rows.
- Title: `font-m-600`, `semantic.text.default`
- Metadata label (e.g. "GTI:", "Location:"): `font-s-400` (14/20), `semantic.text.muted`
- Metadata value: `font-s-400`, `semantic.text.default`
- Footer: "Last edited [date] by [user]" — `font-s-400`, `semantic.text.default`

**Card / Document** (129px) — card with a file attachment indicator.
- Title: `font-m-600`, `semantic.text.default`
- Body: `font-m-400`, `semantic.text.default`
- File icon: document-type badge using primitive palette colours (e.g. `color.green.10` bg + `color.green.70` icon for the file type)
- Footer: "Last edited [date] by [user]" — `font-s-400`, `semantic.text.default`

**Card / Results** (117.5px) — data results display with a divider and value/unit pairs.
- Header: `font-m-600`, `semantic.text.default`
- Divider: 1px `semantic.field.borderFilled` (grey.35)
- Field label: `font-s-400`, `semantic.text.default`
- Value: `font-size 22` bold (large numeric display), `semantic.text.default`

**Card / ORBAT Update Log** (97px) — entity change record.
- Title + subtitle (unit descriptions): `font-m-600` / `font-m-400`, `semantic.text.default`
- Footer metadata (date, editor): `font-s` bold + regular, `semantic.text.default`

### Section Card (container)
504×170px. A grouping container for a set of cards.
- No fill (transparent)
- Border: 1px `semantic.field.borderFilled` (grey.35)
- Contains: title/heading row + action buttons + child cards

---

## Card Belt

Compact, expandable rows for grouped data sets (e.g. obstacle belts). Width ~436px, height varies by state.

### Card Belt / Collapsed (48px)
A single compact row.
- Background: `semantic.surface.default`
- Entity name: `font-m-600`, `semantic.text.default`; leading icon (16px)
- Trailing action buttons (icon button row)

### Card Belt / Expanded — Details (149px or 312px)
Expands below the collapsed header to show entity detail.
- Divider: 1px `semantic.field.borderFilled` (grey.35) between header and body
- Field label: `font-s` semibold, `semantic.text.default`
- Field value: `font-m-400`, `semantic.text.default`
- Two columns of label-value pairs

### Card Belt / Card in Priority (153px)
Summary card for a whole belt showing prioritised entity data.
- Background: `semantic.surface.default`
- Belt title: `font-m` bold, `semantic.text.default`
- Obstacle name list: `font-m-600`, `semantic.text.default`
- Metadata labels: `font-s-400`, `semantic.text.default`
- Belt colour picker: inline dropdown cell (follows Dropdown spec — `surface.subtle` bg, `border.focus` underline when active)

### Card Belt / Checkbox (131px)
Belt card with a leading checkbox for multi-selection.
- Same content layout as Card in Priority
- Leading checkbox follows Selection Controls spec

---

## Rules
- All card states are expressed through background fill only — no border or shadow on individual cards.
- Section Card is the grouping container and uses a `field.borderFilled` border.
- Card Belts use `field.borderFilled` dividers to separate header from expanded content.
- Metadata label-value pairs: labels in `text.muted` (grey.50), values in `text.default`.
- File type icons use primitive palette colours (colour family chosen per document type).
- Disabled = 40% opacity (system-wide). Semantic tokens only.
