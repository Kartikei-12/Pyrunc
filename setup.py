"""setup.py file for package Pyrunc"""

import setuptools

from utility import get_and_update_version

_version = get_and_update_version()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pyrunc",
    version="0.0." + _version,
    author="Kartikei Mittal",
    author_email="kartikeimittal@gmail.com",
    description="Simple python package to write C code directly in python script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kartikei-12/Pyrunc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
)
