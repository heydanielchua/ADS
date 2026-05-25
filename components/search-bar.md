# Search Bar

The Search Bar lets users find content easily. A search bar should always be present on pages with multiple sections, cards, or options. It is the first element in a module pane (Search → Action → Cards).

## Dimensions
- Width: variable
- Height: 40px [Fixed]
- Padding: `spacing.8` (8px)

## Variants

| Variant | Behaviour |
|---------|-----------|
| Normal Search | Filters content on the current page by free-text. |
| Filter Search | Filters the current page by specified types. |
| Spotlight Search | Searches across pages and modules system-wide by free-text; results vary in format. |

## States
Default · Hover · On-click (placeholder → "Enter a keyword") · Open/Hover (shows results list) · No results.

Filter Search adds Open/Hover/Selected-Filter and Active-Filter states (filter chips above the result list).

## Colour
- Field background `field.bg`; placeholder `field.placeholder`.
- Underline `border.strong` at rest → `border.focus` when active or filled.
- Text `body-short-01` `text.default`.

## Rules
- Result rows follow the shared 40px menu-row pattern (`spacing.16` horizontal padding, surface scale subtle → hover → pressed).
- Disabled = 40% opacity. Semantic tokens only.
