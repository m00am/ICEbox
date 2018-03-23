# -*- coding: utf-8 -*-
from setuptools import setup#, find_packages

setup(
    name="ICEbox",
    description="Script to automatically generate hosts, ICE, and matrix topologies for Shadowrun 4.",
    long_description=open("README.md").read(),
    version="0.1.0",
    author="m00am",
    author_email="contact.m00am@gmail.com",
    license="MIT",
    url="",
    # install_requires = [],
    # packages = find_packages(),
    entry_points={
        "console_scripts": [
            "ICEbox_ICE = ICEbox.__main__:main",
            "ICEbox_host = ICEbox.__main__:main",
        ]
    },
)
