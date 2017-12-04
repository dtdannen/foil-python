# !/usr/bin/env python

from setuptools import setup

setup(name='foil-python',
      version='1.4',
      description='Python Implementation of FOIL by J. R. Quinlan',
      author='Dustin Dannenhauer (Original Author: John Trimble)',
      author_email='dustin.td@gmail.com',
      install_requires=[],
      packages=['src',
                'src.trimlogic',
                'src.trimlogic.test',])