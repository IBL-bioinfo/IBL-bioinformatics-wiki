# Using GitHub or GitLab in Research

*By C.Du [@snail123815](https://github.com/snail123815)*

GitHub and GitLab are powerful platforms for version control and collaboration on code. In our context, GitHub is often the practical choice for public repositories and collaboration with people outside Leiden University, while the university-hosted [GitLab service](https://gitlab.services.universiteitleiden.nl/) is the preferred option for projects related to personal data or other work that should stay within the university environment. The university GitLab is listed in the [VRE service overview](https://lab.library.universiteitleiden.nl/vre/#gitlab).

However, Git itself and these hosting platforms are designed to track **code and text files** — not all types of research output. There are restrictions on file sizes (for example, GitHub blocks files over 100 MB), and they are not suited for storing (temporary) results, large datasets, or binary files.

The university GitLab also does **not** allow sharing repositories externally. That makes GitHub the better solution when you need external collaborators, public visibility, or GitHub-specific services such as the GitHub to Zenodo release workflow.

This means that **even for bioinformatics students**, an [Electronic Lab Notebook (ELN)](./ELN.md) is still essential. The ELN captures the full research context that Git cannot: the reasoning behind decisions, experimental results, links to data files, and the relationship between code and outcomes.

```{contents}
---
depth: 3
---
```

## What Git tracks and what it does not

| Tracked well by Git | **Not** suited for Git |
| --- | --- |
| Source code and scripts | Large data files and databases |
| Plain-text configuration files | Binary result files (images, PDFs, compressed archives) |
| Documentation in Markdown/text | Temporary or intermediate results |
| Commit history and diffs | Repository-level operations (renames, transfers) |

Because of these limitations, you should use Git and ELN **together** as complementary tools.

## Recommended workflow

### 1. Starting a GitHub or GitLab repository

When you create a new remote Git repository for your project:

- Choose the platform deliberately:
  - For projects related to personal data or internal university-only collaboration, prefer the university GitLab at [gitlab.services.universiteitleiden.nl](https://gitlab.services.universiteitleiden.nl/).
  - For projects that need external collaborators, public sharing, or later public release workflows, use GitHub.
- Create the repository on the chosen platform (or ask your supervisor to create it within the relevant group or organisation).
- In your ELN, create a new entry or page for this project. Record:
  - The **purpose** of the repository (what the code is for).
  - The **link** to the GitHub or GitLab repository.
  - Which platform you chose, and why.
  - Who has access and their roles.
- Do not just start coding with a local Git repository without linking it to GitHub or GitLab. The remote repository is important for collaboration and long-term tracking.

### 2. Recording major repository operations in ELN

Some operations are **not tracked by Git** itself. Record these in your ELN whenever they happen, including the reasoning:

- Repository **name changes**.
- **Transferring** content or history between repositories.
- Changes to repository **visibility** (public/private).
- Adding or removing **collaborators** or changing permissions.
- Major **branch strategy** decisions (e.g. creating a long-lived branch for a specific experiment).

### 3. Recording test runs and results in ELN

Every time you do a test run or generate results:

- Write a brief **description** of what you ran and why (e.g. parameter changes, input data used).
- Store the result files on [Research Drive](./ResearchDrive.md) and include the **link to the files** in your ELN entry.
- Note which **commit or version** of the code was used (copy the commit hash or tag).

This is crucial because intermediate results, figures, and output files are not recorded by Git versions.

If you sync project folders to Research Drive from the command line, the [sync-with-rclone wrapper](./ResearchDrive_commandLine.md#simplified-rclone-wrapper) is especially useful for GitHub- or GitLab-based workflows. Its git repository tracking feature writes a small summary file with the current commit, configured remotes, and git status while excluding the `.git` directory itself, so the copy stored on Research Drive still keeps a clear reference to the remote repository state that produced the uploaded results.

This repository summary is a useful reference in Research Drive, but it does not replace your ELN entry or the GitHub/GitLab remote repository.

### 4. Making a release and submitting to Zenodo

After the project is completed (e.g. paper published, thesis submitted):

1. If you need a public archived software release, create a **release** on GitHub and tag it with a version number (e.g. `v1.0.0`). If the active development repository is on university GitLab, prepare a suitable GitHub repository for the public release first.
2. Submit the GitHub release to **[Zenodo](https://zenodo.org/)** to obtain a DOI. Zenodo requires a GitHub release to create an archive. See [GitHub's guide on Zenodo integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).
3. Record in your ELN the release version, platform, date, and the Zenodo DOI link.

### 5. Archiving the release on Research Drive

- Download the release zip from GitHub (or let Zenodo create it).
- Upload the zip to [Research Drive](./ResearchDrive.md) in the appropriate project folder.
- Record the **link to the zip file** on Research Drive in your ELN.

This ensures long-term preservation of the code alongside your data, independent of GitHub or GitLab availability.

## Summary

```{list-table}
:header-rows: 1

* - When
  - What to record in ELN
* - Repository created
  - Purpose, link to repo, chosen platform and reasoning, access info
* - Major repo operations
  - Name changes, transfers, permission changes, with reasoning
* - Each test run
  - Description, code version (commit hash), link to results on Research Drive; if using `sync-with-rclone`, keep the generated git repository summary file
* - Project completed
  - Release version, platform, Zenodo DOI
* - Release archived
  - Link to release zip on Research Drive
```
