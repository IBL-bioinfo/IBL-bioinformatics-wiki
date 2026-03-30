# Managing Local Files

*By C.Du [@snail123815](https://github.com/snail123815) & Joost Willemse[@Karivtan](https://github.com/Karivtan)*

In this section, we cover common issues related to managing local files when using Research Drive with the Nextcloud desktop client. This includes understanding how virtual files work, how to free up local disk space, and how to handle large file transfers from network drives.

```{contents}
---
depth: 3
---
```

## Sync taking forever

The reason of sync taking forever can be due to various factors, such as a large number of small files, limited local storage space, or issues with the Nextcloud client. If you are experiencing slow sync times, consider the following troubleshooting steps:

### Check the log

Left-click the Nextcloud icon in the system tray, the log is shown as a list of recent events, ordered by time from newest on top. Look for any error messages or warnings that may indicate the cause of the slow sync.

### Too many small files

When you have a folder with a very large number of small files (for example, thousands or more), syncing can take a very long time. This is due to high per-file overhead: each file requires metadata operations and separate network requests. This increases CPU and disk I/O, bloats the Nextcloud client and server databases, prolongs directory scans and backups, and can cause much slower syncs, timeouts, or sync errors. Antivirus or indexing scans can further degrade performance, and some platforms may hit filesystem limits when directories contain very many entries.

Practical mitigations:

- Archive many small files into ZIP/TAR before uploading to reduce per-file overhead.
- Keep frequently changing tiny files (caches, temp files) in local-only folders rather than in Research Drive.
- Avoid storing dependency/cache directories (for example `node_modules` or virtual environments) in Research Drive.

::: {admonition} This applies to other cloud storage as well
This issue is not specific to Research Drive or Nextcloud; it is a common problem with any cloud storage solution that does not handle large numbers of small files efficiently. The same advice applies to other platforms like OneDrive, Dropbox, Google Drive, etc.
:::

## Space on your local machine

Research Drive uses the Nextcloud desktop client to *sync* files between the **cloud** (Research Drive) and your **local** computer.

When **Virtual files** are enabled (recommended), Windows Explorer or Finder on macOS can show files that exist in the cloud without storing the full data locally.

- Local vs cloud (practical meaning)
  - **Cloud**: The file exists on Research Drive and counts toward your project's storage, even if it is not downloaded to your laptop/PC.
  - **Local**: The file's data is present on your computer and consumes disk space.

You can think of "virtual files" as shortcuts/placeholders: they show up in Explorer or Finder so you can browse/search, but the content is only downloaded when you open it.


:::{admonition} Virtual files and "Choose what to sync" are mutually exclusive
(choose-what-to-sync-are-mutually-exclusive)=
The "Choose what to sync" option allows you to select specific folders to sync locally, but it is not compatible with virtual files. If you enable "Choose what to sync", you will lose the virtual file functionality, and all files in the synced folders will be downloaded to your local machine. Therefore, it is recommended to keep "Choose what to sync" disabled and use virtual files to manage your storage efficiently.
:::

### Windows "Properties" can show two different sizes

On Windows, right-click a file/folder → **Properties**. You may see:

- **Size**: the *logical* size of the file(s) (how much data it is in total).
  - Large, showing the real file size in the cloud.
- **Size on disk**: the *physical* space currently used on your local drive.
  - Zero or very small with virtual files, only metadata/placeholder data stored locally.

![Property window when virtual files are enabled](../_static/images/nextcloud_virtual_files.png)

After you open a file (or mark it to keep offline), Windows downloads it and **Size on disk** will increase accordingly.

::: {admonition} Secure local space before opening
If you do not have enough space for the file you are opening, Nextcloud will try to reclaim space by converting downloaded local files to cloud. If it is not successful, it will report a corresponding error.
:::

### Free up space (Windows)

If your local disk is getting full, you can remove local copies while keeping the files in Research Drive.

Common options in Windows Explorer (wording may vary slightly by Nextcloud client version):

1. In the synced Research Drive folder, right-click a file or folder.
2. Choose **Free up space**.
3. Sometimes the **Free up space** option is unavailable. This usually means **the selected file or folder** is already online-only (stored only in the cloud), so there is no local copy to remove. You can check the properties to confirm.

![Free up space](../_static/images/nextcloud_take_too_much_space.png)

This converts downloaded files back to online-only (virtual) files:

- The data stays in Research Drive (cloud).
- The file remains visible in Explorer.
- Disk space is freed on your computer.

## Transfer large files from network drive

Transferring large files located on a network drive (for example, `J:`) to the cloud may require some extra steps.

Uploading files usually involves three steps:

1. Copy/move local files into the synced folder.
2. Nextcloud uploads these files to ResearchDrive (or other cloud storage).
3. If the files are not used, or if local storage is full, Nextcloud removes the local copies and replaces them with "virtual files".

If you have large files located on your network drive, the first step can be difficult because you may not have enough local storage to hold them temporarily.

**Choose one of the following**:

1. Recommended: [**Add** an additional sync folder, then **remove** the sync after uploading](./ResearchDrive_uploadFromNetworkDrive.md)
2. [RcloneView](https://rcloneview.com/) software (not for university computers)
3. [Rclone GUI](https://rclone.org/gui/)

## Removing a shared folder or file

In Research Drive, you **cannot delete folders** shared with you from your computer. This can only be done by using the "Leave this share" option in the \[**&middot;&middot;&middot;**\] menu in the web interface.

![leave this share button](../_static/images/nextcloud_leave_share.png)

However, deleting a shared **file** is **possible**. It does **not** delete it from the cloud — it removes **your** share (i.e., you leave the share by deleting the file). To regain access, you need to contact the person who originally shared it with you.

::: {admonition} Non-destructive, but non-reversible
:class: warning
When you delete a shared file or leave a shared folder, it is not deleted from the cloud, but it is also not recoverable from your side. You will lose access to that file or folder unless the original sharer (ISSC for project folders) shares it with you again. Therefore, be cautious when deleting shared files, as it can lead to loss of access to important data.
:::

## Windows long path compatibility issue

On Windows, file paths can become too long for the operating system or for specific applications. Even on recent Windows versions, many tools still fail when the full path length approaches the legacy limit ([260 characters](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation)). When this happens, files may not sync correctly and may not be usable locally.

```{warning}
If Windows cannot create a folder/file locally due to path length, the Nextcloud/Research Drive client cannot store it either. You may see sync errors.
```

### Common scenarios where files cannot be stored (or synced)

- Deep folder nesting (many subfolders), especially when the local sync folder is already long (for example under `C:\RD`).
- Very long filenames, or filenames generated by software exports (for example, long sample IDs + many parameters in the name).
- Extracting archives (ZIP/TAR) into a synced folder: the extracted structure is often deeper than expected.
- Cloning software repositories into Research Drive (for example, projects containing `node_modules`, `venv`, `conda` environments, or other dependency trees).
- Workflows that auto-generate deeply nested output directories.

### How to reduce the risk

- Use a short local sync root path (for example `C:\Users\<name>\RD` or simply `C:\RD` (if you are not sharing this computer with others) instead of a long path).
- Avoid unnecessary nesting; keep project folder structures shallow.
- Shorten filenames where possible; avoid encoding too much metadata in the name. Keep the metadata in a separate file when necessary.
- **Do not store dependency folders or full software environments in Research Drive**; keep those local.
- If you are on a managed university device and need Windows long path support enabled, contact ICT/ISSC. Enabling it typically requires admin rights, and note some applications still ignore the setting or report error while reading those files.
