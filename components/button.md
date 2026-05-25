# Button (UX 2.0 additions)

> This extends the existing `button.md`. It adds the **Alert** variant and the **size scale** from the UX 2.0 master. Merge into the existing spec; do not duplicate variants already documented (Primary, Outlined, Icon, Ghost).

Buttons are the primary call-to-action on a page. The system is a matrix of **size × variant × content × state**.

## Variants
Primary · Outlined · Icon · Ghost · **Icon + Text** · **Loading** · **Alert**.

- **Icon + Text** — secondary CTA for stand-alone actions ("New", "Edit") not in an action bar; usually styled as outlined. More than one allowed per page.
- **Loading** — feedback after a press, to show the action's result is in progress.
- **Alert** — for warnings or high-criticality actions. Three styles (contained / outlined / ghost). Colours follow system feedback tokens:
  - **Critical** → `feedback.error` (red)
  - **Warning** → `feedback.warning` (amber)

## Size scale

| Size | Width | Height | V-pad | H-pad | Radius |
|------|-------|--------|-------|-------|--------|
| Default | 100px [variable] | 40px | 10px | min 12px | `radius.8` |
| Small | min 80px [variable] | 32px | 6px | min 12px | `radius.8` |
| Icon (default) | 40px | 40px | — | — | `radius.8` |
| Icon (small) | 32px | 32px | — | — | `radius.8` |
| Icon (raw) | 24px | 24px | — | — | — |

Icon + Text: icon sits in a 20×20px container with 4px gap to the label.

## States
Default · Hover · On-click · Active · Disabled · Loading — colour changes, geometry does not. (See existing `button.md` for the per-variant state token table.)

## Emphasis / hierarchy
When a layout needs multiple actions, establish clear hierarchy and group related actions. You do not have to use an outlined button as the secondary action — icons and ghost buttons are often better for data tables and dashboards.

## Rules
- One contained Primary (or one Alert) per container where possible.
- Alert colours must match the system's feedback tokens — never a one-off hex.
- Disabled = 40% opacity. Semantic tokens only.
