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


.. _ESP32 Project C API:

API Reference
==============

**Documented Functions:**
:cpp:func:`setup`
    Sets up the initial configuration for the Arduino board.
:cpp:func:`loop`
    The main loop of the program, continuously executed.
:cpp:func:`batteryRead`
    Reads the battery voltage and returns the value.

**Additional Documentation (Optional):**

(In this section, you can add further explanations and details for the documented functions beyond what Breathe extracts from code comments.)

* **setup Function:**
   - Describe the initialization steps performed by `setup()`. Consider mentioning specific actions like setting up serial communication or initializing pins.
* **loop Function:**
   - Explain the repetitive actions or processes handled by `loop()`. Describe how it might read sensor data, control actuators, or communicate with other devices.
* **batteryRead Function:**
   - Explain the purpose of this function in more detail.
   - Describe the parameters it takes (e.g., the pin number for reading battery voltage).
   - Specify the return type (e.g., voltage value, error code).
   - Provide code examples demonstrating how to use the function in your Arduino code.

.. include:: links.rst  # Optional file for external links

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

