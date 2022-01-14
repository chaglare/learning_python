#!/usr/bin/env python3
"""Install democc."""
from setuptools import find_packages, setup

with open('requirements.txt', 'rt') as reqs_file:
    reqs_list = reqs_file.readlines()

setup(
    name='cctest',
    description='DevInfra Artifactory CLI.',
    packages=find_packages(where='./'),
    package_dir={'': './'},
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=reqs_list
)
