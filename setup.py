#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    'Programming Language :: Python',
    "Programming Language :: Python :: 2.7",
    "Operating System :: OS Independent",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    'Topic :: Software Development :: Libraries :: Python Modules']

long_description = open('README.md').read()

setup(name='oml',
      version="0.1",
      description="Open Mining Language",
      long_description=long_description,
      classifiers=classifiers,
      keywords='langague dml oml openmining mining',
      author="Avelino",
      author_email="thiago@avelino.xxx",
      url='http://openmining.io',
      download_url="https://github.com/mining/oml/tarball/master",
      license="MIT",
      package_dir={'oml': 'oml'},
      install_requires=REQUIREMENTS,
      include_package_data=True,
      zip_safe=False)
