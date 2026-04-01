# Useful IPA commands

*By C.Du [@snail123815](https://github.com/snail123815)*

```{contents}
---
depth: 3
---
```

## Before you start

Run `kinit` with your own account before using any IPA administrative command:

```sh
kinit [USERNAME]
```

These commands assume your account already has the required IPA permissions.

## User management

### Check target user groups

Prepare the user's primary group first. If you create a user without assigning an existing group, IPA may create the user with `GID == UID`. That can result in `umask 002`, which is not appropriate for normal user accounts.

```{caution}
Create or confirm the lab group before adding the user, then use that group's GID as the user's primary group.
```

```sh
# Check the lab group and note its GID
ipa group-show [GROUP-NAME]
# If the group does not exist, try to find it by searching with a keyword
ipa group-find [KEYWORD]
# If the group does not exist, create it first
ipa group-add --desc="Group of [LAB-NAME or PI-NAME], abbreviated to ... because ..., work mainly with ..." [GROUP-NAME]
```

The lab group should be a member of `condablis` to ensure the members have access to the necessary software environments.

```sh
ipa group-add-member condablis --groups [LAB-GROUP-NAME]
```

### Find users by primary group

```sh
ipa user-find --gid [GID]
```

### Create a user

Then create the user with the lab group as the primary group:

```sh

# Create the user with that group as the primary group
ipa user-add [USERNAME] \
    --first [FIRST-NAME] \
    --last [LAST-NAME] \
    --random \ # this creates a random password
    --gid [GID] \
    --shell /usr/bin/bash
# !!! Must do: !!! Add the user to all required groups
# Although when --gid is set, you still need to add the user to the group explicitly
ipa group-add-member [GROUP-NAME-1] --users [USERNAME]
```

Each new user should belong to their lab group, and thus belong to the `condablis` group. Do not add users directly to `condablis` group.

### Change a user's default shell

Only do this when asked by the user. The default shell is `bash`, but some users may prefer `zsh` or other shells. To change the default shell, use:

```sh
ipa user-mod [USERNAME] --shell=/usr/bin/zsh
```

## Group management

### Create a group

```sh
ipa group-add --desc="Explain why this group exists" [GROUP-NAME]
```

### Add members to a group

Add users:

```sh
ipa group-add-member [GROUP-NAME] --users [USERNAME-1] --users [USERNAME-2]
```

Add another group as a member (for `condablis`, we add lab groups as members of it):

```sh
ipa group-add-member [GROUP-NAME] --groups [GROUP-NAME-1]
```

### Check group information

Show information about a group:

```sh
ipa group-find [GROUP-NAME]
```

Show all groups a user belongs to:

```sh
ipa group-find --user=[USERNAME]
```

## Password policy

### Show the current policy

```sh
ipa pwpolicy-show
```

### Set password expiration

Set the password lifetime to 730 days:

```sh
ipa pwpolicy-mod --maxlife=730
```