# Action Bar

The Action Bar lets users carry out functions on one or more selected sections, cards, or options. It sits at the top of the module content (after the Search Bar), following the Gmail-style convention.

## Dimensions
- Width: variable (e.g. 432px)
- Height: 48px [Fixed]
- Padding: `spacing.8` (8px)

## Layout rules
- **Text buttons**: flushed **left**, `spacing.8` (8px) between each.
- **Icon buttons**: flushed **right**, `spacing.12` (12px) between each.
- **Vertical dividers**: 32px tall, following the spacing of the buttons they separate.
- When a header or text must be left-flushed, **all** buttons move to the right.

## Examples
"New / Import" (Overlay Manager) · "New" (Map Snippets) · "2 members selected … Edit Role / Remove" (User Preferences) — the variant set is not exhaustive.

## Rules
- Pair with a Search Bar above and Cards below (see `module-layout.md`).
- Buttons reference the Button spec; no custom button styling here.
- Disabled = 40% opacity. Semantic tokens only.
