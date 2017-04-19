# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kpi',
    version='0.1.0',
    description='Webscraping application',
    long_description=readme,
    author='Mattias Gonday',
    author_email='mattias.gonday@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

