# Notification

Contextual alert panels in two families — **Notification Card** (panel-style, no external border) and **Notification Toast** (bordered, floating). Three severity types, collapsed/expanded/hover states, and a 20px dismiss button. Width 400px.

## Severity types

| Type | Background | Accent bar | Accent fill |
|------|-----------|-----------|------------|
| Info | transparent | none | — |
| Warning | `color.yellow.10` (#FEF8D2) | none | — |
| Critical | `color.red.5` (#FEE5E5) | 8px left bar | `semantic.feedback.error` (red.60) |

Critical is the only type with the 8px absolute-positioned accent bar on the left edge, spanning the full card height.

---

## Notification Card

400px wide, no external border. Padding `spacing.16`. Content width = 368px.

### Anatomy
1. **Source attribution** (368×20) — workspace / module name. `font-s-400`, `semantic.text.subtle`.
2. **Notification content** (368×64):
   - Timestamp — `font-s-400` (14/20), `semantic.text.default`
   - Title — `font-s-400`, `semantic.text.default`. Max 1 line.
   - Description — `font-s-400`, `semantic.text.subtle`. Max 2 lines.
3. **Buttons** (32px, right-aligned):
   - Secondary action e.g. "Options" — Outlined, `semantic.border.strong`
   - Primary action e.g. "Acknowledge/Dismiss" — Danger, `semantic.feedback.error`

> Note: the primary action button uses the Danger style (red.60 fill) consistently across all severity types — signalling that acting on or dismissing a notification is a deliberate, irreversible action.

### States
| State | Height | Notes |
|-------|--------|-------|
| Default | 124px | content visible, buttons hidden |
| On-hover | 172px | expands to reveal footer buttons |

### Collapsed card (grouped notifications)
A container stacking multiple notification cards under a banner header.
- **Banner** (400×32): fill `semantic.surface.pressed` (grey.20), radius `radius.8` top corners only [8,8,0,0]. Leading icon + source name (bold, `semantic.text.default`).
- **Stacked cards** below (Critical + Info cards nested, no gap, shared left edge).
- Hover state expands height from 194 → 242px.

### Expanded card
Full detail view (400×420). All content + an expanded body area with additional detail rows.

---

## Notification Toast

Same content anatomy as the Notification Card, with an additional external border and explicit radius.
- Border: 1px `semantic.field.borderFilled` (grey.35)
- Radius: `radius.8` (all corners)
- Background: same type-based tint (transparent / yellow.10 / red.5)
- Hover state: 410×184px (width extends 10px on hover — allow room in layout)

---

## Notif Cancel (dismiss button)
A 20×20 icon button for dismissing individual notifications.
| State | Appearance |
|-------|-----------|
| Default | transparent bg |
| Hover | subtle bg |
| On Click | pressed bg |

---

## Rules
- Critical uses both a tinted background (`red.5`) AND an 8px left accent bar (`feedback.error`) for maximum visual prominence.
- Warning uses only the tinted background (`yellow.10`) — no accent bar.
- Info uses no tint or accent bar — reads as a neutral informational message.
- Buttons always right-align; footer only visible on hover.
- Collapsed cards stack with no gap; the banner header uses only top corner radius so the transition to flat stacked cards is seamless.
- Semantic tokens only. The `yellow.10` and `red.5` fills are deliberate primitive references (lightest tint steps).
