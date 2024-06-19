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
sys.path.insert(0, os.path.abspath('..'))  # Add parent directory to path

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:
    subprocess.call('doxygen', shell=True)


source_suffix = '.rst'
master_doc = 'index'

project = u'documentation-example'
copyright = 'workshop participant'
author = 'workshop participant'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'breathe',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
]

# Breathe configuration (adjust paths as needed)
breathe_projects = {
    'documentation-example': ('../src', '.')  # Replace with your project name and source/header paths
}
breathe_default_group = 'documentation-example'  # Replace with your project name


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for Hawkmoth ----------------------------------------------------
# https://jnikula.github.io/hawkmoth/dev/extension.html#configuration



# -- Breathe configuration -------------------------------------------------

breathe_projects = {
	"C++ Sphinx Doxygen Breathe": "_build/src/"
}
breathe_default_project = "C++ Sphinx Doxygen Breathe"
breathe_default_members = ('members', 'undoc-members')

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
