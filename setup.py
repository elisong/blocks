#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import listdir
from setuptools import setup

scripts = ['bin/' + f for f in listdir('bin')]

setup(name='cmdkit',
      version='1.0',
      description='CmdKit - terminal command collections',
      author='elisong',
      author_email='elisong.ah@gmail.com',
      url="https://github.com/elisong/cmdkit",
      scripts=scripts,
      install_requires=[
          'lxml',
          'google',
          'mdutils',
          'simple_term_menu'
      ]
      )
