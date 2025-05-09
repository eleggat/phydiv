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
    description="A package to calculate phylogenetic diversity metrics from community data.",
    classifiers=["Programming Language :: Python :: 3"],
    dependencies = [
        "itertools",
        "os",
        "numpy",
        "pandas",
        "toytree",
        "toyplot"],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        "console_scripts": [
            "phydiv = src.__main__:main"
            ]

    }
    
)