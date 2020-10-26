#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

test_requirements = [
    # TODO: put package test requirements here
]


setup(
    name='DL-OPT',
    version='1.0',
    description="A Python implementation of Data Lake Optimization algorithm.",
    long_description=readme + '\n\n' + history,
    author="Marziye Derakhshannia and Dickson Owuor",
    author_email='dm.derakhshannia@gmail.com',
    url='https://github.com/owuordickson/dl_opt',
    packages=find_packages(),
    #package_dir={'dlopt':'dlopt'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='data lake',
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Massachusetts Institute of Technology (MIT) License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
