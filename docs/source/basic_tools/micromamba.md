# Setup `micromamba`

*By C.Du [@snail123815](https://github.com/snail123815)*

```{contents}
---
depth: 3
---
```

`micromamba` is a standalone environment manager, inheriting many features from `conda`. For what `micromamba` is and how to use it, [follow this link](https://mamba.readthedocs.io).

## IBL server users

The program is available, but please follow [execute programs tutorial](../IBL_servers/Execute%20programs.md) for how to use.

## Why choose Micromamba instead of Conda on BLIS?

[Instructions on how `micromamba` works](../IBL_servers/Install%20programs.md) on BLIS.

`micromamba` is a standalone reimplementation of `conda` package manager in C++. It provides the same command line interface as `conda`. In addition to `conda`:

1. Parallel downloading of repository data and package files using multi-threading
2. `libsolv` for much faster dependency solving, a state of the art library used in the RPM package manager of Red Hat (base of our Rocky linux 8), Fedora and OpenSUSE. This is extremely apparent when encountering some large repositories such as conda-forge.
3. Maintained actively by community, **NOT** Anaconda Inc.
4. Not python dependent. So 1, an environment without python is by default; 2, upgrade python version inside environment is easier.
5. `micromamba` executable relies only on the one executable file itself, very easy to maintain.

## Install `micromamba` from scratch

**Do NOT do this on any of our servers!** This tutorial is for you to install this in your own computer.

[Official installation guide](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)

For Linux, macOS, or Git Bash on Windows install with:

```sh
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

On Windows Powershell, use

```powershell
Invoke-Expression ((Invoke-WebRequest -Uri https://micro.mamba.pm/install.ps1 -UseBasicParsing).Content)
```

After installation, you should be able to run `micromamba` command in your terminal. Run the following command to check:

```shell
micromamba info
```

Output should show `micromamba` version and some other information, for example:

```
  libmamba version : 2.5.0
micromamba version : 2.5.0
      curl version : libcurl/8.18.0 OpenSSL/3.5.4 zlib/1.3.1 zstd/1.5.7 libssh2/1.11.1 nghttp2/1.67.0 mit-krb5/1.21.3
libarchive version : libarchive 3.8.5 zlib/1.3.1 bz2lib/1.0.8 libzstd/1.5.7 libb2/bundled
...
```

If you see errors, please try to re-initialize your shell by running:

```shell
micromamba shell init -s <your_shell> -r <your_micromamba_root_prefix>
```

Then **restart the terminal**.

::: {admonition} Note for GitBash users after python installation
In GitBash, `python` will not run directly as a console. If you want to do that, either install ipython or do the following and restart GitBash:

```shell
echo 'alias python="winpty python"' >> ~/.bash_profile
```

This will use "[winpty](https://github.com/rprichard/winpty)" to supply python with a Unix pty-master for communicating with Windows console. It works by starting a hidden console window and bridging between the console API and terminal input/output escape codes.
:::
