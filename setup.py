# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zmsai",
    version="0.1.5",
    author="evi1haxor",
    author_email="architdwivedi.off@gmail.com",
    description="Ai solution for Luhmann's Zettelkasten",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evi1haxor/zettelkasten-ai/",
    packages=["zmsai"],
    # packages=setuptools.find_packages(),
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["scikit-learn"],
    entry_points={"console_scripts": ["zmsai=zmsai.__main__:main",]},
)
