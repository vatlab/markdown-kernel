#!/usr/bin/env python
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

import sys, os
import shutil
from setuptools import find_packages, setup
from distutils import log

# obtain version of markdown-kernel
with open('src/markdown_kernel/_version.py') as version:
    for line in version:
        if line.startswith('__version__'):
            __version__ = eval(line.split('=')[1])
            break

kernel_json = {
    "argv":         ["python", "-m", "markdown_kernel.kernel", "-f", "{connection_file}"],
    "display_name": "Markdown",
    "language":     "markdown",
}


dest = '''\
A simple markdown kernel that render its input in markdown, pretty useless by itself
but can be very useful with SoS (https://vatlab.github.io/SoS).
'''

setup(name = "markdown-kernel",
    version = __version__,
    description = 'A markdown kernel for Jupyter',
    long_description=dest,
    author = 'Bo Peng',
    url = 'https://github.com/vatlab/markdown-kernel',
    author_email = 'bpeng@mdanderson.org',
    maintainer = 'Bo Peng',
    maintainer_email = 'bpeng@mdanderson.org',
    license = '3-clause BSD',
    include_package_data = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        ],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires=[
          'notebook',
          'markdown',
      ]
)
