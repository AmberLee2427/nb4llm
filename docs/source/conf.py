# Configuration file for the Sphinx documentation builder.

project = "nb4llm"
copyright = "2025, Amber Malpas (AmberLee2427)"
author = "Amber Malpas (AmberLee2427)"
release = "v0.1.3"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and directories
# to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = "alabaster"
html_static_path = ["_static"]

# Napoleon settings for numpydoc
napoleon_google_docstring = False
napoleon_numpy_docstring = True
