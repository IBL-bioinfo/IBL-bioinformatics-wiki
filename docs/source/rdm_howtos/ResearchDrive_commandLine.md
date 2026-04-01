# Research Drive Command Line Upload with `rclone`

*By C.Du [@snail123815](https://github.com/snail123815)*

For **command line users** (for example, if you are using a Linux terminal on IBL servers or ALICE, or even on your Windows using PowerShell), you can use `rclone` to sync with Research Drive. This can be especially useful for uploading large files or syncing entire directories without needing to copy them to your local machine first (alternative to [using the Nextcloud desktop client](./ResearchDrive_uploadFromNetworkDrive.md)).

You need to finish configuration steps to use `rclone` with Research Drive.

## Install `rclone`

The instructions on the [`rclone` website](https://rclone.org/install/) requires `sudo` or administrator privileges, which is not be available on university computers. Even if you have admin privileges, we still recommend following the instructions below to install `rclone` in your user space without needing admin privileges.

### MacOS

Install `rclone` using Homebrew:

(If you don't have Homebrew, you can install it by running the magic command at [https://brew.sh/](https://brew.sh/))

```sh
brew install rclone
```

### Linux

For IBL servers and ALICE, `rclone` is already installed and available in the system path. You can check by running:

```sh
rclone --version
```

### Windows

Install `rclone` using Winget or Scoop:

(If you don't have Scoop, you can install it by running the magic command at [https://scoop.sh/](https://scoop.sh/))

```powershell
winget install Rclone.Rclone
```

or

```powershell
scoop install rclone
```

## Configure `rclone` for Research Drive

Command line program `rclone` needs to be configured to connect to Research Drive. You only need to do this once on each machine you want to use `rclone` on.

1. Get your Research Drive credentials: In [Research Drive web interface](https://universiteitleiden.data.surfsara.nl/), click on your name at the top right, then go to "Settings", click "Security" on the left, scroll to the bottom. You will need:
    - The URL at the bottom "Access your Files via WebDAV", should be something like `https://universiteitleiden.data.surf.nl/remote.php/dav/files/<your email address>`
    - Create a new "App password". Fill in the "App name" field with something like "university computer rclone", then click "Create new app password". You will get a **"Login"** as *user name* and a **"Password"**. The password is only shown once, so make sure to copy it and keep it safe.
2. In your terminal, run `rclone config` to start the configuration process. Follow the prompts to create a new remote connection:
    - Choose "n" for a new remote.
    - Name it "rd" for research drive.
    - For the storage type, choose "webdav".
    - For the webdav type, choose "nextcloud".
    - For the URL, enter the WebDAV URL you got from step 1.
    - For the user name and password, enter the credentials you got from step 1.
    - You can leave other settings as default.
3. Once you finish the configuration, you can test the connection by running `rclone lsd rd:`. This should list the project folders or folders shared with you in your Research Drive. `lsd` stands for "list directories". Note files will not be listed by this command, only directories. You can use `rclone ls rd:` to list all files and directories, but it may take a long time if you have many files. There should not be any error message.

## Basic `rclone` commands

Check the [`rclone` documentation](https://rclone.org/docs/#subcommands) for more details and options. Here are some common commands:

```sh
# List files and directories
rclone ls rd:/path/in/researchdrive

# Sync a local directory to Research Drive showing progress
rclone sync -P /path/to/local/dir rd:/path/in/researchdrive

# Copy a local file to Research Drive
rclone copy /path/to/local/file rd:/path/in/researchdrive

# Sync Research Drive to a local directory
rclone sync rd:/path/in/researchdrive /path/to/local/dir

# Copy a file from Research Drive to local
rclone copy rd:/path/in/researchdrive/file /path/to/local/dir

# Dry run a sync to see what would be changed without actually doing it
rclone sync /path/to/local/dir rd:/path/in/researchdrive --dry-run
```

**Differences between `sync` and `copy`:** `sync` will make the destination exactly match the source, which means it will delete any files in the destination that are not in the source. `copy` will only copy files from source to destination without deleting anything.

## Determine the path in Research Drive

The path in Research Drive is determined by the folder structure in the web interface. For example, if you are *Dave* and have a folder `Dave` in your PI's project folder `ProjectA`, and inside it a folder called `Research`, the path to that `Research` folder would be `rd:ProjectA/Dave/Research`. If you want to upload a file directly to "Dave", the path would be `rd:ProjectA/Dave`.

## Specific requirements for Research Drive

The transfer using `rclone` basic commands should already work for small files and directories. However, for large files and directories with many files, it is recommended to use additional parameters to optimize the transfer:

```sh
rclone sync --links --use-cookies --transfers 4 --timeout "60m" /path/to/local/dir rd:/path/in/researchdrive
```

- `--links`: This option tells `rclone` to copy symbolic links as symbolic links, which can be important for preserving the structure of your data, very important for Linux users which you have soft links in your data.
- `--use-cookies`: This option allows `rclone` to use cookies for authentication, which can help maintain a stable connection during long transfers.
- `--transfers 4`: This option allows `rclone` to perform multiple file transfers in parallel, which can speed up the transfer process. You can adjust the number based on your network and system capabilities.
- `--timeout "60m"`: This option sets a longer timeout for the transfer, which can help prevent timeouts for large files or slow connections.

## Simplified `rclone` wrapper

I am maintaining a [`sync-with-rclone`](https://github.com/IBL-bioinfo/sync-with-rclone) wrapper script that simplifies the `rclone` commands above. Instead of remembering all the flags and paths, you configure once per folder and then just run `push` or `pull`. It also has a built-in ignore list that automatically excludes common files that don't need to be backed up (e.g. `*.tmp`, `.git` directories), and can record git commit information for git repositories. This is useful whether your remote repository is on GitHub or on the university GitLab.

(Linux and MacOS only)

I especially recommend IBL server users and ALICE users to use this wrapper, because it is optimized for syncing research data and can handle some edge cases that may arise when syncing with Research Drive.

### Setup

Make sure you have `rclone` installed and configured for Research Drive as described above. Clone the repository to your local machine and make the script executable:

```sh
git clone https://github.com/IBL-bioinfo/sync-with-rclone.git
cd sync-with-rclone
chmod u+x sync-with-rclone.sh
```

For each local folder you want to sync with Research Drive:

1. Copy `sync-with-rclone.sh` and `sync-with-rclone.config` to the local folder
2. Edit `sync-with-rclone.config` to set your remote name and path:

   ```ini
   REMOTE_NAME="rd"
   REMOTE_PATH="ProjectA/Dave/Research"
   ```

3. The script should be executable, otherwise:

   ```sh
   chmod u+x sync-with-rclone.sh
   ```

### Basic usage

```sh
# Upload local folder to Research Drive
./sync-with-rclone.sh push

# Download from Research Drive to local folder
./sync-with-rclone.sh pull

# Preview what would change without actually doing it
./sync-with-rclone.sh push --dry-run

# Use sync instead of copy (WARNING: deletes files in research drive that are not in local)
./sync-with-rclone.sh push --sync

# Push only specific files, and with dry-run to preview
./sync-with-rclone.sh push --include "analysisC/**" --dry-run

# Get help
./sync-with-rclone.sh --help
```

For more details and options, see the [sync-with-rclone README](https://github.com/IBL-bioinfo/sync-with-rclone).
