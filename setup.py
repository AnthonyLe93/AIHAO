#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='AIHAO',
    version='0.0.1',
    packages=find_packages(exclude=['config', 'notebooks']),  # Add 'aihao' as the parameter
    package_dir={'aihao': 'aihao'},  # specify the 'aihao' directory as the root package directory

)
