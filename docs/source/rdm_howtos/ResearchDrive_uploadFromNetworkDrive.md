---
orphan: true
---

# Transfer to ResearchDrive from Mapped Network Drive

Uploading files usually takes 3 steps:

1. Local file copied / moved to the synced folder
2. NextCloud upload these files to ResearchDrive (or other cloud storage)
3. If these files are not used, or local storage is full, NextCloud removes these local files, replace them with "virtual files".

For your large files located on your network drive, you will find it difficult to finish the very first step, as you do not have enough local storage to host it.

## Check capacity and reduce small file number

Make sure you have enough capacity. Apply for more with correct cost centre from ISSC helpdesk.

If you have many small files, we recommand you to create zip files for them before uploading. Small files are very expensive in data storage and transfering comparing to large single files. For easier data searching, you can make a copy of human readable results and keep them out from zipping.

:::{admonition} Sizes are not accurate
Due to the differences between file systems, the sizes on your own system may not equal to the sizes taken on ResearchDrive.
:::

### On ResearchDrive

500 GB = 465.66 GiB

- Size units on "Files" page is TiB/GiB/MiB
- Size units on "Dashboard" page is TB/GB

Check the capacity of your target ResearchDrive project folder, note the capacity is calculated differently and there is a delay in showing the changes in your dashboard after you upload or delete some files.

### On your network drive

Right click on your source folder to see its size in "proterty" window. If it takes too long, consider use [WinDirStat](https://windirstat.net/) software (download "Zipped Executables" on your University computer).

## Upload and remove sync after

1. Open settings: right click ![NextCloud](../_static/images/nextcloud_icon.png) and click "Settings"
2. Click on "Add Folder Sync Connection", pick a source dir to be uploaded
   ![Add Folder Sync Connection](../_static/images/nextcloud_settings.png)
   ![Pick a source dir](../_static/images/nextcloud_pick_source.png)
3. Click on "Next>", choose a target location, **"Create folder"**, then click "Next>"
   ![Create target location](../_static/images/nextcloud_create_target_folder.png)
4. Uncheck "Use virtual files instead ...", click "Add Sync Connection"
   ![Add sync connection](../_static/images/nextcloud_add_sync.png)
5. Upload started, wait for it to finish. Try not to change anything in the source folder while uploading.
   ![wait for sync](../_static/images/nextcloud_syncing.png)
6. Once upload finished, confirm everything is green, check your files on the web interface or your default sync folder.
7. Remove the additional syncing folder, confirm the removal by clicking "Remove Folder Sync Connection"
   ![Finished uploading](../_static/images/nextcloud_sync_complete.png)
   ![Confirm removal](../_static/images/nextcloud_sync_remove.png)
8. Now you should be able to safely remove your data from your network drive.

:::{admonition} Always sync to empty folder
A sync folder is always synced bidirectionally, thus an empty folder will ensure NextCloud to not download more data to your network drive.
:::

## In case of uploading error

If you see any red crosses or yellow marks, please left click on the ![NextCloud](../_static/images/nextcloud_icon.png) icon, scroll to the top, you will see what is happening. If you are not sure, please contact IBL RDM team with a screen shot and any related information.