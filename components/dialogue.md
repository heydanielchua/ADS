# Dialogues

A dialogue displays content that requires user interaction in a layer above the system's content. Use it to focus attention, complete a short task, gather input, or display workflow-relevant information.

Dialogues must always be **user-initiated** — they never appear without a specific trigger. If the system auto-generates an alert that is *not* a consequence of a user action, use a **toast** (see `snackbar.md`) instead.

**Do not** use a dialogue to: show content unrelated to the workflow, display complex/large amounts of information, recreate a full page, or appear unprompted.

## Variants

| Variant | Use |
|---------|-----|
| **Modal** | Critical information needing a specific decision/acknowledgement/input to complete a workflow, or blocking errors. Blocks and scrims the rest of the app until completed or dismissed. |
| **Non-modal** | Less critical; does not block the underlying workflow. |
| **Full Screen** | Fills the screen when the user needs the space or a series of tasks (e.g. previewing a map snippet). 1598 × 948px [Fixed], padding `spacing.16`, `radius.10`. |

## Scrim (modal)
Surfaces behind a modal are scrimmed so attention focuses on the dialogue.
- Scrim: `color.black` @ 60%.
- A scrim must stay dark in both light and dark themes, so it anchors to the `black` palette primitive (not a theming surface token).

## Anatomy
- **Title** — a clear statement or question; brief; include the action where possible for context. Avoid apologies ("Sorry for the interruption"), alarm ("Warning!"), and jargon.
- **Supporting description** — elaborates the problem (informational) or explains the impact of the action.
- **Close / Cancel** — an icon button top-right to cancel or defer the decision.
- **Action buttons** — bottom-aligned; the primary action is bolded. Button alignment must be consistent across all dialogues.
- **Icon** (optional) — leading icon for status dialogues.
- Default padding `spacing.16`.

## Surface stacking
There must be **no more than 2 dialogues** stacked above one another.

## Rules
- Always user-initiated; reach for a toast for background/system alerts.
- Title carries the purpose; keep it brief and action-oriented.
- Disabled = 40% opacity. Semantic tokens only.
