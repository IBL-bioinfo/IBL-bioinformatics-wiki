# IBL bioinformatics servers administration tools

*By C.Du [@snail123815](https://github.com/snail123815)*

Repository (private): [IBL bioinformatics admin tools](https://github.com/IBL-bioinfo/admin_tools)

## Asked to create a user or a group?

First redirect them to [getting access](https://ibl-bioinformatics-wiki.readthedocs.io/IBL_servers/Intro.html#get-access) page, ask them to fill in [the form](https://forms.office.com/e/aTH5VSJdEL) linked there. You can use [this text](https://github.com/IBL-bioinfo/admin_tools/blob/main/new_user-information_request.md).

If they have already filled in the form, you can check the form responses and create the user or group accordingly.

Ask [@snail123815](https://github.com/snail123815) for permission to access the form responses if you don't have it.

Once you have the information, you use the `ibl_addgroup` or `ibl_adduser` command in `ipa_functions.sh` script to create the group or user. You can also use [`ipa` commands](ipa_commands.md) directly, but these functions will do some extra checks and steps for you.

```sh
source ipa_functions.sh
ibl_addgroup <GROUP-NAME> <DESCRIPTION>
ibl_adduser <USERNAME> <FIRST-NAME> <LAST-NAME> <PRIMARY-GROUP>
# Then on every server that enabled quotas, run:
ibl_addusers_quota <username_base> <total_users>
```

Once done, send email to the user and their PI to inform them that the account is created, and provide them with instructions on how to access the servers. You can use [this template](https://github.com/IBL-bioinfo/admin_tools/blob/main/new_user-welcome_letter.md). Please remember to change the username and password in the template.