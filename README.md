# IBL bioinformatics wiki document co-authoring

Address:

https://ibl-bioinformatics-wiki.readthedocs.io/index.html

Source files for the documentation are markdown (`*.md`) files in `docs/source/`.

The `docs_archive/` folder contains pages that were removed from the active documentation. When removing a page, move it there and try to preserve the original folder hierarchy (not strictly required for old content).

For markdown syntax and special syntax for MyST (our markdown parser), please check:

https://myst-parser.readthedocs.io/en/latest/intro.html

## How to make changes

This project uses **pull requests (PRs)** for all contributions: a PR is a proposal to merge your branch changes into `main`, where it will be reviewed before merging. Before writing a single line, start from the Issues section.

This project is built with [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html), a documentation generator that converts plain text source files into output documents. Here it converts markdown files into HTML.

### Before you start: find or create an issue

1. Search the [Issues](https://github.com/IBL-bioinfo/IBL-bioinformatics-wiki/issues) page to see if a relevant issue already exists.
2. If it does, join the discussion. If not, open a new issue describing what you want to add or change.
3. If you plan to work on an existing page, describe what you intend to change and mention (`@username`) the previous author so they are aware.
4. Assign yourself to the issue so others know it is in progress.
5. As a guideline, try to open your first draft PR within 1–2 weeks of self-assignment.

### Choose your contribution workflow

- External contributors: use **fork + pull request**.
- Internal contributors (with write access): use **branch in this repository + pull request**.

### Prerequisites

Clone this repository (or your fork) to your local machine. Make sure you have a Python environment, then install dependencies from the canonical file:

`pip install -r docs/requirements.txt`

`docs/requirements.txt` is the single source of truth for documentation build dependencies. If dependencies need to change, update that file first.

(You can write `.md` files without building locally, but a local build is recommended before opening a PR.)

### General pipeline

Check [this page](https://www.freecodecamp.org/news/a-simple-git-guide-and-cheat-sheet-for-open-source-contributors/) for Git basics. Following is our recommended workflow.

#### External contributors (fork + PR)

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
8. Open a pull request from your fork branch to this repository's `main` branch.

#### Internal contributors (branch in main repo + PR)

1. Clone this repository locally (or open a Codespace).
2. Create a feature branch. The recommended way is to use the **"Create a branch"** button on the GitHub issue page — this auto-generates a descriptive name with the issue number and links the branch to the issue. Alternatively, create it locally:
   `git checkout -b your-branch-name`
3. Work on your changes, then commit and push to this repository.
4. Build and verify locally (see [Build and preview locally](#build-and-preview-locally)).
5. Open a pull request from your branch to `main`.

#### How to work on your contribution

Create a markdown `.md` file for your topic and write content using MyST markdown syntax: [syntax reference](https://myst-parser.readthedocs.io/en/latest/intro.html). If you are writing a tutorial, make sure it is understandable for your target audience and test it in relevant environments.

After you add a page, do one of the following:

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

### Build and preview locally

Build HTML locally to verify formatting and preview changes in a browser:

1. Go to the docs directory: `cd docs`
2. Build: `make html`
3. Start a local web server from `docs/build/html`: `python -m http.server`
4. Open `http://localhost:8000` in your browser
5. Re-run `make html` after edits. You can keep the same local server running and just refresh the browser to see updates.

Once you are satisfied, commit your changes on your branch. It is good practice to update your branch with the latest `main` before opening your PR (steps below).

### Update your branch with latest `main`

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

### Before opening a PR

Quick checklist:

- Review the related issue again, make sure your changes satisfy what the issue describes.
- The page builds successfully with `make html`.
- New pages are added to a relevant `{toctree}` (or marked as orphan intentionally).
- At least one link points to each new page (either from another page or from the index).
- Formatting and links were checked in local preview.

When everything looks good, push your branch and create a pull request.

After your pull request is approved and merged, the documentation rebuilds and publishes automatically.

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
