#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "travistimeout",
    version = "1.0.1",
    packages = find_packages('src'),
    package_dir = { '': 'src'},
    author = "Alexander Swensen",
    author_email = "contact@alexswensen.io",
    url = "https://github.com/AlexSwensen/travis-timeout",
    install_requires = [
        'setuptools'
    ],
    dependency_links = [],
    entry_points = {
        'console_scripts': [
            'travis-timeout = travistimeout:main'
        ]
    }
)
