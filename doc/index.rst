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
   api.md

.. _ESP32 Project C API:

API Reference
==============

usage
api

:func:`initialise_logger()`
:cpp:func:`batteryRead()`
:cpp:func:`setup()`
:cpp:func:`loop()`
:c:func:`batteryRead()`

```{literalinclude} example.py
:language: python
:emphasize-lines: 2-3
```
.. autosummary::
   :toctree: _autosummary

   project.module1
   project.module2
