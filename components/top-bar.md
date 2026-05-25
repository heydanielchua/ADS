# Top Bar

The Top Bar is permanent and serves as the main point of navigation. It contains two sections — the **Module Bar** (left) and the **System Status Centre** (right) — flushed to opposite edges of the screen for accessibility and efficiency (Fitts's Law).

Plane `z-system` (30). All values reference tokens.

## Dimensions
- Width: 1920px (100%)
- Height: 84px (`topbar-h`)
- Drop shadow: `shadow.default` — colour `color.black` @ 16%, X 0 / Y 3, blur 6.

## Module Bar
Width 504px (`pane-compact`, same as Module Pane). Consists of:
1. **More Modules** — opens the More Modules pane (Windows Start-button equivalent) for all installed modules not pinned.
2. **Pinned Modules** — user-pinnable module tiles.
3. **'Last Opened' Module** — the most recently used module.

Default pinned modules on first login: **Canvas, Ops Log, CET, ORBAT, Terrain Analysis**.

### Pinned module tile
- Width 76px · Height 72px (within the 84px bar). Spacing between tiles: 0px.
- Icon 32×32 above a 12px label (`caption-01`, weight 400).
- Number of pinned tiles is variable (see States).

## States

| State | Treatment |
|-------|-----------|
| Default | Icon `text.muted` + label `caption-01` weight 400. |
| Active Module | Icon `accent.primary` + label `caption-01` **weight 700**; tile reads as selected. |

Varying pinned counts are supported (the spec illustrates 2× through the configured maximum). The label size steps down (12px → 11px) as more tiles are packed in.

> Open item to confirm: the maximum number of pinned modules. The source deck states "up to 10" in one place and "up to five" in another. Pick one before shipping.

## System Status Centre
Right-flushed. Contains the exercise clock (see `clock-pane.md`), notification centre, system functions, and user settings. All system-status UI (including toasts) is fixed to the right.

## More Modules pane header & card
- **Header**: 504px × 68px, padding `spacing.16`, title `heading-05` in `text.default`, plus an "Edit Module Bar" affordance.
- **Module card**: 504px × 80px, padding `spacing.16`; name `heading-06` `text.default`, description `body-short-02` `text.muted`.

## Rules
- The Top Bar never scrolls or hides; it is fixed at `z-system`.
- Reserve `accent.primary` for the active module only.
- Disabled = 40% opacity. Semantic tokens only.
