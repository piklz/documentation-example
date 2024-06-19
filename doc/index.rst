.. Example documentation master file, created by
   sphinx-quickstart on Sat Sep 23 20:35:12 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Example's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   helloworld.md
   some-feature.md
   another-feature.md

.. doxygenclass:: documentation-example
   :project: documentation-example
   :members:

.. autosummary::
   :toctree: .

   sphinx.environment.BuildEnvironment
   sphinx.util.relative_uri
