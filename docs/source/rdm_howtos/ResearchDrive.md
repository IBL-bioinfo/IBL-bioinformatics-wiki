# Research Data Storage

*By C.Du [@snail123815](https://github.com/snail123815) & Joost Willemse[@Karivtan](https://github.com/Karivtan)*

[Research Drive](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/117178843/Research+Drive) is a cloud-based platform that enables researchers to securely store, share, and collaborate on data, and serves as an essential RDM tool for complying with the IBL RDM policy.

```{contents}
---
depth: 3
---
```

## Research Drive direct access URL

Research Drive (Nextcloud interface) - [https://universiteitleiden.data.surfsara.nl/](https://universiteitleiden.data.surfsara.nl/)

## Research Drive intended structure

![Intended Research Drive folder structure showing a hierarchical hierarchy with root project folders containing year-based subfolders, which contain role-based folders (PI, Students, PostDoc, LabManager) for organizing research data by project, time period, and user responsibility](../_static/images/IBL_Research_Drive_Hierarchy.svg)

## Nextcloud and Research Drive

**Nextcloud is the software platform that powers Research Drive.** It provides a user-friendly interface for managing files and folders, as well as features for sharing and collaboration. The Nextcloud desktop client allows you to sync files between your local computer and Research Drive, enabling you to access your data from anywhere with an internet connection.

## Application and invitation

For **PI**, you need to apply for it:
- Research Drive is now a paid service, please consult IBL RDM team for the cost and funding details.
- Request Research Drive per project/DMP/contract
  - [ISSC helpdesk](https://helpdesk.universiteitleiden.nl/)
  - Go to "Research support" → "Research Drive" → "Request Research Drive"
  - Choose **"No"** for DMP, **always use a cost centre** number in "SAP number:" field, ISSC has stopped support for DMP-based funding.
  - Mention the project folder name you want to create in "Comment:" field
- Invite your lab manager if you do not want to manage the Research Drive yourself. Give your lab manager full access to all your project folders, then the lab manager can then invite the rest of the staff and students and manage the major folder shares.
- See [Invite users and set up the folder structure:](#invite-users-and-set-up-the-folder-structure) section for details.

For **PhD/PostDoc/Researcher (stuff)**, once you received the invitation, please follow the link and confirm you can login. Only then your PI or lab manager can give you access to your folder.

### Download and install Nextcloud desktop client

For University Computer, please find Nextcloud desktop client in the **Company Portal** (Windows 11) or **Managed Software Centre** (macOS). For personal computer, you can download **"Nextcloud Files"** application from the [Nextcloud website](https://nextcloud.com/install/#install-clients). There is also Linux version available.

:::{admonition} MacOS users
(select-virtual-files-version)=
Please make sure to select "Virtual files" desktop client, for example **"macOS Virtual files 12+ (64 bit, universal)"**, from the dropdown menu when downloading. The "Virtual files" version allows you to access your Research Drive files without taking up local storage space, which is inevitable for most research scenarios and is a standard practice.

!["macOS 12+" (standard) and "macOS Virtual files 12+ (64 bit, universal)". The latter needs to be selected from the dropdown menu.](../_static/images/nextcloud_macos_virtualfiles_version.jpg)
:::

:::{admonition} Managed Software Centre for macOS users
It is possible that the Nextcloud desktop client available in the Managed Software Centre does not have the "Virtual files" feature enabled. If that is the case, please contact the ISSC helpdesk to request an update to the Nextcloud client with "Virtual files" support. This feature is important for efficient storage management and seamless access to Research Drive files on your local machine.
:::

## Workflow Setting Up Research Drive

After Research Drive has been activated, follow these steps to set up your project folder, invite users, and sync files to your local computer.

Login:
- PI logs in to [Research Drive](https://universiteitleiden.data.surf.nl)
- Go to the dashboard (top-left icon row, rightmost icon)

::: {admonition} First-time login
Expect multiple login prompts and a missing project folder the first time you log in. This is because some things are only set up when you start using Research Drive. The project folder should appear a few minutes later.
:::

::: {admonition} It is **normal** to have "No permission to create a project folder"
On your "Dashboard" → "Project folders" page, you may see the message "You do not have sufficient permissions to create ...". This is normal: project folders can only be created by ISSC upon request.

![You will always see 0B of 0B used](../_static/images/nextcloud_zero_of_zero_used.png)

![You do not have sufficient permissions to create ...](../_static/images/nextcloud_you_have_no_permission.png)
:::

### Invite users and set up the folder structure:

- Go to "Dashboard" → "User accounts" and invite all users, both staff and students.
  - Once the first several staffs finish setting up, they can invite the rest of the staff and students.
- Invite users using their official email address, for example the @biology mail for employees
  - **External users** can gain access when you invite their external email address. They must first create their own [eduID](https://eduid.nl/home) account or use the account from their institute (if present in the system) before they can log in.
- Go to the **Files** tab (top left), and go into your **project folder**
- Create a folder for everyone in this project

Once the staff and student accounts are activated:
- Go to the **Files** tab, locate the target folder, and click the **"Shared"** button
  - Make sure the pop-up shows the correct folder name, click "Sharing" tab if not already selected
- In **Internal shares** section, add the correct users, and set permissions to allow editing (for their own folder only).
  - Same procedure for other files you want to share with specific users, but be careful with the permissions.
- Users can now access data within the subfolder of the project.

::: {admonition} Only add data to the project folder
The project folder is the only folder that will be synced to your local computer. If you add files outside the project folder, they will not be synced and you will not be able to access them locally.
:::

Setup local sync (optional):
- [Install the Nextcloud application](#download-and-install-nextcloud-desktop-client)
- Open Nextcloud once installed and click **Log in**  
  ```{image} ../_static/images/nextcloud_login_login.png
  :alt: login
  :width: 30em
  ```
- Enter the following URL and click **Next**  
  ```
  https://universiteitleiden.data.surf.nl
  ```
  ```{image} ../_static/images/nextcloud_login_URL.png
  :alt: Enter URL
  :width: 30em
  ```
- **Log in** with your ULCN account in the pop-up browser window
- **Grant access** when asked, then close the browser page  
  ```{image} ../_static/images/nextcloud_login_grantaccess.png
  :alt: Login and grant access
  :width: 30em
  ```
- Choose a folder to store the data; it must be a new or empty folder. **Please make sure to select a folder that is not synced by iCloud, OneDrive, or other services**. MacOS users should also avoid using the default "Documents" folder, which is often synced with iCloud and can cause issues. We recommend creating a new folder named "RD" (or similar) directly under your user directory (for example, `C:\Users\<name>\RD` on Windows or `/Users/<name>/RD` on macOS) to ensure it is not affected by other sync services and to minimize path length issues.
  - **MacOS users:**
    - You do not need to choose any file or folder to sync, the virtual file system will create a virtual drive for you, and you can access the data via the file browser. You can also choose to sync to a local folder if you prefer, but it is not required.
    - You will not see "User virtual files ..." option.
  - [Virtual files and "Choose what to sync" are mutually exclusive](#choose-what-to-sync-are-mutually-exclusive)
  ```{image} ../_static/images/nextcloud_login_chooselocation.png
  :alt: Choose sync location
  :width: 30em
  ```
- Click **Connect**. Sync should start; you can see ![icon](../_static/images/nextcloud_icon.png) or <span><img alt="macos icon" src="../_static/images/nextcloud_icon_macos.jpg" width="24"></span> in your system tray located on the bottom right (Windows) or top right (macOS). Expand the system tray if needed.
- Check your settings:
  - Right-click the Nextcloud icon ![icon](../_static/images/nextcloud_icon.png) in the system tray, then left-click "Settings"  
    ```{image} ../_static/images/nextcloud_systemtray.png
    :alt: NextCloud Settings
    ```
  - Virtual files **enabled**  
    ```{image} ../_static/images/nextcloud_login_checkvertualfileenabled.png
    :alt: Virtual files enabled in Windows 11
    :width: 45em
    ```
- For macOS users, you should see "Virtual files" is enabled by default. If not, you need to uninstall the current Nextcloud client and [download the version](#select-virtual-files-version) with "Virtual files" support. For University laptop users, please contact the ISSC helpdesk to request an update to the Nextcloud client with "Virtual files" support.
  ```{image} ../_static/images/nextcloud_enable_virtual_files_macos.jpg
  :alt: Virtual files enabled in macOS
  :width: 30em
  ```
- You can access the data via the file browser (Explorer on Windows, Finder on macOS). You should see the cloud icon on the project folder, that icon will change depending on whether the files are cloud-only or downloaded.
  ```{image} ../_static/images/nextcloud_locations.png
  :alt: Data access via file browser
  :width: 45em
  ```

::: {admonition} Create **Teams** and share within team
Sometimes you want to share a folder with all of your lab members or a specific subgroup. You can create **Teams** in the "Contacts" page (top bar), add the relevant users to that team, and then share the folder with the team instead of individual users. This way, when you add new members to the team, they will automatically have access to the shared folder.
:::

### Space on your local machine

Research Drive uses the Nextcloud desktop client to *sync* files between the **cloud** (Research Drive) and your **local** computer.

When **Virtual files** are enabled (recommended), Windows Explorer or Finder on macOS can show files that exist in the cloud without storing the full data locally.

- Local vs cloud (practical meaning)
  - **Cloud**: The file exists on Research Drive and counts toward your project’s storage, even if it is not downloaded to your laptop/PC.
  - **Local**: The file’s data is present on your computer and consumes disk space.

You can think of “virtual files” as shortcuts/placeholders: they show up in Explorer or Finder so you can browse/search, but the content is only downloaded when you open it.


:::{admonition} Virtual files and "Choose what to sync" are mutually exclusive
(choose-what-to-sync-are-mutually-exclusive)=
The "Choose what to sync" option allows you to select specific folders to sync locally, but it is not compatible with virtual files. If you enable "Choose what to sync", you will lose the virtual file functionality, and all files in the synced folders will be downloaded to your local machine. Therefore, it is recommended to keep "Choose what to sync" disabled and use virtual files to manage your storage efficiently.
:::

#### Windows “Properties” can show two different sizes

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

#### Free up space (Windows)

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

### Transfer large files from network drive

Transferring large files located on a network drive (for example, `J:`) to the cloud may require some extra steps.

Uploading files usually involves three steps:

1. Copy/move local files into the synced folder.
2. Nextcloud uploads these files to ResearchDrive (or other cloud storage).
3. If the files are not used, or if local storage is full, Nextcloud removes the local copies and replaces them with “virtual files”.

If you have large files located on your network drive, the first step can be difficult because you may not have enough local storage to hold them temporarily.

**Choose one of the following**:

1. Recommended: [**Add** an additional sync folder, then **remove** the sync after uploading](./ResearchDrive_uploadFromNetworkDrive.md)
2. [RcloneView](https://rcloneview.com/) software (not for university computers)
3. [Rclone GUI](https://rclone.org/gui/)

### Windows long path compatibility issue

On Windows, file paths can become too long for the operating system or for specific applications. Even on recent Windows versions, many tools still fail when the full path length approaches the legacy limit ([260 characters](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation)). When this happens, files may not sync correctly and may not be usable locally.

```{warning}
If Windows cannot create a folder/file locally due to path length, the Nextcloud/Research Drive client cannot store it either. You may see sync errors.
```

#### Common scenarios where files cannot be stored (or synced)

- Deep folder nesting (many subfolders), especially when the local sync folder is already long (for example under `C:\RD`).
- Very long filenames, or filenames generated by software exports (for example, long sample IDs + many parameters in the name).
- Extracting archives (ZIP/TAR) into a synced folder: the extracted structure is often deeper than expected.
- Cloning software repositories into Research Drive (for example, projects containing `node_modules`, `venv`, `conda` environments, or other dependency trees).
- Workflows that auto-generate deeply nested output directories.

#### How to reduce the risk

- Use a short local sync root path (for example `C:\Users\<name>\RD` or simply `C:\RD` (if you are not sharing this computer with others) instead of a long path).
- Avoid unnecessary nesting; keep project folder structures shallow.
- Shorten filenames where possible; avoid encoding too much metadata in the name. Keep the metadata in a separate file when necessary.
- **Do not store dependency folders or full software environments in Research Drive**; keep those local.
- If you are on a managed university device and need Windows long path support enabled, contact ICT/ISSC. Enabling it typically requires admin rights, and note some applications still ignore the setting or report error while reading those files.
