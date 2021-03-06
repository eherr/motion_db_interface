#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = []
with open(path.join(here, "requirements.txt"), "r") as infile:
    requirements = [line for line in infile.read().split("\n") if line]

setup(
    name="motion_db_interface",
    version="0.1",
    description="Motion DB Interface.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eherr/motion_db_interface",
    author="DFKI GmbH",
    license='MIT',
    keywords="REST Interface",
    packages=find_packages(exclude=("examples",)),
    python_requires=">=3.5.*, <4",
    install_requires=requirements,
)
