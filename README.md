# IBL bioinformatics wiki document co-authoring

Address:

https://docs.ibl.bio
https://bioinfo.ibl.bio
https://ibl-bioinformatics-wiki.readthedocs.io

Source files for the documentation are markdown (`*.md`) files in `docs/source/`.

The `docs_archive/` folder contains pages that were removed from the active documentation. When removing a page, move it there and try to preserve the original folder hierarchy (not strictly required for old content).

For markdown syntax and special syntax for MyST (our markdown parser), please check:

https://myst-parser.readthedocs.io/en/latest/intro.html

## How to contribute

This project uses **pull requests (PRs)** for all contributions: a PR is a proposal to merge your branch changes into `main`, where it will be reviewed before merging. Before writing a single line, start from the Issues section.

This project is built with [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html), a documentation generator that converts plain text source files into output documents. Here it converts markdown files into HTML.

### Before you start: find or create an issue

1. Search the [Issues](https://github.com/IBL-bioinfo/IBL-bioinformatics-wiki/issues) page to see if a relevant issue already exists.
2. If it does, join the discussion. If not, open a new issue describing what you want to add or change.
3. If you plan to work on an existing page, describe what you intend to change and mention (`@username`) the previous author so they are aware.
4. Assign yourself to the issue so others know it is in progress.
5. As a guideline, try to open your first draft PR within 1–2 weeks of self-assignment.

### Set up your local environment

Make sure you have a Python environment, then install dependencies from the canonical file:

`pip install -r docs/requirements.txt`

If dependencies need to change, update that file first.

You can write `.md` files without building locally, but a local build is recommended before opening a PR.

Clone this repository (or your fork) to your local machine. Alternatively, you can open a GitHub Codespace directly from the repository page, which provides a ready-to-use cloud environment with all dependencies pre-installed.

### Contribution pipeline

Check [this page](https://www.freecodecamp.org/news/a-simple-git-guide-and-cheat-sheet-for-open-source-contributors/) for Git basics. Following is our recommended workflow.

#### 1. Choose your contribution workflow

- External contributors: use [**fork + pull request**](#external-contributors-fork--pr).
- Internal contributors (with write access to this repository): use [**branch in this repository + pull request**](#internal-contributors-branch-in-main-repo--pr).

Both workflows lead to the same result: a pull request that can be reviewed and merged. Work on branches within the main repository allows other internal contributors to work on the same branch if needed, while the fork workflow is more isolated. Choosing the forked workflow means you are the only one with write access to your branch, you are responsible for taking care of any possible review feedback until approval. But that is the standard way for external contributions and is perfectly fine.

##### External contributors (fork + PR)

1. Fork this repository.
2. Clone your fork locally (or open a Codespace).
3. Create a feature branch. The recommended way is to use the **"Create a branch"** button on the GitHub issue page — this auto-generates a descriptive name with the issue number and links the branch to the issue. Alternatively, create it locally:
   `git checkout -b your-branch-name`
4. Ensure remotes are correct:
   - `origin`: your fork
   - `upstream`: `https://github.com/IBL-bioinfo/IBL-bioinformatics-wiki.git`
5. Keep your branch updated as needed:
   `git pull upstream main`
   - If this fails, see [When `git pull upstream main` fails](#when-git-pull-upstream-main-fails).
6. Commit and push your changes:
   - `git add path/to/your.md`
   - `git commit -m "your commit message"`
   - `git push --set-upstream origin your-branch-name` (first push only)
7. Build and verify locally (see [Build and preview locally](#build-and-preview-locally)).
8. Open a pull request from your fork branch to **this repository's** `main` branch.

##### Internal contributors (branch in main repo + PR)

1. Clone this repository locally (or open a Codespace).
2. Create a feature branch. The recommended way is to use the **"Create a branch"** button on the GitHub issue page — this auto-generates a descriptive name with the issue number and links the branch to the issue. Alternatively, create it locally:
   `git checkout -b your-branch-name`
3. Work on your changes, then commit and push to this repository.
4. Build and verify locally (see [Build and preview locally](#build-and-preview-locally)).
5. Open a pull request from your branch to `main`.

#### 2. Work on your contribution

Whether you are **creating a new page** or **updating an existing one**, the process is the same: edit the relevant `.md` file in `docs/source/` and commit your changes.

Write content using MyST markdown syntax ([syntax reference](https://myst-parser.readthedocs.io/en/latest/intro.html)). MyST is mostly standard markdown — if you know markdown, you already know most of it. It adds a few extra features such as directives (e.g. `{toctree}`, `{note}`, `{code-block}`) and cross-reference roles that are useful for structured documentation. If you are writing a tutorial, make sure it is understandable for your target audience and test it in relevant environments. The [Quick special markdown reference](#quick-special-markdown-reference) below may help with this.

**Commit message conventions:**

Keep commit messages clear and descriptive:
- Use the imperative mood: "Add documentation" instead of "Added documentation"
- Start with a verb: Add, Update, Fix, Remove, Refactor, Reorganize
- First line should be under 50 characters when possible
- Include the issue number if applicable: `Add feedback section (fixes #42)`
- Example: `git commit -m "Add <tool> installation troubleshooting guide (fixes #18)"`

If you created a new page, do one of the following to make it reachable:

1. If your page belongs to an existing major topic, add its path (relative to `docs/source/index.md`) to the relevant `{toctree}` section.
2. If your page introduces a new major topic, create a new `{toctree}` section in `docs/source/index.md`. Also add this block in your page (preferably near the top):

   ````
   ```{toctree}
   ---
   #caption: Table of contents
   maxdepth: 3
   ---
   ```
   ````

3. If you intentionally keep the page as an orphan page (not in any toctree), add MyST metadata so Sphinx does not warn, and make sure at least one other page links to it.

#### 3. Build and preview locally

Build HTML locally to verify formatting and preview changes in a browser:

1. Go to the docs directory: `cd docs`
2. Build: `make html` (or `.\make.bat html` on Windows)
3. Start a local web server from `docs/build/html`: `python -m http.server`
4. Open `http://localhost:8000` in your browser
5. Re-run `make html` (or `.\make.bat html` on Windows) after edits. You can keep the same local server running and just refresh the browser to see updates.

Once you are satisfied, commit your changes on your branch. It is good practice to update your branch with the latest `main` before opening your PR (steps below).

#### 4. Update your branch with latest `main`

Use one of these approaches before opening your PR:

1. Merge-based update (simpler):
   - `git fetch upstream`
   - `git checkout your-branch-name`
   - `git merge upstream/main`
2. Rebase-based update (linear history):
   - `git fetch upstream`
   - `git checkout your-branch-name`
   - `git rebase upstream/main`

If you get conflicts, resolve files, then continue:

- For merge: `git add <resolved-files>` then `git commit`
- For rebase: `git add <resolved-files>` then `git rebase --continue`

Push updates after merge/rebase:

- Merge: `git push`
- Rebase: `git push --force-with-lease`

#### 5. Open a pull request (PR)

Quick checklist **before opening your PR**:

- Review the related issue again, make sure your changes satisfy what the issue describes.
- The page builds successfully with `make html` (or `.\make.bat html` on Windows) and looks good in the local preview.
- New pages are added to a relevant `{toctree}` (or marked as orphan intentionally).
- At least one link points to each new page (either from another page or from the index).
- Formatting and links were checked in local preview.
- **Your name is listed as an author at the top of every page you created or significantly edited.** Don't be shy — credit matters. It will be reviewed to preserve contributions from previous writers.

When everything looks good, push your branch, go to your branch on GitHub, and create a pull request. Please request a review from at least one other contributor (e.g. the issue author or a previous page author) to ensure your changes are reviewed by someone familiar with the content.

#### 6. Review and merge

Your PR will be reviewed by maintainers and possibly other contributors. You may receive feedback or requests for changes — this is normal and part of the collaborative process. Address any feedback by making more commits to your branch, which will automatically update the PR.

After your pull request is approved and merged (by yourself or a maintainer), the documentation rebuilds and publishes automatically.

### When `git pull upstream main` fails

Common causes are local uncommitted changes, conflicts, or divergent history.

Recommended recovery:

1. Check status: `git status`
2. Commit or stash local changes:
   - Commit: `git add -A && git commit -m "WIP: save local work"`
   - Or stash: `git stash`
3. Fetch and update explicitly:
   - `git fetch upstream`
   - `git merge upstream/main` (or `git rebase upstream/main`)
4. If you used stash, restore changes: `git stash pop`

If the error is unclear, copy the full terminal output into an issue or PR comment and ask for help.

## Quick special markdown reference

Practical syntax snippets for (un)common formatting needs. All examples come from existing pages in this repository.

### Images

**Simple inline image** (markdown standard):

```markdown
![Alt text describing the image](../_static/images/your-image.png)
```

**Image with controlled size** (MyST `{image}` directive):

````markdown
```{image} ../_static/images/your-image.png
:alt: Description of the image
:width: 30em
```
````

**Tiny inline icon** (HTML, for small inline images where size matters):

```html
<span><img alt="icon description" src="../_static/images/icon.png" width="24"></span>
```

**Image with a solid background colour** (useful for PNG/SVG with transparent backgrounds that look broken in dark themes — apply a background matching the logo's intended colour):

```html
<span style="background-color:#3568b4;padding:0.2rem;border-radius:3px;display:inline-flex;align-items:center;justify-content:center;width:32px">
  <img src="../_static/images/logo_white.svg" alt="Logo">
</span>
```

Note: the Sphinx `{image}` directive does not support the `style` attribute, so HTML `<span>` wrapping is necessary for background colour control.

### Call-outs (admonitions)

**Built-in types** (`note`, `warning`, `tip`, `important`) — simplest form:

````markdown
```{note}
This is a note.
```
````

````markdown
```{warning}
This is a warning.
```
````

**Custom title** (use `{admonition}` with any title you like):

```markdown
:::{admonition} Your custom title
The body of the call-out goes here.
:::
```

**Custom title with a styling class** (applies the visual style of a built-in type):

````markdown
```{admonition} Your custom title
:class: warning
Body text here.
```
````

Available classes: `note`, `warning`, `tip`, `important`, `hint`, `caution`, `danger`, `info`.

**Linking to a call-out** — place a named anchor inside the admonition, then link to it:

```markdown
:::{admonition} It is normal to have zero space
(you-do-not-own-space)=
Body text here.
:::
```

Then link from anywhere on the same page:

```markdown
[see explanation](#you-do-not-own-space)
```

Note: anchor labels placed inside admonitions are intentional — the `(label)=` tag will not render as visible text or affect the admonition's style.

### Custom link anchors

By default, every heading is automatically linkable using its text in lowercase with spaces replaced by hyphens:

```markdown
[link text](#your-section-title)
```

For cross-page links:

```markdown
[link text](./other-page.md#your-section-title)
```

When you need a stable anchor independent of the heading text (e.g. the heading may change, or you want to target a non-heading element), place a named anchor explicitly with `(anchor-name)=` on the line immediately before it:

```markdown
(create-ssh-key-pair)=
### 1. Create ssh key pair
```

Link to it from the same page:

```markdown
[Create SSH key pair](#create-ssh-key-pair)
```

Link to it from a different page:

```markdown
[Create SSH key pair](./ssh-access-command-line.md#create-ssh-key-pair)
```

Anchor names must be lowercase, use hyphens instead of spaces, and be unique within the entire documentation build.
