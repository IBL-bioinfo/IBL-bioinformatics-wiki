---
applyTo: docs/source/**/*.md,docs/source/*.md
---

For image style in `<span>` tag `<span><img alt="macos icon" src="../_static/images/nextcloud_icon_macos.jpg" width="24"></span>`, the complier does not respect `style="width: 1.5em;"`, unless you have other solution.

Tag `(select-virtual-files-version)=` placed inside the admonition is intentional, it will prevent the compiler adding admonition style to the popup text box.