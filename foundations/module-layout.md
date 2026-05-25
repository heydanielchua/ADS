# Module Layout

The general layout for every module is **card-based**. The Module Pane consists of a Side Bar, a Search Bar, and an Action Bar, above a list of Cards.

All colour references use **semantic tokens only**.

## Vertical composition

A module pane always stacks its content in this order:

1. **Search Bar** — find content inside the module
2. **Action Bar** — contextual actions for selected entries (top-positioned, per Gmail-style convention)
3. **Cards** — content entries; click into a detailed view (no expanded view)

See `search-bar.md`, `action-bar.md`, and `card.md` for the interplay rule (always Search → Action → Cards).

## Side Bar states

### Unexpanded (72px)
- Width 72px (3.75%) · Height 996px (96.25%); token `sidebar-w`.
- Contains a floating **creation FAB** (call-to-action for new entries, if applicable) and **filter** options.
- Custom/active filters carry a `accent.primary` circle indicator showing that not all content is shown.
- Expands to push content right, like Outlook / Gmail / Amazon.

### Expanded as a landing page (280px)
- Width 280px · Height 996px (96.25%).
- The creation FAB expands to show button text.
- Use **text** options rather than custom icons (custom icons are not easily recognised → higher learnability cost).

### Expanded as navigation (280px)
- Sub-sections appear in this order: (1) common functions, (2) navigational elements, (3) common module pages (e.g. Help, Settings).

## View modes

| Mode | When to use |
|------|-------------|
| **Split Screen** (default) | App + map content side by side for single-view reference. |
| **Fullscreen** | Base map is less relevant and more screen real estate is needed. May be a module's default *and only* mode if it needs no base-map functions. |

## Module colour

Colour use is **deliberate and limited** for cross-module consistency (60-30-10 rule). The accent colour (`accent.primary`) is used **only to indicate active card selection** — e.g. card-header icons are intentionally left un-tinted.

## Rules

- Follow the Search → Action → Cards order in every module pane.
- Reserve `accent.primary` for active selection; do not use it decoratively.
- Disabled = 40% opacity (system-wide). Semantic tokens only.
