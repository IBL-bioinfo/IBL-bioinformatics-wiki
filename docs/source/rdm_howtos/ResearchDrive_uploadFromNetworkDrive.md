# Upload Large Files to ResearchDrive

*By C.Du [@snail123815](https://github.com/snail123815)*

For anything you can put on your local drive, the Nextcloud client handles the upload nicely. However, large files usually located on a **mapped network drive (e.g., `J:`)** or **USB storage device**, and they are usually too large to fit on your local drive.

This guide focuses on using the **Nextcloud desktop client** to upload large files by **setting up a temporary sync connection**. If you don't have the client installed, please follow the instructions in the [Nextcloud setup guide](./ResearchDrive_setup.md) to install and configure it first.

**If you cannot use the Nextcloud desktop client** for any reason, for example on a Linux server which you cannot install the client, please refer to the [**command line guide**](./ResearchDrive_commandLine.md) for detailed instructions on using `rclone` to sync with Research Drive.

:::{admonition} Web interface sucks for large file uploads
Web interface uploads usually have a file size limit and can time out for large files or a large number of small files. It also depends on the stability of your internet connection and the stability of your browser. Once stopped, you have to start over from the beginning.
:::

```{contents}
---
depth: 3
---
```

## Check capacity and reduce the number of small files

Make sure you have enough capacity. [Request more if needed](./ResearchDrive.md#expand-storage-space).

Note that [there are differences in file size calculation regarding with your quota](./ResearchDrive.md#different-sizes-in-dashboard-and-files).

If you have many small files, we recommend creating zip files before uploading. Large numbers of small files are expensive to store and transfer compared to fewer large files. For easier searching, you can keep a separate copy of human-readable results outside the zip archives.

:::{admonition} Sizes are also not accurate between local and remote
Due to differences between file systems, the sizes on your own system may not match the sizes shown on ResearchDrive.
:::

### On your mapped drive or USB storage

Right-click your source folder to see its size in the “properties” window. If it takes too long, consider using [WinDirStat](https://windirstat.net/) (download “Zipped Executables” on your university computer).

## Upload and remove sync after

1. Open settings: right-click <span><img alt="new windows systemtray icon" src="../_static/images/nextcloud_icon_new.png" width="24"></span> or <span><img alt="windows systemtray icon" src="../_static/images/nextcloud_icon.png" width="24"></span> or <span><img alt="macos icon" src="../_static/images/nextcloud_icon_macos.jpg" width="24"></span> and click “Settings”.
2. Click “Add Folder Sync Connection”, then pick the source directory you want to upload.
   ![Add Folder Sync Connection](../_static/images/nextcloud_settings.png)
   ![Pick a source dir](../_static/images/nextcloud_pick_source.png)
3. Click “Next”, choose a target location, click **“Create folder”**, then click “Next”.
   ![Create target location](../_static/images/nextcloud_create_target_folder.png)
4. Uncheck “Use virtual files instead ...”, then click “Add Sync Connection”.
   ![Add sync connection](../_static/images/nextcloud_add_sync.png)
5. The upload starts; wait for it to finish. Try not to change anything in the source folder on the mapped drive or USB storage while uploading.
   ![wait for sync](../_static/images/nextcloud_syncing.png)
6. Once the upload has finished, confirm everything is green, then check your files in the web interface or in your default sync folder.
7. Remove the additional sync folder by clicking “Remove Folder Sync Connection”, and confirm the removal.
   ![Finished uploading](../_static/images/nextcloud_sync_complete.png)
   ![Confirm removal](../_static/images/nextcloud_sync_remove.png)
8. You can now safely remove your data from your mapped drive or USB storage.

:::{admonition} Always sync to empty folder
A sync folder is always synced bidirectionally, so using an empty folder helps ensure Nextcloud does not download data back to your mapped drive or USB storage.
:::

## In case of upload errors

If you see red crosses or yellow warnings, left-click the <span><img alt="new windows systemtray icon" src="../_static/images/nextcloud_icon_new.png" width="24"></span> or <span><img alt="windows systemtray icon" src="../_static/images/nextcloud_icon.png" width="24"></span> or <span><img alt="macos icon" src="../_static/images/nextcloud_icon_macos.jpg" width="24"></span> icon and scroll to the top to see what is happening. If you are not sure, please contact the IBL RDM team with a screenshot and any related information.