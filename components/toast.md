# Toast

Transient notification banners. Four semantic types — all share the same **always-dark surface**, differing only in their icon. Width min 432 / max 553px. Semantic tokens throughout.

## Anatomy
- **Background**: `semantic.surface.contrast` (grey.100 light / grey.5 dark — always a dark/inverted surface regardless of page theme)
- **Border**: 2px `semantic.text.inverted` (grey.5 off-white) inside edge
- **Shadow**: `shadow.prominent` (4px 4px 4px rgba(0,0,0,0.5) — stronger than shadow.default/elevated to float above content)
- **Radius**: `radius.8`
- **Padding**: `spacing.16` all sides
- **Layout**: horizontal, gap `spacing.8`

| Part | Token |
|------|-------|
| Background | `surface.contrast` |
| Border | `text.inverted` (2px inside) |
| Shadow | `shadow.prominent` |
| Text | `text.inverted` |
| Icon | type-specific (see below) |

## Types
The icon is the only differentiator between types. Background, border, and text are identical.

| Type | Icon | Semantic feedback token |
|------|------|------------------------|
| Success | ✅ success icon | `semantic.feedback.success` |
| Warning | ⚠️ warning icon | `semantic.feedback.warning` |
| Error | ❌ error icon | `semantic.feedback.error` |
| Tips | ℹ️ info icon | `semantic.feedback.info` |

Icon size: 24px (from `icon.size.xs`).

## Text
- Style: `font-m` (16 / 22), `semantic.text.inverted`
- Max 2 sentences. Target 50–70 characters per line for 1–2 second scannability.

## Optional close button
A dismiss (×) icon button is included in the component but hidden by default. Make visible when the toast should be manually dismissible.

## Rules
- Toasts always use `surface.contrast` — they appear as dark banners regardless of light or dark page theme.
- Copy must be brief: max 2 sentences, scannable in 1–2 seconds.
- Use the appropriate type icon so the semantic meaning is clear at a glance.
- Width: min 432px, max 553px. Semantic tokens only.
