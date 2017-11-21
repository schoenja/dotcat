# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
        name='dotcat',
        version='0.0.1',
        description='A mildly complex dotfile manager for linux',
        long_description=readme,
        author='schoenja',
        url='https://github.com/schoenja/dotcat',
        license=license,
        packages=find_packages(exclude=('tests', 'docs'))
)
