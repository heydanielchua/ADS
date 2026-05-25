# System Layout

The C3 (ORMR UX 2.0) system is a map-centric command application. Its UI is organised as a set of fixed **surfaces stacked along a positive z-axis** toward the user. Defining this structure ensures a consistent, predictable experience and reduces the learning curve.

All colour references below use **semantic tokens only** (see `/tokens`). All dimensions are given against a `1920 × 1080` reference frame.

## Spatial depth (the core mental model)

Surfaces sit at fixed depths. Surfaces on the **same** plane interact (e.g. the Module Pane pushes the Floating Buttons to the right). Surfaces on a **higher** plane overlap those on a lower plane.

| Plane | Token | Surfaces |
|-------|-------|----------|
| Z = +3 | `z-system` (30) | Top Bar · More Modules Pane · Notifications / Menu Pane |
| Z = +2 | `z-module` (20) | Side Bar · Module Pane · Floating Buttons · Floating Pane |
| Z = +1 | `z-overlays` (10) | Overlays |
| Z = 0 | `z-base` (0) | Base Map |

## The nine surfaces

1. **Top Bar** — permanent primary navigation
2. **Side Bar** — left rail, expandable when a module is open
3. **Module Pane** — module content, flush left
4. **More Modules Pane** — launcher for unpinned modules
5. **Notifications / Menu Pane** — system status & alerts
6. **Floating Buttons** — map call-to-actions at screen corners
7. **Floating Pane** — panels opened by floating buttons
8. **Overlays** — map data layers
9. **Base Map** — the map canvas

## Dimensions

| Surface | Width | Height | Token / Notes |
|---------|-------|--------|---------------|
| Top Bar | 1920px (100%) | 84px (7.8%) | `topbar-h` = 84. Module Bar left, System Status Centre right (Fitts's Law). |
| Module Bar | 504px (26.25%) | 84px | Same width as Module Pane. |
| Side Bar | 72px (3.75%) | 996px (96.25%) | `sidebar-w` = 72. Expands to 280px. |
| Module Pane | 504px (26.25%) | 996px (96.25%) | `pane-compact` = 504. Translates map centre right. |
| More Apps Pane | 400px (20.83%) | 1080px (100%) | Flush left, below System Status Centre. |
| Notifications / Menu Pane | 400px (20.83%) | 1080px (100%) | Flush right. |

## Rules

- The Top Bar is always present and fixed; all system-status UI (toasts, alerts) is fixed to the **right** of the screen.
- The Module Pane offers a default **split view** of app + map; some modules also (or only) support **fullscreen** — see `module-layout.md`.
- Floating Buttons live on the same plane as the Module Pane and are pushed right when it is open.
- Never hard-code z-index, dimensions, or colour. Reference layout tokens, `spacing.*`, and semantic colour tokens only.
