.. nb4llm documentation master file, created by
   sphinx-quickstart on Tue Jul 22 23:30:04 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

nb4llm: Notebook ↔ LLM Text Converter
=======================================

Welcome to **nb4llm**'s documentation!

nb4llm is a Python tool and library for converting Jupyter notebooks to and from a readable, LLM-friendly text format. It is designed for scientists, data scientists, and anyone who wants to make notebooks more accessible to large language models or other text-based tools.

Features
--------
- Convert `.ipynb` to readable `.txt` (and back!)
- Preserves code cell language (Python, R, Julia, ...)
- Handles nested code fences and markdown
- CLI and Python API
- Numpydoc-style docstrings for easy API browsing

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   cli_tutorial.md
   api

Quick Start
-----------

.. code-block:: bash

   # Convert a notebook to text
   nb4llm my_notebook.ipynb

   # Convert text back to a notebook
   nb4llm --reverse my_notebook.txt

See the :doc:source:`cli_tutorial` for more details and examples.

API Reference
-------------

See :doc:source:`api` for the Python API documentation.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`