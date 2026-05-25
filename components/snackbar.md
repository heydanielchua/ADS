# Snackbars / Toasts

Snackbars provide brief, informative feedback (single line, maximum 2 lines) directly related to an operation just performed. They may contain a single text action. Use a toast — **not** a dialogue — when the system auto-generates an alert that is *not* a direct consequence of a user action.

## Placement
Always centralised, **48px above the bottom edge** of the screen. Fixed at `z-system`.

## Dimensions
- Single line: 432px wide, height 56px.
- Double line: up to ~496px wide, height 66px.
- Padding: `spacing.16` horizontal, `spacing.8` vertical.

## Colour
- Surface: `surface.contrast` (always-dark floating surface, reads on any background).
- Text: `text.inverted`.

## Variants

| Variant | Use | Accent |
|---------|-----|--------|
| Default | General system actions ("Copied to clipboard.") | — |
| Success | Successful actions ("Changes saved successfully.") | `feedback.success` |
| Error | Denied actions ("Unable to edit because of limited access rights.") | `feedback.error` |
| Warning | Actions with consequences ("The overlay '…' was deleted.") | `feedback.warning` |
| Helpful Tips | Suggestions / guidance ("Hold down 'Ctrl' to add a new arrowhead.") | `accent.primary` |
| With Action | Any of the above plus one text action ("Undo") | inherits |

Forms: single line, with icon, or with cancel/action.

## Rules
- Maximum 2 lines of text; one action maximum.
- Disabled = 40% opacity. Semantic tokens only.
