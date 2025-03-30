# Common questions

```{contents}
---
depth: 3
---
```

## Discussion group

Currently, our SLACK group (you get invitation from intake email) is recommended place to report issues and discuss usage. You have to report your long jobs there to let other users prepared. Please note it is a **public** place and **do not discuss sensitive data!**

We have a home on GitHub called [IBL-bioinfo](https://github.com/IBL-bioinfo). Any suggestions related to this documentation can also be reported over there, go to [issues](https://github.com/IBL-bioinfo/IBL-bioinformatics-wiki/issues) page of [this repository](https://github.com/IBL-bioinfo/IBL-bioinformatics-wiki).

Please note that there is **no dedicated** administrators for the IBL bioinformatics atelier, leave a message in above locations is much better than physically wandering around in the building to find us.

## Home directory quota

Every user have a disk space quota of 20 GB for their home directory. [Home directory quota explained](./Server%20configurations.md#home-directory-quota-explained)

[Do not analyse large dataset in your home directory](./Execute%20programs.md#do-not-analyse-large-dataset-in-your-home-directory)

[Program fail when HOME is full](./Execute%20programs.md#program-fail-home-full)

## Micromamba or Conda

We use [micromamba instead of conda](./Server%20configurations.md#micromamba-instead-of-conda) to manage software environments. [Explanation of why](../basic_tools/micromamba.md#why-choose-micromamba-instead-of-conda-on-blis)

## Shared storage

Our servers do not have a unified storage. Each server has its own storage space. Usually, system and home directory share a same SSD and data should be stored on the servers HDD. Note that the extra storage for data is mounted on `/vol/local/` or `/vol/local1/` etc. [Explained here](./Execute%20programs.md#run-analysis-in-shared-drive)

[Server configurations](./Intro.md#ibl-linux-servers)

## Shared environments

On servers with Micromamba setup, shared environments should be stored [in `/vol/local/conda_envs`](./Server%20configurations.md#shared-environments-location). It is in a shared location so every user should be able to use, but not modify. To modify, the user that last modified the environment should [set the permission correctly](./Server%20configurations.md#modify-an-environment-by-different-user)

We recommend to [use `~/.mambarc` file](./Install%20programs.md#setting-up-config-file) ([`~/.condarc` on ALICE](../alice/alice_ibl.md#group-shared-conda-environments)) to configure the behaviour of `micromamba` (`conda` on ALICE). Most important setting is `pkgs_dirs:`, it controls where to store the cache file when downloading packages, which could easily eat up all your home directory quota if not set. The specific location `/vol/local/.conda_cache/[USERNAME]` ensures easy cleaning up.
