# Common questions

```{contents}
---
depth: 3
---
```

## Discussion group

If you have suggestions or inquiries, our Slack workspace is the best place to reach out. You will receive an invitation once your username and password are send to you.

For long-running analyses, please notify the **#jobs-on-servers** channel so other users can prepare accordingly.

Keep in mind that the Slack workspace is public, so refrain from sharing any sensitive data.

On GitHub, we have established an organization called **[IBL-bioinfo](https://github.com/IBL-bioinfo)**. If you have any suggestions regarding this documentation, please create a new issue on the [issues](https://github.com/IBL-bioinfo/IBL-bioinformatics-wiki/issues) page of [this repository](https://github.com/IBL-bioinfo/IBL-bioinformatics-wiki).

Remember, there are no dedicated administrators for the IBL bioinformatics atelier, so leaving a message in the mentioned places is more effective than trying to find someone in person.

## Home directory quota

Every user have a disk space quota of 20 GB for their home directory. [Home directory quota explained](./Server%20configurations.md#home-directory-quota-explained)

[Do not analyse large dataset in your home directory](./Execute%20programs.md#do-not-analyse-large-dataset-in-your-home-directory)

[Program fail when HOME is full](#program-fail-home-full)

## Micromamba or Conda

We use [micromamba instead of conda](./Server%20configurations.md#micromamba-instead-of-conda) to manage software environments. [Explanation of why](../basic_tools/micromamba.md#why-choose-micromamba-instead-of-conda-on-blis)

## Shared storage

Our servers do not have a unified storage. Each server has its own storage space. Usually, system and home directory share a same SSD and data should be stored on the servers HDD. Note that the extra storage for data is mounted on `/vol/local/` or `/vol/local1/` etc. [Explained here](./Execute%20programs.md#run-analysis-in-shared-drive)

[Server configurations](./Intro.md#ibl-linux-servers)

## Shared environments

On servers with Micromamba setup, shared environments should be stored [in `/vol/local/conda_envs`](#shared-environments-location). It is in a shared location so every user should be able to use, but not modify. To modify, the user that last modified the environment should [set the permission correctly](./Server%20configurations.md#modify-an-environment-by-different-user)

We recommend to [use `~/.mambarc` file](./Install%20programs.md#setting-up-config-file) ([`~/.condarc` on ALICE](../alice/alice_ibl.md#group-shared-conda-environments)) to configure the behaviour of `micromamba` (`conda` on ALICE). Most important setting is `pkgs_dirs:`, it controls where to store the cache file when downloading packages, which could easily eat up all your home directory quota if not set. The specific location `/vol/local/.conda_cache/[USERNAME]` ensures easy cleaning up.
