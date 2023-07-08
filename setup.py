#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    author="Andrew Moss",
    author_email="andrew@m0ss.dev",
    python_requires=">=3.7",
    name="bookit",
    version="0.0.2",
    description="Doc site generator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    license="MIT license",
    packages=find_packages(include=["bookit", "bookit.*"]),
    url="https://github.com/agmoss/bookit",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["click", "pathspec", "Pygments"],
    tests_require=["pytest"],
)
