# coding: utf-8
import os
from setuptools import setup, find_packages

# Directory containing this file
CONTAINING_DIR = os.path.abspath(os.path.dirname(__file__))

with open("README.md") as f:
    README_MD = f.read()

setup(
    name="tiledb-cloud-pythondb",
    version='0.0.1',
    long_description=README_MD,
    packages=find_packages(),
    long_description_content_type="text/markdown",
    author="TileDB, Inc.",
    author_email="help@tiledb.io",
    maintainer="TileDB, Inc.",
    maintainer_email="help@tiledb.io",
    description="TileDB Connector for Python DB API 2.0",
    url="https://tiledb.io",
    keywords=["TileDB", "cloud", "python"],
    install_requires=[
        "pandas",
        "tiledb-cloud",
        "pyarrow>=7.0.0"
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
