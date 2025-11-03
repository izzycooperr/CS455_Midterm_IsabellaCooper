# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'Date Generator Design'
copyright = '2025, Isabella Cooper'
author = 'Isabella Cooper'
release = '0.1'

# -- Path setup --------------------------------------------------------------
import os
import sys

# Add the parent directory (where src/ is located) to sys.path
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',      # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',     # Support Google/Numpy-style docstrings
    'sphinx.ext.viewcode',     # Add links to highlighted source code
    # Optional: uncomment if you want Markdown docs (requires pip install myst-parser)
    # 'myst_parser',
]

# If using Markdown, recognize .md files as valid sources
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
# }

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# Title for the generated site
html_title = "Date Generator API (Design Stubs)"

# -- Autodoc settings --------------------------------------------------------

# Include both class docstrings and __init__ docstrings
autoclass_content = 'both'

# Order members by their appearance in the source
autodoc_member_order = 'bysource'

# Display type hints in function signatures
autodoc_typehints = 'description'

# Napoleon settings (for Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_special_with_doc = True
