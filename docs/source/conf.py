# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "IBL-Bioinformatics wiki"
copyright = "2026, IBL"
author = "IBL-Bioinformatics atelier"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinx_tippy",
]
templates_path = ["_templates"]
exclude_patterns = ["_excluded"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# Theme alabaster
# https://alabaster.readthedocs.io/en/latest/customization.html
# Side bar
# https://www.sphinx-doc.org/en/master/#confval-html_sidebars
html_theme = "alabaster"
html_static_path = ["_static"]
html_css_files = ["custom.css", "sidebar.css", "tocbackref.css"]
html_js_files = ["external_links.js", "anchor_scroll.js", "sidebar_scroll.js"]
html_scaled_image_link = False
html_sidebars = {
    "**": [
        "about.html",
        # 'globaltoc.html',
        "searchbox.html",
        "navigation.html",
        "relations.html",
        # "sourcelink.html",
    ]
}
html_theme_options = {
    "description": "IBL Bioinformatics atelier",
    "github_user": "snail123815",
    "github_repo": "IBL-bioinformatics-wiki",
    "github_count": False,
    "fixed_sidebar": True,
    "sidebar_collapse": True,
    "sidebar_width": "18rem",  # has to be fixed
    "page_width": "48rem",  # controls mobile breakpoint; actual max-width is overridden to min(70rem,95%) in custom.css
    # System sans-serif stack instead of Alabaster's serif default (Georgia), which
    # renders muddy on non-retina 1080p screens. 'Segoe UI Variable Text' is
    # Windows 11's Fluent-era refinement of Segoe UI; it degrades gracefully to
    # classic 'Segoe UI' on Windows 10 and other platforms.
    "font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI Variable Text', "
    "'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif",
    "head_font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI Variable Text', "
    "'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif",
    "code_font_family": "'Cascadia Code', 'JetBrains Mono', Consolas, Menlo, "
    "'DejaVu Sans Mono', monospace",
    # Alabaster's default body_text (#3E4349) is a light grey that reads thin at
    # regular weight on non-retina Windows screens; headings inherit this color
    # too since they have no color rule of their own, so darkening it here fixes
    # both. Using GitHub's docs body text color rather than an arbitrary pick.
    "body_text": "#1F2328",
    # Slightly off-white page background (Bootstrap/GitHub's "light" token)
    # instead of pure #fff, to soften the glare of near-black text on a fully
    # white page. Kept clearly lighter than admonitions' #EEE (gray_2) fill so
    # callout boxes stay visually distinct. body_bg inherits this
    # automatically (Alabaster falls back to base_bg when body_bg is unset).
    "base_bg": "#F8F9FA",
    # Mobile/narrow sidebar: light blue tint matching the desktop caption accent
    # instead of Alabaster's default flat dark grey (#333), so the nav panel stays
    # visually consistent with the rest of the site. See sidebar.css for the
    # separator that keeps this panel distinguishable from the body text below it.
    # Darkened from the original #f0f7fb: that value was tuned against a pure
    # white page background, and reads as barely-there now that base_bg is
    # #F8F9FA (the accent's gap versus the page bg shrank to ~32% of its
    # original size). #E6F0F7 restores roughly the original visual weight.
    "narrow_sidebar_bg": "#E6F0F7",
    "narrow_sidebar_fg": "#3E4349",
    "narrow_sidebar_link": "#004B6B",
}
# https://alabaster.readthedocs.io/en/latest/customization.html
html_favicon = "_static/images/ibl.png"

# -- MyST settings -----------------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
myst_heading_anchors = 4
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_block",
    "attrs_inline",
]
