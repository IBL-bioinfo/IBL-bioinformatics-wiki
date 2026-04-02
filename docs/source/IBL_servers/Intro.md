# IBL Linux Servers

*By C.Du [@snail123815](https://github.com/snail123815)*

To serve bioinformatics requirements within IBL, we have three tiers of computing infrastructure:

1. IBL servers. Now contains 3 workstation level PCs setup.
2. One private GPU node in the Leiden University super computer cluster ALICE, not restricted to GPU work.
3. ALICE cluster, which is a shared resource for all Leiden University researchers, with a large number of CPU cores and GPU nodes. Additional charge will apply.

For more demanding works, we can also apply for national super computer resources, such as [Snellius](https://userinfo.surfsara.nl/systems/snellius). However, these resources are not dedicated to IBL and the application process is more complicated, so we will not cover them in this documentation.

```{contents}
---
depth: 3
---
```

## IBL Servers and specs

All IBL servers run on [Rocky Linux 9](https://rockylinux.org/news/rocky-linux-9-3-ga-release/), a production-ready downstream version of Red Hat Enterprise Linux.

Most servers have local storage mounted on `/vol/local/`, for both data and programs. All home directories are located on a dedicated SSD partition and have a quota for each user. Additional storage is mounted on `/vol/local1/` and `/vol/local2/`, etc.

:::{NOTE}
**NOT** all servers have [ECC memory](https://serverfault.com/questions/5887/what-is-ecc-ram-and-why-is-it-better), if you plan to run long analysis (>10 hours) on no-ECC-memory servers, be prepared for some random error even if your program is perfect.
:::

### BLIS

Has a shared local storage and use [software environments managed by `micromamba`](./Install%20programs.md) to manage software. Home directory has a quota of 50 GB for each user, no quota on shared local storage.

Conda environments (created by `micromamba`), located and should be created in `/vol/local/conda_envs/`; `conda` cache should be stored in `/vol/local/.conda_cache/[USER]`.

- Intel(R) Core(TM) i9-10980XE
  - @ 3.00GHz
  - 18 cores (36 threads)
- 256 GB memory (no ECC)
- NVIDIA Quadro RTX 4000
  - 8 GB memory
- `/home/` 2 TB SSD; Quota for each user: 50 GB
- `/vol/local/` 7 TB HDD

### BILBO

Home directory quota, shared local storage, and `micromamba` are setup the same as [BLIS](#blis). Note, if you run your program using an environment on one server and want to use another one, you need to setup the environment again.

- AMD Ryzen Threadripper PRO 5955WX
  - @ 4.0GHz
  - 16 cores (32 threads)
- 256 GB memory (ECC)
- NVIDIA T1000
  - 8 GB memory
- `/home/` 1 TB SSD; Quota for each user: 50 GB
- `/vol/local/` 12 TB HDD
- `/vol/local1/` 4 TB SSD
- `/vol/local2/` 4 TB HDD

### DINGLAB01

Home directory quota, shared local storage, and `micromamba` are setup the same as [BLIS](#blis).

- Intel(R) Core(TM) i9-10900 CPU
  - @ 2.80GHz
  - 10 cores (20 threads)
- 32 GB memory (no ECC)
- `/home/` 400 GB SSD; Quota for each user: 20 GB
- `/vol/local/` 1 TB HDD

### VBLIS

Home directory quota, shared local storage, and `micromamba` are setup the same as [BLIS](#blis).

- Intel(R) Core(TM) i9-10900 CPU
  - @ 2.80GHz
  - 10 cores (20 threads)
- 32 GB memory (no ECC)
- `/home` 400 GB SSD; Quota for each user: 20 GB
- `/vol/local` 7 TB HDD
- `/vol/local1` 1 TB SSD

### FRODO for private use

This machine is, in principle, dedicated to the Paco group and managed by [Paco lab](https://www.universiteitleiden.nl/en/staffmembers/paco-barona-gomez). You do not have access by default. Ask an admin for more info if necessary.

- AMD Ryzen Threadripper PRO 5975WX
  - @ 3.6GHz
  - 32 cores
- 64 GB memory (ECC)
- NVIDIA Quadro RTX A4500
  - 20 GB memory
- `/home` 1.8 TB SSD; Quota for each user: 100 GB
- `/vol/local` 10 TB HDD

## Private GPU node in ALICE cluster

The `node888` is a GPU node under partition `gpu_ibl` in ALICE cluster that is dedicated to the whole of IBL. Only IBL members have access to this node. This server is setup for educational purposes, but it can also be used for production work. Educational work will be notified to all users in advance in the Slack channel `#jobs-on-servers` and will have higher priority than production work.

- AMD Zen 4 architecture EPYC 9534 CPU &times; 2
  - @ 2.45GHz, boost up to 3.7GHz
  - 64 cores each (128 threads each)
- Nvidia A5000 Ada GPU &times; 2
  - 32 GB memory each
- 640 GB memory (ECC)
- 14 TB scratch space:
  - 7 TB PCIe Gen4 &times;4 NVMe SSD &times; 2
  - RAID 0 for maximum performance, reaching ~ 12.4 GiB/s read and 7.7 GiB/s write
  - No redundancy, but it is scratch data space anyway

Check [ALICE WIKI](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519378/About+ALICE) for detailed documentation about ALICE cluster.

Check [IBL on ALICE](../alice/alice_ibl.md) for IBL specific information.

## Basic knowledge of using linux shell

It is easy to find information and basic training online. If you do not know which to follow, we recommend you to follow this to start:

[The Unix Shell for novice](https://swcarpentry.github.io/shell-novice/)

## Get access

[Research Network](#what-is-research-network)

To ask for access to all servers, please fill in [this form](https://forms.office.com/e/aTH5VSJdEL).

Once you have submitted the form, we will provide you information needed for accessing our servers.

Currently we are using Slack group "IBL-Bioinformatic" for discussion and most importantly, organizing and planning long jobs in `#jobs-on-servers` channel. You will get invitation link together with your IBL server username and password.

## Usage guidelines

Remember: feel free to test and explore — the servers are built to be robust. If you somehow break something, that’s our problem, not yours!

However, please keep in mind that this is a shared resource. To ensure fair use, follow these guidelines:

1. Register using your real name
2. Communicate via the designated discussion group
3. Monitor your use of key resources:
   - CPU cores
   - Memory
   - Network bandwidth and connections
   - **Storage space**
     - Use your home directory for small files and programs
     - Use shared local storage for large files and programs, but be mindful of others
     - Remove files you no longer need to free up space
     - Keep an eye on the environment you created with `micromamba`, especially if they download large files during installation.
     - Check [Monitoring disk space](./Install%20programs.md#monitoring-disk-space) for tips on how to monitor and manage disk space.
4. Inform others when a significant number of resources are needed
5. Report any issues promptly

During your work, you may encounter limits due to restricted administrative rights — this is part of the training, and we are here to help. You will learn how to install and manage software as a non-administrator. This ensures the servers remain stable and available to all users.

## How to connect

SSH connection is the only recommended way to connect to our servers. To do that, please read through the following sections, then proceed to the tutorial [SSH access](../ssh%20access/ssh%20access.md).

## What is Research Network

Our university's network is called **Research Network**, which is a "private" network that is isolated from the world wide web (Internet). This isolation is for security reasons.

The IBL servers are setup inside Leiden University's **Research Network**, which means intranet. To protect intranet from internet, gateway servers are hosted by Leiden University. Connecting IBL servers from internet can be done only through connecting to the gateway first and then from gateway to IBL servers. Of course, if you are inside our Leiden University intranet, you can make direct connections to IBL servers.

Without being on the Research Network, your computer cannot connect our servers using the given IP addresses.

### Determine your network location

If you are outside of Research Network, you cannot communicate with our servers through the IP addresses in the email.

INSIDE:

Only university managed PCs or laptops are allowed to be inside Research Network.

- University managed PC that is connected through an ethernet port
- University managed laptops that:
  - Connected to the “NUWD-Laptop” WiFi access point
  - Connected to an ethernet port

OUTSIDE:

- Using your own device:
  - Even if it is connected to an ethernet port (usually as BYOD connections)
  - Connected to WiFi access point "eduroam"
- At home, even if you are using University managed laptop
- Note that "eduVPN" does not help you to connect IBL servers. Probably because our servers are not registered.

## Leiden University gateways

The concept of "gateway server" is explained [here](../ssh%20access/ssh%20access.md#ssh-gateway). Basically, the gateway servers are setup for security reasons. From Internet, one has to pass through the gateway servers to make SSH connections to any computer or server inside Research Network.

Leiden University has two different gateway servers which uses different account systems.

### Leiden University general purpose gateway

You need your ULCN account. You do not need to specifically apply for it.

You can set it up follow [Manual Setting up SSH gateway PDF tutorial (login needed)](https://helpdesk.universiteitleiden.nl/tas/public/ssp/content/detail/knowledgeitem?unid=4b176453-ad3f-418f-9c15-40a11471de5f).

### ALICE gateway

For people who have [eduVPN](https://eduvpn.org/) access, you do not need to use the gateway server to connect to ALICE cluster. After connecting to eduVPN, you can directly connect to ALICE login nodes.

If you cannot access eduVPN, Leiden University super computer cluster has its own gateway server, can be used also to connect Research Network. Please refer to [this page](../alice/alice_ibl.md#how-to-get-an-account) for more details.

```{note}
The access to Research Network is not officially supported and you need to use it with your own risk!
```
