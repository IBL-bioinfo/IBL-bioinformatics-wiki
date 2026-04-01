# Maintain the system

*By C.Du [@snail123815](https://github.com/snail123815)*

```{contents}
---
depth: 3
---
```

## Update the system from time to time

Keeping the system updated is important for security and stability. I recommend running the following commands on each server at least once a month, or whenever you receive security update notifications.

```sh
sudo dnf update -y
```

::: {caution}
If the server has NVIDIA drivers installed, please note whether the update includes NVIDIA driver updates, as these breaks the driver immediately and require a system reboot.
:::

## Reboot the system if necessary

If the update includes kernel updates or NVIDIA driver updates, please reboot the system as soon as possible to apply the updates.

Before rebooting, please check if there are any active users on the system and inform them about the reboot. It is not an easy job. The next section describes how to check active users and their sessions.

Please announce the reboot in advance in our Slack channel. Good communication is important to avoid unnecessary disruption to users.

## Check who has running sessions

### Active users only

`w` is just more verbose than `who`, they:

- Does not show background processes (tmux, screen, cron, daemons)
- Includes sessions that are technically active or “connected”
- Inactive **GUI sessions may appear** as display manager keeps the session alive

### See currently active login sessions

Ground truth:

```sh
loginctl list-sessions
```

More detail about a session `loginctl show-session <SESSION_ID>`

```sh
# When the session started:
loginctl show-session <SESSION_ID>
```

### Check what a user is running in a session

If a session is `closing`, most likely it is because of `tmux` or `screen`. Check what is holding the session:
(Use sudo if it is not your own session)

```sh
sid=<SESSION_ID>
uid=$(loginctl show-session $sid -p User --value)
scope=$(loginctl show-session $sid -p Scope --value)
systemd-cgls /sys/fs/cgroup/user.slice/user-$uid.slice/$scope
```

::: {warning}
Dangerous command alert: Do not kill any process without checking what it is. If you are not sure, ask for help in our Slack channel.
:::

```sh
loginctl terminate-session $sid
# If refuses, it will not kill if tmux is there.
loginctl kill-ssession <SESSION_ID> -s SIGKILL
# Then you need to kill tmux / screen using PID
kill <PID> <PID> ...
# add -9 to force it
kill -9 <PID>
```

### Check what a user is running in all sessions

```sh
uid=148600005
sudo systemd-cgls /user.slice/user-$uid.slice/
# If you need ground truth
sudo ps -u $uid -o pid,ppid,tty,stat,cmd
```

Problem service: `systemd-logind`

```sh
systemctl restart systemd-logind
```
