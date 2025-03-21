# IBL Linux Servers

*By C.Du [@snail123815](https://github.com/snail123815)*

IBL now have 3 workstation level PCs setup to server bioinformatics requirements within IBL. Every one is welcome to use and share their expertise within our community!

## Servers and specs

Except FRODO, all of servers are powered by [Rocky linux 8](https://rockylinux.org/about), a production-ready downstream version of Red Hat Enterprise Linux. FRODO is now [Rocky linux 9](https://rockylinux.org/news/rocky-linux-9-3-ga-release/). In the future, all servers will be upgraded to Rocky linux 9 to keep up with [ALICE](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519378/About+ALICE). Ethernet connection of all servers have a speed of 1000 Gb/s. There is no sub-network for the servers.

:::{NOTE}
Not all servers have [ECC memory](https://serverfault.com/questions/5887/what-is-ecc-ram-and-why-is-it-better), if you plan to run long analysis (>10 hours) on no-ECC-memory servers, be prepared for some random error even if your program is perfect.
:::

### BLIS

This is our main server, it has a shared local storage and use [conda environments (managed by `micromamba`)](Program%20setup.md) to manage softwares. Home directory has a quota of 20 GB for each user, no quota on shared local storage.

- Intel(R) Core(TM) i9-10980XE
  - @ 3.00GHz
  - 36 cores
- 256 GB memory (ECC)
- NVIDIA Quadro RTX 4000
  - 8 GB memory
- `/home` 1.8 TB SSD; Quota for each user: 20 GB
- `/vol/local` 7 TB HDD

### FRODO

The only Rocky linux 9 server. Shared local storage and `micromamba` enviroment are in line with BLIS. Home directory on SSD and has a quota of 20 GB for each user.

- AMD Ryzen Threadripper PRO 5975WX
  - @ 3.6GHz
  - 32 cores
- 64 GB memory (ECC)
- NVIDIA Quadro RTX A4500
  - 20 GB memory
- `/home` 1.8 TB SSD; Quota for each user: 20 GB
- `/vol/local` 10 TB HDD

### BILBO

Managed by [Paco lab](https://www.universiteitleiden.nl/en/staffmembers/paco-barona-gomez). No quota, no `micromamba` setup.

- AMD Ryzen Threadripper PRO 5955WX
  - @ 4.0GHz
  - 16 cores
- 32 GB memory (ECC)
- NVIDIA T1000
  - 8 GB memory

### DINGLAB01

Home directory quota, shared local storage, and `micromamba` are setup the same as [BLIS](#blis). Note, if you run your program using an environment on BLIS and want to use DINGLAB01, you need to setup the environment again. The architecture of the two machines are not completely the same.

- Intel(R) Core(TM) i9-10900 CPU
  - @ 2.80GHz
  - 10 cores (20 with Hyper-Threading, on)
- 32 GB memory (no ECC)
- `/home` 390 GB SSD; Quota for each user: 20 GB
- `/vol/local` 1 TB HDD

### VBLIS

Home directory quota, shared local storage, and `micromamba` are setup the same as [BLIS](#blis). Note, if you run your program using an environment on BLIS and want to use VBLIS, you need to setup the environment again. The architecture of the two machines are not completely the same.

- Intel(R) Core(TM) i9-10900 CPU
  - @ 2.80GHz
  - 10 cores (20 with Hyper-Threading, on)
- 32 GB memory (no ECC)
- `/home` 390 GB SSD; Quota for each user: 20 GB
- `/vol/local` 7 TB HDD
- `/vol/local1` 1 TB SSD

## Basic knowledge of using linux shell

It is easy to find information and basic training online. If you do not know which to follow, we recommend you to follow this to start:

[The Unix Shell for novice](https://swcarpentry.github.io/shell-novice/)

## Get access

You can access all three servers directly within Leiden University [Research Network](#what-is-research-network). From outside of Research Network, you need to jump through one of Leiden University ssh gateways. Please prepare your access to gateway before you make actual connections.

To ask for access to all servers, please send email to me (c.du\[at\]biology.leidenuniv.nl). Please let me know the following info:

- The user name you want to use for login. Only lower case letters and numbers allowed, start with letters. It is OK that you use the same user name as your ULCN account.
- Your first name
- Your last name
- The group you come from (your supervisor)
- The analysis you want to do (generally)

We will provide you information needed for accessing our servers.

Currently we are using Slack group "IBL-Bioinformatic" for discussion and most importantly, send notifications about all servers. You will get invitation link with your username and password.

## How to connect

SSH connection is the only recommended way to connect to our servers. To do that, please read through the following sections, then proceed to the tutorial [SSH access](../ssh%20access/ssh%20access.md).

## What is "Research Network"

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

You need your ULCN account.

Please fill in the form "Request access SSH-gateway" on [this page](https://www.staff.universiteitleiden.nl/ict/help-and-support/application-forms/application-forms/service-units/ict-shared-service-centre) and wait for approval. Then you can set it up follow [Manual Setting up SSH gateway PDF tutorial (login needed)](https://helpdesk.universiteitleiden.nl/tas/public/ssp/content/detail/knowledgeitem?unid=4b176453-ad3f-418f-9c15-40a11471de5f).

### ALICE gateway

Leiden University super computer cluster has its own gateway server, can be used also to connect Research Network. Please refer to [this page](../alice/alice_ibl.md#how-to-get-an-account) for more details. In principle, you still needs to be working or studying in Leiden University or have projects collaborating with us.

```{note}
The access to Research Network is not officially supported and you need to use it with your own risk!
```
