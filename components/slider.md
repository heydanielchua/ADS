# Slider

A range-input control for selecting a value (or range) along a track. Three variants and two thumb-colour schemes. Width expands freely — kit guidance: **keep width in multiples of 4px**.

## Thumb colour schemes
Two schemes share identical structure and differ only in colour:

| Scheme | Filled track | Thumb fill |
|--------|-------------|-----------|
| **Black** | `color.grey.95` (#1C1C1C) | `color.grey.95` |
| **Blue** | `semantic.accent.primary` | `semantic.accent.primary` |

The Black scheme is for always-dark-on-light contexts. The Blue scheme ties the slider to the brand accent (shifts to cyan in dark mode).

## Track
- 4px thick line. Width responsive (multiples of 4).
- **Empty portion**: `color.grey.40` (#9C9C9C — mid-grey, primitive reference; dark mode: `color.grey.65`)
- **Filled/active portion**: scheme colour (grey.95 or accent.primary)

## Thumb states
| State | Appearance |
|-------|-----------|
| Active | 16×16 oval, solid scheme colour |
| On Click | 30×30 with inner 16×16 thumb + 20% alpha outer halo (scheme colour at ~20%) |
| Disabled | 16×16, `semantic.field.borderFilled` (grey.35), 40% opacity |

## Value input box (trailing)
A compact inline input showing the current value.
- Size: 44×32. Radius `radius.8`.
- Background: `semantic.surface.hover` (grey.15)
- Text: `font-s` (14/20), `semantic.text.default`
- Active (focused): 1px `semantic.accent.primary` border
- Disabled: 40% opacity

---

## Variants

### Default slider
Single-thumb slider with start/end labels and a value input box.
- **Label** above (left-aligned): `font-xs` semibold, `semantic.text.subtle`
- **Start / End values** flanking the track: `font-m` (16/22), `semantic.text.default`
- **Value input box** trailing the track

### Range slider
Two-thumb slider for selecting a range.
- Same label as Default.
- **Two value input boxes** (start and end) flanking the track.
- Two thumbs (Black scheme); filled track between the two thumbs.

### Ticker slider
A slider with discrete tick marks and labels below the track.
- Thin track line (~`semantic.text.muted` mid-grey).
- **Tick marks**: 2px vertical strokes, `semantic.text.subtle` (grey.65)
- **Tick labels**: small text, `semantic.text.subtle`
- Thumb sits at the current tick position (Black scheme).

## Rules
- Expand width freely; keep in **multiples of 4px**.
- Black scheme for always-dark tracks; Blue scheme when brand accent is preferred.
- Disabled = 40% opacity. Semantic tokens only — except `color.grey.40` and `color.grey.95` which are used as documented primitive references for the track and Black thumb.
