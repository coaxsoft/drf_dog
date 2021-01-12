# drf_dog

|build-status-image| |pypi-version|

## Overview


Copy-paste utilities for Django REST Framework

## Requirements

-  Python 3.6+
-  Django 3.0+
-  Django REST Framework 3.10+

## Installation

Install using ``pip``\ …

.. code:: bash

    $ pip install drf_dog

## Example

TODO: Write example.

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
    $ ./runtests.py
```

You can also use the excellent `tox`_ testing tool to run the tests
against all supported versions of Python and Django. Install tox
globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you’ll need to install ``mkdocs``.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```

.. _tox: http://tox.readthedocs.org/en/latest/

.. |build-status-image| image:: https://secure.travis-ci.org/mikhailkravets/drf_dog.svg?branch=master
   :target: http://travis-ci.org/mikhailkravets/drf_dog?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/drf_dog.svg
   :target: https://pypi.python.org/pypi/drf_dog
