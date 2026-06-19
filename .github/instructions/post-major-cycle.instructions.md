---
applyTo: docs/source/**/*.md,docs/source/*.md
---

The project is in a stabilization phase after a major development cycle.

- Prefer minimal-risk edits over broad rewrites.
- Do not perform structural refactors (renaming sections/files, moving pages, changing anchors) unless explicitly requested.
- Preserve existing labels/anchors/admonition markers because cross-page links and popup behavior depend on them.
- Keep terminology and style consistent with nearby docs; avoid introducing new naming variants unless requested.
- For branding/icon updates, use local assets under `docs/source/_static/images/` and apply the same change consistently to all matching occurrences.
- For docs builds, always use the project environment: `micromamba run -n ibl-bioinfo-dev`.
- Before opening or updating a PR for docs changes, build HTML with that environment and serve `docs/build/html` locally for preview.
- Pause after serving and wait for explicit user confirmation that the rendered result looks correct before proceeding with PR actions.
