#!/usr/bin/env python
#
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""AlphaGriffin setuptools build script.

@author lannocc

@see    https://packaging.python.org/en/latest/distributing.html
@see    https://github.com/pypa/sampleproject

Some of this script logic also taken from:
        https://github.com/google/protobuf
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

if __name__ == '__main__':

    setup(

        name='pyproject',
        version='0.0.1',
        license='AG', # FIXME

        namespace_packages=['ag'], # home for Alpha Griffin libraries
        packages=find_packages(exclude=['tests']),

        author='Lannocc @ Alpha Griffin',
        author_email='lannocc@alphagriffin.com',

        description='Alpha Griffin Starter Python Project',
        long_description=open('README.rst').read(),
        url='http://alphagriffin.com',

        # @see https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Programming Language :: Python',
            'Topic :: System :: Installation/Setup',
            'Topic :: Utilities'
        ],

        # space-separated list of keywords
        keywords='alphagriffin example utilities',

        # run-time dependencies
        install_requires=['setuptools'], # setuptools here for example only (it's implied)

        extras_require={
        },

        package_data={
        },

        data_files=[],

        entry_points={
        },
    )

