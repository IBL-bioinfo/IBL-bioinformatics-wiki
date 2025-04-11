# Run RStudio in web browser

*By C.Du [@snail123815](https://github.com/snail123815)*

About running RStudio-server on BLIS and access an RStudio in your browser.

:::{admonition} TLDR
Activate the environment `/vol/local/conda_envs/rstudio-web` and run `rstudio-web`, connect to it according to the instructions shown on the screen.
:::

```{contents}
---
depth: 3
---
```

## Why you need it

If you are using your own computer, just install RStudio by yourself and use that. This page is only about how and why you run it on our server.

If you have a large project that requires any of the following:

1. Many CPU cores
2. Large amount of memory (below the maximal of the server of course)
3. Runs for a long time
4. Read or write large amount of data
5. RStudio is the only way to run the analysis

Then you should consider do it on our servers.

## Server configuration for RStudio

RStudio-server is not directly installed on our servers, it will be run in a container using *apptainer* instead.

This is because installing RStudio-server is complex and should be done on a dedicated server. Running an RStudio-server instance means that it should provide service to multiple users, it will conflict with our account management settings. Or it requires independent account setup.

Our method starts a server for each user instance, exposing it to a random port. Users are protected not only by the unknown port, also by a random password that is generated per session. If the random port happens to be identical with another user, restart the server will generate another port for you.

### RStudio Execution

- The RStudio server runs within an Apptainer container
- When launched, you'll receive:
  - A randomly generated port number
  - A randomly generated password for your session
  - SSH tunneling instructions for remote access
  - Direct URL for local access
- You can specify CPU cores and custom port numbers with options like `--cpus` and `--port`

### Temporary Files in Home Directory

Once connected, you may find your home directory becomes `/home/rstudio`, this is the home directory in the container, which linked to your actual home directory. Do not panic.

You will find **NO** `/vol/local` directory in the container, but I made `vol-local-entry-RSTUDIO` directory in your home directory, which is a link to `/vol/local`

- Two temporary files will be created in your home directory:
  - `custom_rsession.conf`: Configuration for your R session
  - A symlink to `/vol/local` at `~/vol-local-entry-RSTUDIO`
- These files are automatically removed when your session ends

### R Package Installation

This is to prevent hitting home directory quota wall.

- R packages are installed to `/vol/local/$USER/Rstudio/$R_VERSION`
- This location persists between sessions
- The R version is automatically detected from the container
- Using this location keeps your packages organized by R version

### R Session Workspace

This is to prevent hitting home directory quota wall.

- Your R workspace defaults to `/vol/local/$USER/RStudio/workspace`
- This prevents clutter in your home directory
- The `.RData` and history files are stored in this location
- This directory is created automatically if it doesn't exist

### CPU Core Allocation

This is not an optimal solution. When certain CPUs are bound, they cannot be changed. But system will allocate CPUs for most other programs, so only possible conflict is from another instance of RStudio-server. This is partially solved by maintaining a CPU usage file, by reading this file, the script knows which CPUs are being used and which are not, thus allocating available CPUs to the new instance.

- By default, your session uses all available CPU cores
- You can limit CPU usage with `--cpus N` to use N cores
- You can specify exact cores with `--cpus 0,2,4` syntax
- The system manages core allocations to prevent conflicts between users
- Allocated cores are automatically released when your session ends
