#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup, find_packages

# build command
setup(
    name="phydiv",
    version="0.0.1",
    author="Emily Leggat",
    author_email="el3258@columbia.edu",
    license="GPLv3",
    description="A package to simulate site by species matrices under different pylogenetic diversity assumptions",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["simpd = phydiv.src.simpd.__main__:main"]
    },
    packages = find_packages()
)