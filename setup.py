#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports #
from setuptools import setup, find_namespace_packages
from os import path

# Load the contents of the README.md file #
this_dir = path.abspath(path.dirname(__file__))
readme_path = path.join(this_dir, 'README.md')
with open(readme_path, encoding='utf-8') as handle: readme = handle.read()

# Call setup #
setup(
    name             = 'waste_flow',
    version          = '1.3.1',
    description      = 'A package for retrieving data concerning waste '
                       'management on the European continent.',
    license          = 'MIT',
    url              = 'http://github.com/xapple/waste_flow/',
    author           = 'Lucas Sinclair',
    author_email     = 'lucas.sinclair@me.com',
    packages         = find_namespace_packages(),
        install_requires = ['autopaths>=1.5.9', 'plumbing>=2.11.1',
                            'pymarktex>=1.5.7' 'pandas', 'numpy',
                            'pytest', 'requests', 'matplotlib'],
    python_requires  = ">=3.6",
    long_description = readme,
    long_description_content_type = 'text/markdown',
    include_package_data = True,
)