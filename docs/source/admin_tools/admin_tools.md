# IBL bioinformatics servers administration tools

*By C.Du [@snail123815](https://github.com/snail123815)*

Repository (private): [IBL bioinformatics admin tools](https://github.com/IBL-bioinfo/admin_tools)

## Asked to create a user or a group?

You can use this [template email](https://github.com/IBL-bioinfo/admin_tools/blob/main/new_user-information_request.md). The email first redirects them to the [getting access](https://ibl-bioinformatics-wiki.readthedocs.io/IBL_servers/Intro.html#get-access) page and asks them to fill in [the form](https://forms.office.com/e/aTH5VSJdEL). Ask [@snail123815](https://github.com/snail123815) for permission to access the responses.

Once the user has filled in the form, you can check the response and create the user and, if needed, the group. Please use the `ibl_addgroup` or `ibl_adduser` command in the `ipa_functions.sh` script to create the group or user. You can also use [`ipa` commands](ipa_commands.md) directly, but the `ibl_` functions will do some extra checks for you.

```sh
source ipa_functions.sh
ibl_addgroup <GROUP-NAME> <DESCRIPTION>
ibl_adduser <USERNAME> <FIRST-NAME> <LAST-NAME> <PRIMARY-GROUP>

# Then on every server that enabled quotas, run:
# Increase the quota only when needed.
sudo xfs_quota -x -c 'limit bsoft=20g bhard=25g <USERNAME>' /home
```

## Want to create many users at once?

For courses or workshops, you might need to add users like `workshop` participants, you can use the following commands to add many users at once:

```sh
source ipa_functions.sh
ibl_addusers_with_defined_password <username_base> <first_name_base> <last_name_base> <groupname> <total_users> <common_password>

# Then on every server that enabled quotas, run:
source ipa_functions.sh
ibl_addusers_quota <username_base> <total_users>
```

Once done, send email to the user and their PI to inform them that the account is created, and provide them with instructions on how to access the servers. You can use [this template](https://github.com/IBL-bioinfo/admin_tools/blob/main/new_user-welcome_letter.md). Please remember to change the username and password in the template.