#!/usr/bin/env python

from setuptools import setup

setup(name='target-json',
      version='0.0.1',
      description='Singer.io target for writing JSON files',
      author='dvelardez',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_json'],
      install_requires=[
          'jsonschema==2.6.0',
          'singer-python==2.1.4',
      ],
      entry_points='''
          [console_scripts]
          target-json=target_json:main
      ''',
)
