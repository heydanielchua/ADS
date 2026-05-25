# Widgets

Widgets surface crucial module information at a glance. Content must be concise and purposeful so it is understood in the shortest time. Widgets summarise core module features and let users navigate directly to modules. They are used in the **Canvas** module, where a single slide acts as an analytical dashboard of widgets for monitoring.

Widgets come in different sizes; users choose what makes sense for them.

## Widget grid
Placement is governed by a layout grid for clear, consistent alignment. The grid defines widget sizes — widgets scale up and down to the grid.

### Grid canvas
- Width 1920px · Height 1080px (scaled proportionally to a 16:9 aspect ratio).
- Column: 146px · Row: 106px
- Gutter: 12px (`spacing.12`)
- Margins: 15px top & bottom, 18px left & right.

### Module unit
- Base unit: 146 × 106px. Larger widgets are multiples of the unit plus gutters.

## Colour
- Surface `surface.subtle`; border `border.default`.
- Headings `heading-06`; values `heading-01`/`heading-03` for large numerics; labels `caption-01`.
- Accent (`accent.primary`) used sparingly for selection/emphasis only.

## Rules
- Snap every widget to the grid; sizes are multiples of the module unit.
- Disabled = 40% opacity. Semantic tokens only.
