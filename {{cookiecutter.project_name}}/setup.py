# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

REQUIRED = []


HERE = os.path.abspath(os.path.dirname(__file__))
VERSION_FILE = os.path.join(HERE, "{{cookiecutter.project_slug}}", "__version__.py")
ABOUT = {}
with open(VERSION_FILE, "r", encoding="utf-8") as f:
    exec(f.read(), ABOUT)  # pylint: disable=exec-used

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=ABOUT["__project_name__"],
    version=ABOUT["__version__"],
    description=ABOUT["__description__"],
    author=ABOUT["__author__"],
    author_email=ABOUT["__author_email__"],
    install_requires=REQUIRED,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
