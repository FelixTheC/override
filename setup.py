#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 30.04.20
@author: felix
"""
import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

packages = find_packages(exclude=["test_*", "*.tests"])

setup(
    name="pyoverload",
    version="0.1.0",
    description="A Runtime method overload decorator.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/FelixTheC/override.git",
    author="FelixTheC",
    author_email="fberndt87@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=["strongtyping"],
    dependencies="",
    packages=packages,
    python_requires=">=3.9",
    include_package_data=True,
)
