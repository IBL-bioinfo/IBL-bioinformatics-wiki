# Set up and run a project folder

*By C.Du [@snail123815](https://github.com/snail123815) & Joost Willemse [@Karivtan](https://github.com/Karivtan)*

This page covers **owning** a Research Drive project folder: preparing for it, requesting it from
ISSC, inviting your people, organising the folder structure, and asking for more space. Sharing the
folders you create is the last step — see [Share folders with others](./ResearchDrive_sharing.md).

You need this page if you are a PI or a lab manager setting up storage for a project. If you are
instead trying to get *your own* data in and out of a folder that has already been shared with
you, start at [Research Drive](./ResearchDrive.md) — most people need both pages at different
times.

```{contents}
---
depth: 3
---
```

## Preparation

For all your current projects, check the DMP and update the corresponding part to fit the new
situation. Make sure the costs are covered by the project. For each project folder that you need,
please assign a cost centre. ISSC is **not** centrally funding the first TB with a valid DMP, so
there is no need to attach that; just mention the cost centre when filling in the form from the
ISSC helpdesk. IBL will fund the first 0.5 TB of the PI umbrella project folder.

Optionally, fill out a DMP:

1. All projects that generate research data
2. Collaborative projects (you can use a collective DMP)
3. An umbrella DMP for your group (covering smaller topics that may not fit any project yet)

After drafting your DMP(s), contact <ibl.rdm@biology.leidenuniv.nl> to have them approved.

## Apply for a project folder

Access to Research Drive is **always by invitation**. ISSC creates project folders on request from
PIs or lab managers; the PI or lab manager then invites the rest of the staff and students.

- Research Drive is a paid service. Please consult the IBL RDM team for cost and funding details.
- Request Research Drive per project/DMP/contract:
  - [ISSC helpdesk](https://helpdesk.universiteitleiden.nl/)
  - Go to "Research support" → "Research Drive" → "Request Research Drive"
  - Choose **"No"** for DMP, and **always use a cost centre** number in the "SAP number:" field —
    ISSC has stopped DMP-based funding.
  - Mention the project folder name you want to create in the "Comment:" field
- Invite your lab manager if you do not want to manage the Research Drive yourself. Give your lab
  manager full access to all your project folders; the lab manager can then invite the rest of the
  staff and students and manage the major folder shares.

For **PhD/PostDoc/Researcher (staff)/student**: once you receive the invitation, follow the link
and confirm you can log in. Only after that can your PI or lab manager give you access to your
folder.

::: {admonition} Project folder name may not be consistent
Example:

![Example of project folder name](../_static/images/nextcloud_different_name_example.png)

Note in this example, `NIOO_4` is actually showing information for `IBL_G_Van_Wezel` folder.

You can rename a project folder in the **Files** tab, but the Dashboard name will not change (it
reflects the owner's original name). If renaming is necessary, include an abbreviation of the
original name, e.g. "New_name_0cnf_opn" (for "changed name from old project name"), so it remains
identifiable. Also avoid [lengthy path problems](./ResearchDrive_troubleshooting.md#windows-long-path-compatibility-issue).
:::

## Invite users and set up the folder structure

After Research Drive has been activated, follow these steps to set up your project folder and
invite users. This assumes you already have a project folder (if you are a PI) or have been
invited to access at least one folder (if you are staff or student). If you do not have access to
any project folder, please contact your PI or lab manager.

PI or authorized lab manager have full control over the project folder: you decide how to organise
the folder structure and who can access which folders. We recommend the
[intended folder structure](./ResearchDrive.md#intended-structure), but you can adjust it
according to your needs.

**Anyone** with a Research Drive account can invite other users, including:

- **Staff**: PhD students, PostDocs, Researcher (staff), Lab managers
- **Students**: Master students, Bachelor students, Interns
- **External collaborators**: collaborators from other institutions. They can be invited using
  their external email address, but will be prompted to create their own
  [eduID](https://eduid.nl/home) account, or use the account from their institute (if present in
  the system), before they can log in. If you share with "Allow download and sync" enabled (which
  is *not* the same as allowing "Edit"), they can access the files just like internal users,
  including via [command line `rclone`](./ResearchDrive_commandLine.md) and the
  [Nextcloud desktop client](./ResearchDrive_setup.md).

Steps:

- Log in to [Research Drive](https://universiteitleiden.data.surf.nl)
- Go to the dashboard (top-left icon row, second icon from right)

::: {admonition} First-time login
The first time you log in, you may be asked to log in more than once, and your project folder may
not be there yet. This is normal. Wait a few minutes and reload the page — your account is still
being set up.
:::

- Go to "Dashboard" → "User accounts" and invite all users, both staff and students, using their
  university email address (for example the @biology mail for employees).
  - For students without a university email address, you can use their personal email address, but
    make sure to inform them to check their inbox and confirm the invitation.
  - For external collaborators, invite them using their external email address. They must first
    create their own [eduID](https://eduid.nl/home) account, or use the account from their
    institute (if present in the system), before they can log in.
  - Once the first several staff finish setting up, they can invite the rest of the staff and
    students.
- Go to the **Files** tab (top left), and go into your **project folder**
- Create a folder for everyone in this project
- Tell your users to install the Nextcloud desktop client from the Company Portal (Windows 11) or
  Managed Software Centre (macOS) and log in with their ULCN account — see
  [Install Nextcloud desktop client](./ResearchDrive_setup.md#install-nextcloud-desktop-client)

```{tip}
Users will see "0B of 0B used" and may report it as a problem. That is expected — see
{ref}`It is normal to have zero space <you-do-not-own-space>`.
```

## Share folders with others

The last step in setting up a project folder is sharing specific folders with the people who need
them. That has its own page — see [Share folders with others](./ResearchDrive_sharing.md) for
sharing with individual users, sharing with a team, and how to name shared folders so recipients
understand what they are looking at.

## Expand storage space

By default, each application creates a project folder with 0.5 TB of storage space. If you need
more space, please specify the required storage size and the reason in the "Comment:" field when
applying for Research Drive.

To expand an existing project folder:

- [ISSC helpdesk](https://helpdesk.universiteitleiden.nl/)
- Go to "Research support" → "Research Drive" → "Ask a question"
- Fill in the desired space you want to expand to
- Explain how you would like to pay for the extra space, for example by mentioning the cost centre
  of the project that will cover the cost.

::: {admonition} Do not blindly expand storage of one project folder
Before requesting more space, consider whether the additional storage will actually be used in line
with your project's Data Management Plan (DMP). Raw data that can be regenerated, large
intermediate files, or software environments generally should not be kept in Research Drive
long-term. If you find your storage is filling up quickly, it may be a sign to review your data
retention strategy: archive or delete files that are no longer needed, avoid storing intermediate,
regeneratable data, and check whether files from completed projects can be moved to long-term
archival storage (tape) instead.

In particular, [do not store dependency folders or software environments in Research
Drive](./ResearchDrive_troubleshooting.md#windows-long-path-compatibility-issue).
:::

Note that the numbers you see are not always in the units you expect — see
[Storage space and quota](./ResearchDrive.md#storage-space-and-quota) before concluding that you
are out of space.
