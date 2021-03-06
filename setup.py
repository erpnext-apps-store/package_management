# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in package_management/__init__.py
from package_management import __version__ as version

setup(
	name='package_management',
	version=version,
	description='Managing Packages',
	author='Lintec Tecnología',
	author_email='contact@lintec.xyz',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
