# Segmented Control

A compact binary or multi-option switcher. The active segment "lifts" to a white pill inside a neutral track. Used inline within forms and panels. Semantic tokens throughout.

## Anatomy
- **Track**: the outer container. Fill `semantic.control.segmentedTrack` (grey.25 light / grey.80 dark). Radius `radius.8`. Padding `spacing.4` all sides.
- **Segment**: each option fills its share of the track width. Height 28px. Radius `radius.8`. Padding `spacing.4`.

## Segment states
| State | Fill | Text | Weight |
|-------|------|------|--------|
| Active | `semantic.surface.default` (white → black in dark) | `semantic.text.default` | `font-m-600` (semibold) |
| Default (inactive) | transparent | `semantic.text.default` | `font-m-400` (regular) |

The active segment stands out by fill + weight; inactive segments are transparent, showing the track through.

## Sizing
- Track height: 36px (including 4px padding top/bottom). Segment height: 28px.
- Width: responsive — detach and adjust segment widths to content. Kit guidance: maintain `spacing.16` (16px) padding on both sides of the track.
- Gap between segments: `spacing.4`.

## Context
The segmented control is used inside forms and panels as a mode switcher (e.g. "L-Time / Exercise Time"). It is not a navigation tab — use Line or Contained Tabs for navigation.

## Dark mode
- Track flips to `grey.80` (#3A3A3A — a dark trough).
- Active segment flips to `surface.default` dark = black (#000000), lifting darker against the dark track.
- Text stays `text.default` (grey.5 in dark) on both active and inactive.

## Rules
- Use for binary or small-set (2–3) option switching within a form or panel.
- Active = white lift + semibold; inactive = transparent + regular.
- Semantic tokens only; never hard-code hex.
