# Card

Cards present content entries inside a module pane. Clicking a card opens a **detailed view** — cards do **not** offer an expanded inline view, since that adds little informational value and costs the same number of clicks as the detailed view.

## Dimensions & padding
- Horizontal padding: `spacing.16` (16px).
- Default vertical padding: `spacing.16`; use `spacing.12` only when vertical space is essential.

## Colour
- Surface: `surface.subtle`; border `border.default`.
- Active selection: `accent.primary` (the **only** sanctioned use of accent on a card — header icons are intentionally left un-tinted, per the 60-30-10 rule).
- Title `heading-06` `text.default`; supporting text `body-short-02` `text.muted`.

## Interplay (Search Bar + Action Bar + Cards)
When used together — which is most of the time — the order is always:
**1. Search Bar → 2. Action Bar → 3. Cards**, with `spacing.8` then `spacing.4` separating them.

## Rules
- Reserve `accent.primary` for active selection only.
- Disabled = 40% opacity. Semantic tokens only.
