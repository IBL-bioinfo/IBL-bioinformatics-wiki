# Install programs

*By C.Du [@snail123815](https://github.com/snail123815)*

For most high-performance computing (HPC) servers, users do not have root access to install software globally. Instead, they can create their own **environments** and install software within those **environments**. This approach allows users to manage their software dependencies without affecting other users on the same server.

This tutorial provides guidance of creating environments and install programs in the created environments using `micromamba`. To install programs that are not available in any `conda` repositories, please ask administrators for help.

```{contents}
---
depth: 3
---
```

## What is an environment

An environment created by `conda`, `micromamba`, or pyvenv is essentially just a folder/directory on the disk. This directory contains configuration files and dependency programs. It has a special structure to allow environment manager programs (`conda`/`micromamba`/`pyvenv`) to read.

[Read package management concepts](../basic_tools/package_management_concept.md) for more detail.

Do not change any content in an environment directory manually, unless you understand how environment manager works.

## Install a program

New users on BLIS should have `micromamba` ready to use directly. You should see your prompt as:

```sh
(base) [user@blis ~]$ 
```

The `(base)` in front means you have the **base** environment activated, which located in `~/.micromamba`. Note this is BLIS only. If this is not seen, please make sure you have [`micromamba` ready to use](./Execute%20programs.md#prepare-micromamba). Before setting up virtual environments, it is highly recommended to setup a `~/.mambarc` file with the following content (new users on BLIS should have it already, check by yourself). It is explained in the later [section](#setting-up-config-file).

```YAML
envs_dirs:
  - /vol/local/conda_envs
pkgs_dirs:
  - /vol/local/.conda_cache/[USERNAME]
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
```

Create an environment to host the software or a pipe line you want to run. Then you have all control over the environment you created.

````{caution}
Do not use `-n` or `--name` to create an environment, it will be created in your home directory by default, which has a quota on disk space. Putting the environment on the shared drive as shown below does not reduce your home directory quota.
````

```{code-block} shell
---
caption: This block includes prompt, select command to copy
---
# 0. Make sure you have your shell initiated with micromamba
(base) [user@blis ~]$

# 1. Create environment called multi-omics and activate it
(base) [user@blis ~]$ micromamba create -p /vol/local/conda_envs/multi-omics
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/multi-omics

# 2. Install software, eg. python
(/vol/local/conda_envs/multi-omics) [user@blis ~]$ micromamba install -c conda-forge python
```

I guess you have noticed that we have setup the channels in `~/.mambarc`, so most of the time you can omit the `-c conda-forge` part for explicitly specifying the channel where the software comes. In the example above, python will be installed from `conda-forge`.

````{tip}
I usually create a "soft link" to `/vol/local/conda_envs/` in home directory for easier access to all the environments. For example,

```sh
ln -s /vol/local/conda_envs/ ~/genvs
```

Then I can replace all `/vol/local/conda_envs/` with `~/genvs`, much simpler.

Advanced method (**do not do** if you don't know what `ln -s` means and its restrictions) is to soft link the shared environment directory to `micromamba` base directory:

```sh
ln -s /vol/local/conda_envs/ ~/micromamba-base/envs
```

This needs to be done when the target directory does not exist (before creating any "named" environment). The advantage of this method is that you can create environment in the shared environment directory using `-n` and may be more compatible with most program tutorial (the old ones usually assume you have sudo rights and unlimited HOME directory, which is not the case in any of the server systems.) Use this method with caution!
````

### Do not follow tutorial with yml/yaml file

`.yml` or `.yaml` file format is usually configuration files written with a variant of markup language, describing the required programs and usually their versions, i.e. *dependencies*.

Many times you will find a tutorial to setup a `conda` environment by `conda env create -f minimotif.yml minimotif`. Please **DO NOT** follow this by simply replacing `conda env` with `micromamba`.

In these cases, the `.yml` file usually looks like:

```YAML
name: MiniMotif
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - _libgcc_mutex=0.1
  - _openmp_mutex=4.5
  - alsa-lib=1.2.8
  - attr=2.5.1
  - biopython=1.81
  - ...
```

You need to open this file using a text editor, remove the `name:` line and save the file. The `name:` line is telling `conda` or `micromamba` to install the environment with `-n` switch, or install the dependencies it is not compatible with `-p` switch.

Then create the environment:

```{code-block} shell
---
caption: This block includes prompt, select command to copy
---
# 1. Create environment using -p
(base) [user@blis ~]$ micromamba create -p /vol/local/conda_envs/MiniMotif
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/MiniMotif
# 2. Install all dependencies using the .yml file
(/vol/local/conda_envs/MiniMotif) [user@blis ~]$ micromamba install -f minimotif.yml
```

Now it should do the installation, follow the screen to continue.

Why not combine into one single command? Because `-p` and `-f` parameters are not compatible.

After installation, you can try your program to see if the help function works:

```{code-block} shell
---
caption: This block includes prompt, select command to copy
---
(/vol/local/conda_envs/MiniMotif) [user@blis ~]$ python minimotif.py -h
usage:
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
Generic command:
     minimotif.py -i [binding_profiles] -G [genome] -O [outdir]
__________________________________________________________________________
Mandatory arguments:
    -G  Provide a genbank file of the genome of interest for TFBS scanning
    ...
```

Do not forget to **deactivate** your environment before doing anything else, unless you know what you are doing. Your current activated environment is shown in the parenthesis before your command line. To deactivate:

```{code-block} shell
---
caption: This block includes prompt, select command to copy
---
(/vol/local/conda_envs/MiniMotif) [user@blis ~]$ micromamba deactivate
(base) [user@blis ~]$
```

## Setting up config file

The program `micromamba` uses a config file located in your home folder: `~/.mambarc` to store your specific configurations. Well `micromamba` *not only* check `~/.mambarc` file, but also uses `~/.condarc`, one of them is enough. (The later is used by `conda`)

The config file has few convenient options. On BLIS, please put these contents in the config file:

```YAML
envs_dirs:
  - /vol/local/conda_envs
pkgs_dirs:
  - /vol/local/.conda_cache/USERNAME
```

- `env_dirs` will allow `micromamba env list` command to list all environments including our shared environments. (ignore this line if you have soft linked it to `~/micromamba_base/envs`)
- `pkgs_dirs` set the cache dir, it is a easy-to-clean location.

You can also add after the above contents:

```YAML
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
```

- `channels` will allow you to skip -c option when installing packages
- `auto_activate_base` will activate your base environment, by this, you will be using eg. python from your base environment rather than a system one.

If you need more information on how to use `micromamba` on your own machine, please refer to our [`micromamba` instruction](../basic_tools/micromamba.md).

## Premissions of shared environments on BLIS

All files generated by `micromamba`, including all environments created, by default belong to the group `condablis`. All group members can activate these environments. **Only** the owner who created the environment can add or remove package. If you want to let others change your environment, you need to specifically change the permission:

```sh
chmod -R g+w /vol/local/conda_envs/yourEnvironment
```

**Anyone who changed this environment should do this *again*** for others to change it. Or, the owner can remove this permission after changing:

```sh
chmod -R g-w /vol/local/conda_envs/yourEnvironment
```

This restriction is due to the limitations of the Linux file system, which are intentional for safety reasons.

## Monitoring disk space

Disk space is a shared resource on our servers, and it is crucial to monitor it regularly to ensure smooth operation. Here are some tips for monitoring disk space related with your environments and installed programs:

1. Use `df -h` to check the overall disk usage.
    - `/home` is the home directory, which has a quota for each user.
    - `/vol/local` and `/vol/local1` etc. are the shared local storage, which has no quota but shared by all users. Be mindful of others when using it.
2. Use `du -sh /path/to/your/environment` to check the size of your `conda` environment.
3. Regularly clean up unused environments and packages to free up space.
    - `micromamba clean -a` to clean up all unused packages and caches.
    - You can simply remove the environment directory to remove an environment.
4. Be **mindful of large files generated by the package**, such as downloaded database, logs, temporary files, and output data. Regularly check and clean these files if they are no longer needed.
    - Well designed programs usually do not use the environment directory to store these files, but some do. Be aware of the programs developed by only a few people, which may not have good design and documentation. If you are not sure where the program stores these files, ask the developers or administrators for help.
    - Some programs have options to specify the location of these files, you can set it to a location with enough space, `shared_db/` if it can be used by other program.
    - Some programs fail because of insufficient space, often due to storing data in your HOME directory, which has a quota.
      - These files may be config, data files, or temporary files.
      - Consult with administrators for how to change the location of these files. Possible solutions include:
        - Change the config file of the program or use environment variables to specify the location of these files.
        - Use a soft link to your shared local storage.
        - Change the default location of these files by changing the program code, if you have the permission to do so.
5. Consult with your team and administrators for how to store and use database from shared database location, to prevent unnecessary duplication.
