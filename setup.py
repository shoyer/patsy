#!/usr/bin/env python

import sys
from setuptools import setup

DESC = """A Python library for describing statistical models and for
building model matrices."""

# Compatibility code for handling both setuptools and distribute on Python 3,
# as suggested here: http://packages.python.org/distribute/python3.html
extra = {}
if sys.version_info >= (3,):
    extra["use_2to3"] = True

setup(
    name="patsy",
    version="0.1.0",
    description=DESC,
    author="Nathaniel J. Smith",
    author_email="njs@pobox.com",
    license="2-clause BSD",
    packages=["patsy"],
    url="https://github.com/patsy/patsy",
    install_requires=["numpy"],
    **extra)
