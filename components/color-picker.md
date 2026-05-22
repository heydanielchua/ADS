# Color Picker

A compact floating palette panel for selecting a colour from the design system's primitive ramp. Width 237px. Semantic tokens throughout — no new tokens needed.

## Color Pick Box (237×288)

**Container**
- Background: `semantic.surface.panel` (accent.30 — same brand-tinted surface as filter dialogs and dialogs)
- Border: 1px `semantic.field.borderFilled` (grey.35)
- Radius: `radius.8`
- Content width: 203px (17px horizontal padding each side)

### Sections (top to bottom)

**Top Row** (203×16)
8 Color Box swatches in a single row. Used for frequently used or semantic/contextual colours.

**Neutrals** (203×16)
8 Color Box swatches showing the grey ramp (grey family steps).

**Colors** (203×169)
8 chromatic family columns, each with 11 shade steps (100→05). Families shown:
Teal · Cyan · Blue · Violet · Purple · Pink · Punch · Red

Each column is 16px wide; rows are ~15px tall per shade step.

**Custom Color** (86×27)
A "Custom Color..." text link for opening a full colour picker.
- Divider above: 1px `semantic.field.borderFilled` (grey.35), full width
- Text: "Custom Color...", `font-m-400`, `semantic.text.default`

---

## Color Box (swatch cell)

Individual colour swatch used inside the Color Pick Box. The hover state "lifts" the swatch by expanding it 1px outward on each side.

| State | Size | Fill | Border |
|-------|------|------|--------|
| Default | 16×16px | any `color.{family}.{step}` | none |
| Hover | 18×18px | same | 1px `semantic.border.strong` (grey.65) |

The swatch fill is the selected colour token (primitive reference). The 2px expansion on hover is a micro-interaction — no layout shift; the swatch expands in place by 1px per side.

---

## Rules
- The Color Pick Box reuses `surface.panel` — consistent with the filter dialog, dialog, and tooltip panel surface.
- Only 8 of the 15 chromatic families are shown in the picker (Teal, Cyan, Blue, Violet, Purple, Pink, Punch, Red). The warmer families (Lime, Green, Turquoise, Sky, Yellow, Amber) may appear in a separate picker or the Top Row.
- Color Box swatch fill is always a primitive `color.{family}.{step}` reference — never a semantic token (since the value is the colour itself, not a role).
- Hover border `border.strong` (grey.65) gives the swatch a visible selection ring without obscuring adjacent swatches.
- Semantic tokens only for chrome; primitive tokens for swatch fills.
