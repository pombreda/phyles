#!/usr/bin/env python

import os

from setuptools import setup, find_packages

import configobj

info = configobj.ConfigObj('PackageInfo.cfg')

setup(name = info['PACKAGE'],
      version = "%(MAJOR)s.%(MINOR)s.%(MICRO)s%(TAG)s" % info,
      author = info['AUTHOR'],
      author_email = info['EMAIL'],
      url = info['URL'],
      description = info['DESCRIPTION'],
      license = info['LICENSE'],
      long_description = open('README.rst').read(),
      packages = [info['PACKAGE']], # or find_packages()
      package_data = {'':['*/*.*']},
      include_package_data = True,
      requires = ['phyles'],
      # test_suite = info['PACKAGE'] + '.tests.test_suite',
      classifiers = [
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7', ],
      )
