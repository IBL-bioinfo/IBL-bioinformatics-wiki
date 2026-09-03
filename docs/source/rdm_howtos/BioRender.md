# BioRender

*By C.Du [@snail123815](https://github.com/snail123815)*

This page covers the IBL BioRender account and the policy on BioRender's built-in "Graphing" feature.

```{contents}
---
depth: 3
---
```

## IBL BioRender account

IBL has a BioRender account that you can join only if you register with an `@biology.leidenuniv.nl` email address. The policy has been shared with PIs and will be included in the introduction material. The correct institute account (organisation) name is [**Leiden University - Institute of Biology**](https://app.biorender.com/portal/leiden-university-institute-biology).

Please fill in [this form](https://forms.cloud.microsoft/e/3wJqS3TBdi) (login required) when you join the IBL BioRender institute account. QR code to the form:

![QRCode IBL BioRender registration](../_static/images/QRCode_IBL_BioRender_registration.resize.png)

New accounts that cannot be found in this form will be removed.

## BioRender Graphing is not recommended for statistics

BioRender's built-in **Graphing** feature imports a dataset and runs guided statistical analysis (t-tests, ANOVA, dose-response, Kaplan-Meier, etc.) to produce a chart inside your BioRender project, and is marketed by BioRender as an alternative to GraphPad Prism.

:::{admonition} Policy: use Prism for statistics and graphing, not BioRender Graphing
:class: important
Do **not** use BioRender's **Graphing** feature to run statistical tests or produce your data graphs. Do the analysis and build the graph in **GraphPad Prism**, then bring only the finished graph into BioRender to assemble and annotate the final figure. See [why](#why-prism-instead-of-biorender-graphing) and [how to request Prism](#requesting-prism-through-issc).
:::

### Why Prism instead of BioRender Graphing

Prism is the long-established statistics and graphing tool used across biology and biomedical research. Colleagues, collaborators, and reviewers are already familiar with it, and an analysis done in Prism can be checked and reproduced using skills and habits already established in the group. BioRender's Graphing feature, by contrast, is new and does not yet have a track record of use within IBL.

Keeping the statistical analysis in a `.prism` file also keeps it separate from the illustrative figure: the `.prism` file remains your durable, re-checkable analysis record, and BioRender is used for figure assembly.

### Requesting Prism through ISSC

Request Prism through the [ISSC helpdesk](https://helpdesk.universiteitleiden.nl/): **Software & licenses** → **Install or request software**. Once the request has been processed, install Prism from **Company Portal** (Windows) or **Managed Software Center** (macOS).

### Moving your Prism graph into BioRender

Export the finished graph from Prism as an **SVG** — the vector format both Prism can export and BioRender can import as an image. Upload that SVG into your BioRender project and place it on the canvas alongside the rest of your figure, the same way you would add any other image.

(**Disclaimer**: the above is based on the current state of BioRender and GraphPad Prism as of September 2026, and may change in the future.)
