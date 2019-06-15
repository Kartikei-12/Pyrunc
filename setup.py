"""setup.py file for package Pyrunc"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pyrunc",
    version="0.1d",
    author="Kartikei Mittal",
    author_email="kartikeimittal@gmail.com",
    description="Simple python package to write C code directly in python script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kartikei-12/Pyrunc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License Version 2",
        "Operating System :: OS Independent",
    ],
)
