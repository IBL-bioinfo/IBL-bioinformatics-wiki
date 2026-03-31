# Execute programs

*By C.Du [@snail123815](https://github.com/snail123815)*

We manage our software using conda-compatible **environments**, which have become a standard in small scale server configurations. By using environments, we can easily manage software dependencies and avoid conflicts between different software versions. [More info](../basic_tools/package_management_concept.md#software-environment).

```{contents}
---
depth: 3
---
```

On BLIS, we use a tool called **[micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)**, a lightweight and efficient alternative to conda, to manage these environments. A shared directory `/vol/local/conda_envs` dedicated to storing, sharing, and modifying environments is created on BLIS. By default, all users on BLIS should be in a group called `condablis`. This group grant users access to our shared environments.

All users should be in `condablis` group, you can use `groups` command to check:

```sh
[user@blis ~]$ groups
sgr condablis
```

## Prepare micromamba

For new users, micromamba will be automatically setup at your first login to a server, if you see `(base)` in front of your prompt login and run `micromamba info` successfully, then you are good to go:

(micromamba-info-output)=

```sh
(base) [user@blis ~]$ micromamba info

       libmamba version : 2.5.0
     micromamba version : 2.5.0
           curl version : libcurl/8.18.0 OpenSSL/3.5.4 zlib/1.3.1 zstd/1.5.7 libssh2/1.11.1 nghttp2/1.67.0 mit-krb5/1.21.3
     libarchive version : libarchive 3.8.5 zlib/1.3.1 bz2lib/1.0.8 libzstd/1.5.7 libb2/bundled
       envs directories : /vol/local/conda_envs
                          /home/<username>/.micromamba/envs
          package cache : /vol/local/.conda_cache/<username>
            environment : base (active)
           env location : /home/<username>/.micromamba
      user config files : /home/<username>/.mambarc
 populated config files : /home/<username>/.mambarc
       virtual packages : __unix=0=0
                          __linux=5.14.0=0
                          __glibc=2.34=0
                          __archspec=1=x86_64_v3
               channels : https://conda.anaconda.org/bioconda/linux-64
                          https://conda.anaconda.org/bioconda/noarch
                          https://conda.anaconda.org/conda-forge/linux-64
                          https://conda.anaconda.org/conda-forge/noarch
                          https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
       base environment : /home/<username>/.micromamba
               platform : linux-64
```

It means you have micromamba setup ready for use, you can [execute an already installed program](#execute-an-already-installed-program). Otherwise, you need to do some configuration before you can activate and create environments.

Note, you only need to do this **once** on **one** server.

Here is how (assuming you are using default shell `bash`):

```sh
[user@blis ~]$ micromamba shell init -s bash -r ~/.micromamba
```

Above command will create a "base" environment at your home directory. Then a script will be put into your `~/.bashrc` file. Now you need to apply the setup by "sourcing" the `~/.bashrc` file:

```sh
[user@blis ~]$ source ~/.bashrc
```

Next time when you start your `bash` shell (at login), the script will be automatically executed.

Now you should be able to run this command without error:

```sh
[user@blis ~]$ micromamba info
```

You should see the output similar to the [one shown above](#micromamba-info-output). You may see less if the `~/.mambarc` file is not fully populated as shown below. If you see errors, please try to restart your shell (restart ssh connection). Ask for help with screen shots if still no success.

{#mambarc-setup}
New users should have `~/.mambarc` file with the following content:

```YAML
envs_dirs:
  - /vol/local/conda_envs
pkgs_dirs:
  - /vol/local/.conda_cache/<username>
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
```

The `~/.mambarc` file is further explained in [setting up config file section](./Install%20programs.md#setting-up-config-file).

## Execute an already installed program

In the base system, there is no bioinformatics related program. You cannot directly run programs like `phylophlan` when not in a corresponding environment. Activate the environment first:

```sh
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/phylophlan
# Note your prompt changes indicating you changed environment
(/vol/local/conda_envs/phylophlan) [user@blis ~]$ phylophlan -v
PhyloPhlAn version 3.0.67 (24 August 2022)
```

You may notice the prefix of the environment `/vol/local/conda_envs`. We store all working environments here. You can check if the environment for target software already exists or not. 

```sh
# `ls` - add forward slash in the end to list items in target directory, 
# `|` - pipe output to the following `grep` which filter the input by `phylophlan`
(base) [user@blis ~]$ ls /vol/local/conda_envs/ | grep phylophlan
phylophlan
```

Many programs are dependencies of others. You may not need to create a dedicated environment for them. Using `diamond` as an example:

```sh
(base) [user@blis ~]$ find /vol/local/conda_envs/ -type f -name diamond -executable
/vol/local/conda_envs/bakta/bin/diamond
/vol/local/conda_envs/antismash8_cda1015/bin/diamond
/vol/local/conda_envs/cblaster/bin/diamond
/vol/local/conda_envs/phylophlan/bin/diamond
/vol/local/conda_envs/quasan/bin/diamond
/vol/local/conda_envs/decrippter/bin/diamond
```

Try activate a few (`/vol/local/conda_envs/bakta`, `/vol/local/conda_envs/cblaster` for example) and see if it fits your need.

Case-insensitive search, which uses `-iname` instead of `-name`; wild-card matching:

```sh
(base) [user@blis ~]$ find /vol/local/conda_envs -type f -iname macs* -executable
/vol/local/conda_envs/macs3/bin/macs3
```

If the target environment or program or specific version of a program is not found, you may need to create an environment and install the software yourself. For detailed instructions, please check [program setup](./Install%20programs.md). You can install some frequently used small programs in your `base` environment. If it is activated by default, you can use them directly.

## Do not analyse large dataset in your home directory

One IBL server maybe powerful, but not when used by many colleagues, especially on data storage. Applying quota system on home directory `~/` is then necessary for the sustainable use. It means that you cannot use your `~/` freely. As a general rule in using Linux servers, you will find the quota system on almost all shared servers, including [ALICE](https://pubappslu.atlassian.net/wiki/x/wIA8Ag).

To check how much quota has left for you:

```sh
# Note you can only see the information when you are in ~ or any of its subdirectories.
[user@blis ~]$ quota -s
Disk quotas for user username (uid 148600000):
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
/dev/mapper/rl-home
                 16073M  20480M  25600M            154k       0       0
# Meaning you have used 16GB of the 20GB.
# You can store up to 25GB but after exceeding 20GB,
# you will be given a grace time of few days, then
# your home directory will be locked until you remove excess data
```

### Run analysis in shared drive

tldr: **Create a directory with your user name** in `/vol/local/`, then store your data and analysis in it.

Almost all bioinformatics analysis requires operating many Gigabytes of data. Since home directory `~/` is not a good place, we have a general storage space on each server, which is usually mounted on directory `/vol/local`, if there is extra disks, we mount them on `/vol/local1`, `/vol/local2` etc. You can use command `df -h` to check:

```sh
[user@blis ~]$ df -h /vol/*
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda        7.3T  622G  6.7T   9% /vol/local
/dev/nvme1n1    954G  442G  512G  47% /vol/local1
```

Note the `/dev/nvme1n1` is an `nvme` device, meaning it is an SSD. For IO rich commands, SSD might save your time. Not like ALICE, we do not have a common network location for storage which you can access from any server. It is quite complex and expensive to maintain, so we will not implement it in the near future.

````{admonition} Data not in your username directory will be removed
:class: warning

Please always store your data and analysis in `/vol/local/<YOUR-USERNAME>`. Data stored elsewhere may be removed by administrators without prior notice.
````

:::{admonition} Program fail when HOME is full
:class: warning
:name: program-fail-home-full

When a program fails, always check the quota for your home directory. Some programs may attempt to write temporary files to your home directory, even if your analysis is being conducted elsewhere. If your home directory is full, this can cause errors that are not always clearly reported. To resolve this:

1. Check your quota using the `quota -s` command.
2. Clean up your home directory by removing unnecessary files.
3. Retry running the program.

If the issue persists, contact the administrator to temporarily increase your quota.
:::

## Plan and notify others before execute long program

Once you have done [program installation](./Install%20programs.md), it is time to plan a real job. Please follow these steps:

1. Check the "jobs-on-servers" channel in our Slack group for pinned messages.
2. Log in to the system and use htop or top to check for heavily running processes. Notify the channel if you see any anomalies.
3. Run your job. If it will take a long time, run it in a `screen` session and check its status.
4. Inform everyone else in the "jobs-on-servers" channel using this format:  
   "{Job type} on {SERVER} is using {number} cores, (approximately, optional) {number} ram, until ~(approximately) {time}."  
   For example, "phylophlan on BLIS is using 8 cores, 100 GB ram, until ~20 Nov 9:00." Pin this message if the job list is a bit long.
5. Once your job is done, edit the message to include a big "DONE" at the beginning and unpin it.

```{admonition} Rule of thumb
- For any job, leave at least 2 cores free.
- For short jobs, use as many cores as possible.
- For long jobs, use maximum half of the avaliable cores. If more cores are needed, notify everyone at least half hour in advance.
  For example, "PLANNING phylophlan on BLIS, is using 18 cores, 160 GB ram, from 19 Nov 20:00 till ~20 Nov 9:00."
```

## File transfer

Most basic skill for file transfer is to identify the location of your data and the destination. Terminology may differ, here we use:

- **Local**: the computer you are using to connect to the server, which can be your laptop or a desktop computer in the lab.
- **Server**: the computer you are connecting to, which is IBL servers or ALICE in our case.
- **Cloud**: the storage or computing resources provided by a third-party company, such as AWS, Google Cloud, Azure etc. Here it often refers to Research Drive.

### To and from cloud

Since Research Drive is the recommended location for storing research data, it will be easy to keep research data just in the cloud and do analysis on the server. To transfer data between them, check [how to upload data to Research Drive using Rclone](../rdm_howtos/ResearchDrive_commandLine.md).

### Between local and server

To transfer your files from or to the server, you need to have already set up an SSH connection BLIS (`blis`). For MobaXterm users, you can drag and drop in the app's file explorer. For MobaXterm, it is on the left.

SCP and `rsync` are recommended.

#### SCP

SCP for <u>s</u>ecure <u>c</u>o<u>p</u>y, or ssh cp, or safe cp...

When you have few files to copy, this is a good tool. It **cannot** resume transfer after transfer failure.

The syntax for `scp` is

```shell
scp [OPTIONS] [[user@]src_host:]file1 [[user@]dest_host:]file2
```

Same as command `ssh`, since you have already a config with user name and IP address for `Host blis` and `Host hpc1`, then the `[[user@]dest_host:]` part can be replaced with `blis:` or `hpc1:`.

```shell
# A file
scp path/to/file blis:/vol/local/username/
# Multiple files
scp path/to/fileA path/to/fileB blis:/vol/local/username/
# A directory, -r for recursive
scp -r path/to/dir blis:/vol/data/username
```

#### rsync

`rsync` is a more reliable tool for copying large datasets. It can continue the transfer from where it left off in case of interruption. (PowerShell does not have this program, use `scp` instead.)

The syntax for `rsync` is almost the same as `scp`:

```shell
rsync [OPTION...] SRC... [USER@]HOST:DEST
```

```shell
# Copy a directory to your own folder in the shared storage on BLIS
rsync -aP path/to/dir blis:/vol/data/username/
```

`-a` means archiving the directory, it will copy everything associated with the file, including its creation time, permissions etc. It implies `-rlptgoD`.  
`-P` to show progress.

## How to run long jobs

Your terminal connection to the server may be interrupted for various reasons, such as network issues, power failure, or simply closing the terminal by mistake. If you are running a long job in the terminal, it will be killed once the connection is lost. To avoid this, you can use tools like `screen` or `tmux` to run your job in a session that can be detached and re-attached later. This way, even if your connection is interrupted, your job will continue running in the background, and you can reconnect to it later to check its status or view the output.

Please try not use `tmux` or `screen` for long jobs on ALICE. All work should only run in a slurm queue.

### Using `tmux`

Tmux is a similar program, allows you to run a shell in the background, it should be available on all servers, let administrators know if not.

- `tmux new -s <session_name>` will create a session with the name you specify
- `Ctrl + b` is the magic key stroke in tmux, `Ctrl + b`, release the keys, and then press `d` will "detach" from the terminal and put it in the background.
- `tmux a -t <session_name>` will "re-attach" the session.

[A beginner's guide to tmux](https://www.redhat.com/en/blog/introduction-tmux-linux)

### Using `screen`

To use `screen`, simply execute the command, and a new shell will open. From here, you can execute commands as usual.

- `screen -S <session_name>` will create a session with the name you specify. You can have multiple sessions running at the same time, and this will help you to keep track of them.
- `Ctrl + a` is the majic key stroke in screen. `Ctrl + a`, release the keys, and then press `d`. This will "detach" from the terminal and leave the program running in the background.
- To re-attach to the session, use `screen -r <session_name>`.

## Run a command in an environment without activation

Sometimes you may need to run a program in a script, which may require multiple different software environments. You can activate them in a script, but this is not possible in Slurm system, for example running the command in a sub-shell, then you need to know how to run a program in one command without activating the environment in your script (when it does not work).

There are two ways, given as examples:

1. Recommended:

    For `micromamba`:

    ```sh
    cmd="eval \"\$(micromamba shell hook --shell=posix)\" && micromamba activate /vol/local/conda_envs/bakta && echo \$BAKTA_DB"
    echo $cmd
    eval $cmd
    ```

    For `conda`:

    ```sh
    cmd="eval \"\$(conda shell.posix hook)\" && conda activate /vol/local/conda_envs/bakta && echo \$BAKTA_DB"
    echo $cmd
    eval $cmd
    ```

2. Not recommended:

    It does not respect activation hooks (`activate.d`).

    For `micromamba`:

    ```sh
    cmd="micromamba run -p ~/genvs/bakta echo \$BAKTA_DB"
    echo $cmd
    eval $cmd
    ```

    Same for `conda`, just replace `micromamba run -p` with `conda run -p`.
