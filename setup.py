#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='AIHAO',
    version='1.0.0',
    packages=find_packages(include=['aihao', 'aihao.*'], exclude=['config', 'notebooks']),

)
