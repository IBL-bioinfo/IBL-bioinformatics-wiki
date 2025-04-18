# Server configurations

Software setup of our servers.

```{contents}
---
depth: 3
---
```

## General storage

```` {admonition} No backup
:class: note
As a small server cluster intended for testing and teaching, we **do not** plan to backup any data you upload to the servers. Please remove your data when it is not needed.
````

```` {admonition} Remove your data after use
:class: warning
We kindly request all users to be mindful of the limited storage available. To ensure fair usage and accommodate everyone's needs, please remove your data once it is no longer required. Your cooperation is greatly appreciated. **Research Drive** is one option of backing up your data. For that `rclone` tool is avilable, notify adminstrator if not. In Research Drive webpage, you click top right on your name, then "settings", go to the left, click "Security", scroll to the bottom, create a new "App password". The weblink is shown below in the bottom, you need to **remove** the last two parts `/remote.php/webdav/` when asked. Now you have all necessary information. Detailed instructions will follow soon.
````

Most of the IBL servers have a small but fast SSD for `/home` directory storage, plus one or more slower but much larger HDD for storage of data. The HDDs are mounted on directory `/vol/local`, if there is extra disks, we mount them on `/vol/local1`, `/vol/local2` etc. You can use command `df -h` to check:

```sh
[user@blis ~]$ df -h /vol/*
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda        7.3T  622G  6.7T   9% /vol/local
/dev/nvme1n1    954G  442G  512G  47% /vol/local1
```

Note the `/dev/nvme1n1` is an `nvme` device, meaning it is also an SSD, for IO rich commands, you can try to run on that location.

## Sharing data and software environment

When you get your account, you will be assigned to the research group you belong to. At the same time, all members in all research groups will automatically join another group called `condablis`.

1. **`/home/user`** is your own private space. But keep in mind that administrators can have access to it.
2. **`/vol/local`** directory will have `rwxr-xr-x` or `755` and files will have `rw-r--r--` or `644`.
(shared-environments-location)=
3. **`/vol/local/conda_envs`** is where all software environments should be created and maintained. It has permission `rwxrwsr-x`, or `2775`.  
    The `2` in front means that all files and directories will have `condablis` as group ownership, accessible (read permission) to everybody.

### Modify an environment by different user

Only you can modify an environment that is created by yourself. If you want others to help modify, for example after activating the environment, try to install something by `micromamba install` or do any other modification on the environment directory, you need to specifically give the permission to `condablis` group. Which is write permission to all files and directories:

```shell
(base) [user@blis ~]$ chmod -R g+w /vol/local/conda_envs/env_name
```

After the environment is modified by another user, the environment is locked again by the other user. This process needs to be repeated by the other user to allow the original user to edit the environment. When doing the same command, you will see a lot of `Operation not permitted` warning, you can ignore those. Because you can only change the file you created. The modified files will not be shown. You can check by comparing the permission string of just a few files before and after `chmod` command, all should have a `w` in the middle. Use `find` command:

```sh
(base) [user@blis ~]$ find /vol/local/conda_envs/env_name -user $USER -exec ls -al {} \;
```

## Home directory quota explained

Except BILBO, you will have limited storage space in your `/home/<user>` directory. This is meant for supporting as much users as possible. The `/home` directory is located in SSD and should be fast, it is intended to store scripts that you made, programs that you compile that do not fit for sharing, or some temporary files generated by your program.

Find how much you have used using the following commands:

```sh
[user@blis ~]$ quota -s
Disk quotas for user <user> (uid 168888888):
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
/dev/mapper/rl-home
                   785M  20480M  25600M           14081       0       0

[user@blis ~]$ du -d 0 -h ~/
785M    /home/user/

```

Please avoid exceeding your quota, even if you notice that your usage is not being tracked or listed in the quota system. This could be an error and may be corrected at any time.

You can overrun the system to "limit", but cannot exceed it. The file system will block you from writing any new stuff in. If this happened during your job which writes to `~` directory, the job will fail. You need to run all data IO heavy jobs from the shared storage. For that, please check carefully the program you want to use for its temporary and output data location.

Contact server administrators in our SLACK group if you really need larger `~` directory.

## Micromamba instead of Conda

For program environment management and setup, we use **Micromamba** instead of Conda. While `micromamba` and `conda` share similar commands, you may need to adjust some commands to fit `micromamba`. There are several advantages to using `micromamba`. 

1. **Faster Dependency Resolution**: `micromamba` resolves dependencies significantly faster, reducing resolution times from 10 minutes to as little as 1 minute.
2. **Simpler Maintenance**: `micromamba` is a single executable with minimal dependencies, whereas Conda requires multiple libraries and often root privileges for installation and upgrades.
3. **Command Compatibility**: The commands for `micromamba`, such as `install` and `--channels`, are the same as those in Conda. Additionally, environments created with `micromamba` are largely compatible with Conda, allowing you to follow most online tutorials, such as those involving the `activate.d` directory.
4. **Shared Server Optimization**: On shared servers, you often need to tweak `conda create` and `conda install` commands to set up environments in shared storage. It takes same effort to use `micromamba`.

### How to use Micromamba on IBL servers

1. **Create environment before install**: For command `conda create -n myenv -c bioconda python biopython`, to create "myenv" environment and install `python` and `biopython` package in it. Please use the following 3 commands instead.

     ```sh
     (base) [user@blis ~]$ micromamba create -p /vol/local/conda_envs/myenv
     (base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/myenv
     (/vol/local/conda_envs/myenv) [user@blis ~]$ micromamba install -c bioconda python biopython
     ```

2. **Always create environment in `/vol/local/conda_envs/`**:  
     **Always** use `micromamba create -p /vol/local/conda_envs/myenv`.  
     If you have a *soft link* `~/genvs -> /vol/local/conda_envs`, you can simplify the command to `micromamba create -p ~/genvs/myenv`. I have an *alias* `mmm=micromamba`, so `mmm create -p ~/genvs/myenv` will work for me.  
     This is because we applied disk quota on `/home` directory. These environments are in your `/home` directory:
     1. The `micromamba` base environment.
     2. All environments created using `micromamba create -n <env-name>`
     3. All environments created using `micromamba create -f <environment_description>.yaml` (or `*.yml`). Most `*.yaml` file starts with `name: env-name` line, it is equivalent to `-n <env-name>`. Also, `-n` is not compatible with `-p`.  
          To use this file, please remove the `name: env-name` line, then create an environment for it using `-p` as stated. Then you can install it in an **existing** environment using `micromamba install -f <environment_description>.yaml` 

## Jump within servers

You can jump from any server to any other server using `ssh [servername (lowercases)]`.

### Check os version

```sh
$ cat /etc/os-release
NAME="Rocky Linux"
VERSION="9.3 (Blue Onyx)"
ID="rocky"
ID_LIKE="rhel centos fedora"
VERSION_ID="9.3"
PLATFORM_ID="platform:el9"
PRETTY_NAME="Rocky Linux 9.3 (Blue Onyx)"
ANSI_COLOR="0;32"
LOGO="fedora-logo-icon"
CPE_NAME="cpe:/o:rocky:rocky:9::baseos"
HOME_URL="https://rockylinux.org/"
BUG_REPORT_URL="https://bugs.rockylinux.org/"
SUPPORT_END="2032-05-31"
ROCKY_SUPPORT_PRODUCT="Rocky-Linux-9"
ROCKY_SUPPORT_PRODUCT_VERSION="9.3"
REDHAT_SUPPORT_PRODUCT="Rocky Linux"
REDHAT_SUPPORT_PRODUCT_VERSION="9.3"
```