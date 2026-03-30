# ALICE server from Leiden University

*By C.Du [@snail123815](https://github.com/snail123815)*

[ALICE (Academic Leiden Interdisciplinary Cluster Environment)](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519378/About+ALICE) is the high-performance computing (HPC) facility of Leiden university and LUMC. It is a shared resource for all Leiden University researchers, with a large number of CPU cores and GPU nodes. Additional charge will apply.

## How to get an account

Please read and follow the instructions:

[Get an account on ALICE](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519441/Getting+an+account+on+ALICE)

[Connecting to ALICE](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519483/Connecting+to+ALICE)

If you are from IBL Leiden university, please also ask for shared folder access. Our shared folder is under PI name: [Bastienne Vriesendorp](https://www.universiteitleiden.nl/en/staffmembers/bastienne-vriesendorp), and please CC your request to her.

## IBL on ALICE

We have strong connection with ALICE management and support team, please contact via Slack team or any open office day if you have any questions regarding ALICE cluster.

### Private GPU node in `gpu_ibl` partition

We have one GPU node `node888` in ALICE cluster that is dedicated to the whole IBL. Users with group `bio` can access this node. This server is setup for educational purposes, but it can also be used for production work. Educational work will be notified to all users in advance in the Slack channel `#jobs-on-servers` and will have higher priority than production work.

Use this in your slurm script to specify the partition and use only one GPU on this node:

```bash
#SBATCH --partition=gpu_ibl
#SBATCH --gres=gpu:1
```

Check who is using the node:

```bash
sinfo -p gpu_ibl
squeue -p gpu_ibl
```

If you find the GPU is not available, please contact the user who is using it or contact the admin to check if it is a problem of the node.

### Group shared dir

Please use a folder of your user name in our group shared folder for your data.

`/data1/projects/pi-vriesendorpb/<ULCN_USERNAME>`

This is Project directories on ALICE, [rules apply](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519552/Storage+on+ALICE#Project-directories).

The directory is backed up. Please only store data that you think very important to keep. Otherwise, use

`/data1/<ULCN_USERNAME>`

or simply use the soft link

`~/data`

As the quota is much higher according to [ALICE WIKI](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519552/Storage+on+ALICE#The-scratch-shared-file-system-on-%2Fdata1).
 
We cannot overwrite data that others created.
 
### Group shared Conda environments

Load Conda module:

```shell
module load Miniconda3
```

Your `HOME` dir is limited to a quota of 15 GB, as a result, we created a shared dir for our group and we can use and create shared Conda environments, just like [on BLIS](../IBL_servers/Execute%20programs.md)
`/data1/projects/pi-vriesendorpb/condaEnvs`

TEMP/CACHE dir for pkgs:

`/data1/projects/pi-vriesendorpb/.condaTemp/<username>`

Want others to change your environment? Do

`chmod g+w -R [ENVDIR]`

Generate a `*.yaml` file when you think your environment is working.
 
Example `.condarc` file

```YAML
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
show_channel_urls: true
envs_dirs:
  - /data1/projects/pi-vriesendorpb/condaEnvs
pkgs_dirs:
  - /data1/projects/pi-vriesendorpb/.condaTemp/<username>
```
 
Be cautious if your environment involves R and R packages. Do some extra tests.

### Storage Quota

To get your quota on SCRATCH, use

`beegfs-ctl --getquota --uid <ULCN_USERNAME>`

To get status of group quota, use

`beegfs-ctl --getquota --gid pi-vriesendorpb`

Yes, we only have 600GB, and it is almost full. Please do not store data on our shared space unless you want to share it.

## Transfer data

Refer to [Run jobs - file transfer](../IBL_servers/Execute%20programs.md#file-transfer).