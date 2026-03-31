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

Check node status and who is using the node:

```bash
sinfo -p gpu_ibl
squeue -p gpu_ibl
```

If you find the GPU is not available, please contact the user who is using it or contact the admin to check if it is a problem of the node. This is the **major difference** between this node and IBL servers. **A job will have complete possession of the GPU it requested on ALICE, including our private node, but not on IBL servers.** Advantage is that jobs on ALICE will not be affected by other users, but the disadvantage is that you may have to wait for a long time if the node is occupied by others. So please be patient and communicate with other users if necessary.

### Group shared dir

Currently ALICE is [providing enough storage](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519552/Storage+on+ALICE#Summary-of-available-file-systems) for your temporary data in your `/home/<username>` dir, but it can not be shared with others. To share data with other IBL colleagues, we have created a shared directory located in `/data1/projects/pi-vriesendorpb/`. Please use this directory for any data that can be shared with others.

Please create a folder with your username in our group shared folder for your data.

`/data1/projects/pi-vriesendorpb/<ULCN_USERNAME>`

This is Project directories on ALICE, [rules apply](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519552/Storage+on+ALICE#Project-directories).

The directory is **not** backed up. Please only store data that you think very important to keep.

### Shared Conda environments

For software that is:
1. Not available as a module on ALICE, and
2. Can be installed via Conda, and
3. May be useful for other IBL colleagues

Load Conda module:

```shell
module load Miniconda3
```

Conda usually creates environments and stores packages in your home directory, which is not shared with others. Add this to your `.condarc` file to add location of Conda environments:

```yaml
envs_dirs:
  - /data1/projects/pi-vriesendorpb/condaEnvs
```

Example `.condarc` file is shown below. You can also add other channels to the file.

```YAML
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
show_channel_urls: true
envs_dirs:
  - /data1/projects/pi-vriesendorpb/condaEnvs
```

If the software in your target environment is designed properly, others should be able tocan use the environment. Any software which <u>on its run time</u>, write data to the environment directory will fail for other people, as they don't have write permissions to the directory.  If that is the case, or **if you want others to update your environment**, you need to give proper permissions to the environment directory:

`chmod g+w -R [ENVDIR]`

Keep in mind that if program write data to the environment directory, you may be sharing your intermediate data or result completely with others whenever you use this environment. You may:

1. Consider to not share this environment, by creating the environment in your home directory (simply run `conda create -n [ENVNAME] [PACKAGES]`)
2. Report the issue to the developers.

Generate a `*.yaml` file with all dependencies next to the environment when you think it is working.

Be cautious if your environment involves R and R packages. Do some extra tests.

### Storage Quota

To get your quota on SCRATCH, use

`beegfs-ctl --getquota --uid <ULCN_USERNAME>`

To get status of group quota, use

`beegfs-ctl --getquota --gid pi-vriesendorpb`

## Transfer data

Refer to [Run jobs - file transfer](../IBL_servers/Execute%20programs.md#file-transfer).