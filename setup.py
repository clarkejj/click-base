# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup

description = '''
An example CLI project for PyYYC
'''

setup(
    name='yycli',
    version='0.0.0',
    description=description,
    long_description=open('README.md', 'r').read(),
    keywords=['python', 'cli', 'Click'],
    install_requires=[
        "click",
        "pytest",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    author='PyYYC',
    author_email='organizers@pyyyc.org',
    url='https://github.com/py-yyc/click-base',
    license='Public Domain',
    packages=[
        "test",
        "yycli",
    ],
    entry_points={
        'console_scripts': [
            'yycli = yycli._cli:cli'
        ]
    },
)
