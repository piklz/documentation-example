# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import shlex
import subprocess
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath('.')), "src"))# Add parent directory to path

# Use the installed Hawkmoth package for CI, testing, and Read the Docs, while
# allowing documentation build using Hawkmoth from the source tree.
if not tags.has('use-installed-hawkmoth') and 'READTHEDOCS' not in os.environ:
    sys.path.insert(0, os.path.abspath('../src'))




project = u'ArduinoDocs'
copyright = 'workshop participant'
author = 'workshop participant'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx_rtd_dark_mode',
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'clang',
    'hawkmoth',
    'hawkmoth.ext.javadoc',
    'hawkmoth.ext.napoleon',
]

try:
    # Add Copy button to code cells, if extension is available
    import sphinx_copybutton
    extensions.append('sphinx_copybutton')
except ImportError:
    pass


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}






# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'
master_doc = 'index'


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for Hawkmoth ----------------------------------------------------
# https://jnikula.github.io/hawkmoth/dev/extension.html#configuration


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'default_dark_mode': True,  # Set to True for dark mode by default
    # Other theme options (refer to sphinx_rtd_theme documentation)
    'description': 'Sphinx Autodoc for C',
    'extra_nav_links': {
        'GitHub': 'https://github.com/jnikula/hawkmoth',
        'PyPI': 'https://pypi.org/project/hawkmoth',
    }
}
html_static_path = ['_static']
