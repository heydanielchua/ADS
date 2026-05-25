# Floating Buttons

Floating Buttons are call-to-actions for map (SmartGIS) functions, located at the corners of the screen. They lie on the same plane as the Module Pane (`z-module`) and are pushed right when it expands. When active, their functions typically open in Floating Panes on the same plane.

## Dimensions
- 44 × 44px [Fixed], `radius.8`.
- Padding: 10px.
- Spacing from screen edge: `spacing.24` (24px). Spacing between buttons: `spacing.8` (8px) on all sides.

## States

| State | Fill | Icon |
|-------|------|------|
| Default | `surface.hover` (grey.15) | `text.muted` (grey.50) |
| Hover | `surface.hover` (grey.15) | `accent.hover` |
| On-click | `surface.pressed` (grey.20) | `accent.hover` |
| Active | `surface.contrast` (grey.100) | `text.inverted` (grey.5) |

## Examples of functions
Storytelling Library, Map Intel, Map Snippets, Location Search, Overlays Manager, Terrain Analysis Tools, Base Map, Common Operating Picture; plus map controls: Field of Vision, 2D/3D Map, Map Grid On/Off, Panning Tool, Coordinates, Zoom, Viewport.

## Rules
- Default and Hover share the same fill (`surface.hover`); the icon colour carries the hover signal.
- Disabled = 40% opacity. Semantic tokens only.
