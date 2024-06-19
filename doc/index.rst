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

.. autosummary:: ArduinoDocs
   :toctree: ArduinoDocs
   :cpp:ArduinoDocs:
.. _ESP32 Project C API:

ESP32 Project C API Reference
===============================

This section documents the C API functions available in the project.

.. doxygen:: documentation-example  # Replace with your project name
   :project: documentation-example

**Functions:**

* :cpp:func:`setup`
* :cpp:func:`loop`
* ... (other documented functions from your Arduino code)

