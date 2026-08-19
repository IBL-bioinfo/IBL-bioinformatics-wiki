# Set up sync on your computer

*By C.Du [@snail123815](https://github.com/snail123815) & Joost Willemse [@Karivtan](https://github.com/Karivtan)*

We recommend using the Nextcloud desktop client to access Research Drive files on your local
computer. This allows you to work with your data directly from your file explorer (Windows
Explorer or macOS Finder), and avoids the size limits and timeouts of
[uploading through the web interface](./ResearchDrive_transfer.md).

The **"virtual files" feature** of modern OS is supported in Nextcloud desktop sync, which allows
you to see all your files in Explorer/Finder without taking up local storage space until you open
them. You can also choose to make files available for offline access.

(first-sync-takes-time)=
::: {admonition} Before you start: allow about an hour for the first sync
:class: important
Set this up at a time when you can **leave the computer switched on and connected for around an
hour**. The first sync has to reconcile everything that has been shared with you, and it takes far
longer than later ones.

Do not shut down, sleep, or disconnect the computer part-way through. An interrupted first sync can
leave files in an inconsistent state, and in the worst case you can lose data. Wait until the
Nextcloud icon reports that syncing is complete before you close the laptop.
:::

::: {admonition} Do not add data directly to the top-level Research Drive folder
:class: warning
Unlike OneDrive, {ref}`you do not own any space in Research Drive <you-do-not-own-space>` — everything is shared with you. When you open Research Drive, the first screen you see (the **top-level folder**) only shows folders that have been shared with you:

1. The project folder that belongs to a PI
2. Any other folder shared with you

Anything you create **directly in that top-level folder** is **not part of Research Drive** and will **not be synced** — it will be lost.

```{mermaid}
graph LR
    RD["🗄️ Research Drive (top-level folder — what you see when you open Research Drive)"]
    RD --> P1["📁 ProjectA  ← shared with you ✅"]
    RD --> P2["📁 ProjectB  ← shared with you ✅"]
    RD --> BAD1["❌ 📄 my_file.txt created by yourself  ← NOT synced, will be lost!"]
    RD --> BAD2["❌ 📂 my_folder created by yourself  ← NOT synced, will be lost!"]
    RD --> GOOD1["📄 data.txt shared by others  ← synced ✅"]
    P1 --> GOOD2["📂 subfolder created by yourself inside ProjectA  ← synced ✅"]
    style BAD1 fill:#ffcccc,stroke:#cc0000
    style BAD2 fill:#ffcccc,stroke:#cc0000
    style P1 fill:#ccffcc,stroke:#009900
    style P2 fill:#ccffcc,stroke:#009900
    style GOOD1 fill:#ccffcc,stroke:#009900
    style GOOD2 fill:#ccffcc,stroke:#009900
```

:::

```{contents}
---
depth: 3
---
```

## Install Nextcloud desktop client

For University Computer, please find Nextcloud desktop client in the **Company Portal** (Windows 11) or **Managed Software Centre** (macOS). For personal computer, you can download **"Nextcloud Files"** application from the [Nextcloud website](https://nextcloud.com/install/#install-clients). There is also Linux version available.

### University Mac users

The Nextcloud client from the **Managed Software Centre** supports virtual files. If yours does not (see [how to check](#set-up-nextcloud-desktop-client-and-sync-with-research-drive) below), it is probably an outdated build — contact the ISSC helpdesk and ask for the current Nextcloud desktop client. Virtual files is important for efficient storage management and seamless access to Research Drive files on your local machine.

(select-virtual-files-version)=
### Personal Mac users

Download the standard **macOS 13+** client from the [Nextcloud website](https://nextcloud.com/install/#install-clients). Virtual files is built into it, so there is nothing extra to choose.

:::{warning}
Do **not** download the **"MacOS 11+ (legacy)"** build. It is an old version (3.13.4) that does **not** support virtual files, so every file would be downloaded to your Mac and fill up your disk.

If your Mac cannot run macOS 13 or newer, you cannot use virtual files at all. Either upgrade macOS, or work with Research Drive through the [web interface](https://universiteitleiden.data.surf.nl/) and [`rclone`](./ResearchDrive_commandLine.md) instead.
:::

```{note}
Older guides (including earlier versions of this page) told you to pick a separate "Virtual files" download such as *"macOS Virtual files 12+ (64 bit, universal)"* from a dropdown. That dropdown no longer exists — Nextcloud now ships a single macOS client with virtual files included.
```

## Set up Nextcloud desktop client and sync with Research Drive

- [Install the Nextcloud application](#install-nextcloud-desktop-client)
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

- Choose a folder to store the data; it **must be a *new* or *empty* folder**. **Please make sure to select a folder that is *not synced* by iCloud, OneDrive, or other services**. MacOS users should also avoid using the default "Documents" folder, which is often synced with iCloud and can cause issues. We recommend creating a new folder named "RD" (or similar) directly under your user directory (for example, `C:\Users\<name>\RD` on Windows or `/Users/<name>/RD` on macOS) to ensure it is not affected by other sync services and to minimize path length issues.
  - **MacOS users:**
    - You do not need to choose any file or folder to sync, the virtual file system will create a virtual drive for you, and you can access the data via the Finder. You can also choose to sync to a local folder if you prefer, but it is not required.
    - You will *not* see "User virtual files ..." option.
  - See {ref}`Virtual files and "Choose what to sync" are mutually exclusive <choose-what-to-sync-are-mutually-exclusive>`

  ```{image} ../_static/images/nextcloud_login_chooselocation.png
  :alt: Choose sync location
  :width: 30em
  ```

- Click **Connect**. Sync should start; you can see <span><img alt="new windows systemtray icon" src="../_static/images/nextcloud_icon_new.png" width="24"></span> or <span><img alt="windows systemtray icon" src="../_static/images/nextcloud_icon.png" width="24"></span> or <span><img alt="macos icon" src="../_static/images/nextcloud_icon_macos.jpg" width="24"></span> in your system tray located on the bottom right (Windows) or top right (macOS). Expand the system tray if needed.
- Check your settings:
  - Right-click the Nextcloud icon <span><img alt="new windows systemtray icon" src="../_static/images/nextcloud_icon_new.png" width="24"></span> or <span><img alt="windows systemtray icon" src="../_static/images/nextcloud_icon.png" width="24"></span> or <span><img alt="macos icon" src="../_static/images/nextcloud_icon_macos.jpg" width="24"></span> in the system tray, then left-click "Settings"  

    ```{image} ../_static/images/nextcloud_systemtray.png
    :alt: NextCloud Settings
    ```

  - Virtual files **enabled**  

    ```{image} ../_static/images/nextcloud_login_checkvertualfileenabled.png
    :alt: Virtual files enabled in Windows 11
    :width: 45em
    ```

- For macOS users, "Virtual files" should be enabled by default. If it is missing, you are running an outdated client: uninstall it and [install the current macOS 13+ client](#select-virtual-files-version). For University laptop users, please contact the ISSC helpdesk to request an update instead.

  ```{image} ../_static/images/nextcloud_enable_virtual_files_macos.jpg
  :alt: Virtual files enabled in macOS
  :width: 30em
  ```

- You can access the data via the file browser (Explorer on Windows, Finder on macOS). You should see the cloud icon on the project folder, that icon will change depending on whether the files are cloud-only or downloaded.

  ```{image} ../_static/images/nextcloud_locations.png
  :alt: Data access via file browser
  :width: 45em
  ```

::: {admonition} Sharing with a whole group
If you want to share a folder with all of your lab members or a specific subgroup, create a
**Team** in the "Contacts" page (top bar) and share with the team instead of with individual
users — new team members then get access automatically. See
[Share with a group of users](./ResearchDrive_sharing.md#share-with-a-group-of-users).
:::

## Next steps

- Moving a large amount of data? Start at
  [Choose how to move your data](./ResearchDrive_transfer.md).
- Sync stuck, or your disk filling up? See
  [Common issues and troubleshooting](./ResearchDrive_troubleshooting.md).
