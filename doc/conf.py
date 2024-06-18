# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Use the installed Hawkmoth package for CI, testing, and Read the Docs, while
# allowing documentation build using Hawkmoth from the source tree.
if not tags.has('use-installed-hawkmoth') and 'READTHEDOCS' not in os.environ:
    sys.path.insert(0, os.path.abspath('../src'))



project = 'Example'
copyright = 'workshop participant'
author = 'workshop participant'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'hawkmoth',
    'hawkmoth.ext.javadoc',
    'hawkmoth.ext.napoleon',
    'sphinx.ext.intersphinx'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for Hawkmoth ----------------------------------------------------
# https://jnikula.github.io/hawkmoth/dev/extension.html#configuration

# Setup Clang on Read The Docs
if 'READTHEDOCS' in os.environ:
    from hawkmoth.util import readthedocs

    readthedocs.clang_setup()
hawkmoth_root = os.path.abspath('../src')

hawkmoth_clang = ['-I../src', '-DHAWKMOTH']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
