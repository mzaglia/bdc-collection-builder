#
# This file is part of BDC Collection Builder.
# Copyright (C) 2019-2020 INPE.
#
# BDC Collection Builder is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)


g = dict()
with open(os.path.join('..', '..', 'bdc_collection_builder', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

# -- Project information -----------------------------------------------------

project = 'bdc-collection-builder'
copyright = '2019-2020, National Institute for Space Research'
author = 'BDC - INPE'

# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

#
# BDC theme configuration
#

import bdc_readthedocs_theme

html_theme_path = bdc_readthedocs_theme.html_theme_path()
html_theme = 'bdc_theme'

extensions.append("bdc_readthedocs_theme")

html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": project,
    "github_project": "brazil-data-cube/bdc-collection-builder"
}

def setup(app):
    app.add_stylesheet('bdc_collection_builder.min.css')
