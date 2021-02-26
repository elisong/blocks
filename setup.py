#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import listdir
from setuptools import setup

scripts = ['bin/' + f for f in listdir('bin')]

setup(name='cmdkits',
      version='1.0',
      description='CmdKits - terminal command collections',
      author='elisong',
      author_email='elisong.ah@gmail.com',
      url="https://github.com/elisong/cmdkits",
      scripts=scripts,
      install_requires=[
          'lxml',
          'google',
          'mdutils',
          'simple_term_menu',
          'beautifulsoup4'
      ]
      )
