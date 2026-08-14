# Choose how to move your data

*By C.Du [@snail123815](https://github.com/snail123815)*

There are several ways to get data in and out of Research Drive, and picking the wrong one is the
most common reason a transfer takes days or fails halfway. This page is the decision point; each
method has its own page with the actual steps.

```{contents}
---
depth: 3
---
```

## Which method?

| Your situation | Use this |
|---|---|
| Files already on your computer | The [Nextcloud desktop client](./ResearchDrive_setup.md) — drop them in the synced folder |
| Large data on a mapped network drive (for example `J:`) or USB storage | A [temporary sync connection](./ResearchDrive_uploadFromNetworkDrive.md), so the data never has to fit on your own disk |
| You are on an IBL server or ALICE, or cannot install the desktop client | [`rclone` on the command line](./ResearchDrive_commandLine.md) |
| You prefer working in a terminal on your own Linux or macOS machine | [`rclone`](./ResearchDrive_commandLine.md) works there too |
| You want to script or schedule the transfer | [`rclone`](./ResearchDrive_commandLine.md), optionally with the `sync-with-rclone` wrapper |
| Anything large, through the browser | Don't — see below |

:::{admonition} Web interface uploads are unreliable for anything large
Web interface uploads usually have a **file size limit** and can **time out** for large files or a
large number of small files. The transfer also depends on the stability of your internet
connection and of your browser. Once stopped, you have to start over from the beginning — the same
applies to downloads.

Use the [desktop client](./ResearchDrive_setup.md) or
[`rclone`](./ResearchDrive_commandLine.md) instead.
:::

If you cannot use the desktop client and cannot use a terminal, two GUI front-ends for `rclone`
exist: [RcloneView](https://rcloneview.com/) (not for university computers) and the
[Rclone GUI](https://rclone.org/gui/).

## Before you start a large transfer

**Check that you have the capacity.** Compare the size of what you are about to upload against
your quota, and be aware that the numbers shown are not always in the units you expect — see
[Storage space and quota](./ResearchDrive.md#storage-space-and-quota). If you need more space, your
PI or lab manager can [request it](./ResearchDrive_admin.md#expand-storage-space).

:::{admonition} Sizes are also not accurate between local and remote
Due to differences between file systems, the sizes on your own system may not match the sizes
shown on Research Drive.
:::

**Setting up the desktop client for the first time?** Allow about an hour of uninterrupted,
powered-on time for the initial sync to finish — see
{ref}`Before you start: allow about an hour for the first sync <first-sync-takes-time>`.

**Reduce the number of small files.** Large numbers of small files are far more expensive to store
and transfer than a few large ones: each file needs its own metadata operations and network
requests, which is why a folder of thousands of tiny files can take hours. Create ZIP or TAR
archives before uploading. For easier searching, keep a separate copy of human-readable results
outside the archives.

Do not upload dependency or cache directories at all — `node_modules`, virtual environments, conda
environments. They are the worst case for this (very many small files, deeply nested) and they can
be regenerated. See
[Windows long path compatibility issue](./ResearchDrive_troubleshooting.md#windows-long-path-compatibility-issue).

## After the transfer

Confirm the files are there before deleting anything from the source. If a transfer reported
errors, check
[Common issues and troubleshooting](./ResearchDrive_troubleshooting.md) before retrying.
