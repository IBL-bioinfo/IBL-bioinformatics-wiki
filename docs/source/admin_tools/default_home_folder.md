# Home directory template for new users on IBL servers

*By C.Du [@snail123815](https://github.com/snail123815)*

To automatically apply custom home directory template when IPA users first log in to our servers.

FreeIPA uses PAM (Pluggable Authentication Modules) system to manage users, this repository is intended to use its automation processes to achieve our goal.

Repository (private): [iblservers home directory setup](https://github.com/IBL-bioinfo/iblservers-home-directory-setup)

::: {caution}
This repository uses git LFS, run `git lfs install` in the repository directory before proceeding, you may need to install `git-lfs` package in the system or your environment.
:::

For how to setup in a new server, see [Auto home directory setup](https://github.com/IBL-bioinfo/iblservers-home-directory-setup/blob/main/Auto-home-directory-setup.md)

## Actual execution flow

1. During login, PAM will execute a set of routines, which will include our pam_setup_homedir.sh.
2. `pam_setup_homedir.sh` will do several checks and get the user and group name. If the user has no HOME directory, or has no `~/.home_initialized` flag file, it will call `convert_home_dir.sh` with appropriate parameters. `/home/.home_template/` will be used.
3. `convert_home_dir.sh` will then
   - Make a copy of `.home_template`
   - Make a copy of existing home directory
   - Unzip the `vscode-server.tar.xz` to `.vscode-server`
   - Prepare `.mambarc` for `micromamba,` the cache directory will be created for the user
   - Create a user directory in shared storage, make a soft link `data` in HOME
   - Initialize `micromamba` environments for the user, which will create `~/.micromamba` as the base environment, and setup `~/.mambarc`.