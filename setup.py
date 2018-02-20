# coding: utf-8

import os
import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name='sample_stream',
    version='0.0.1',
    url='https://github.com/pistatium/sample_stream',
    author='pistatium',
    description='Sample server of http streaming',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
    ],
    extras_require={
        'test': [
            'pytest',
        ]
    },
)
