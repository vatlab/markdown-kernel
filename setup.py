#!/usr/bin/env python
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

import os
from setuptools import find_packages, setup

# obtain version of markdown-kernel
with open('src/markdown_kernel/_version.py') as version:
    for line in version:
        if line.startswith('__version__'):
            __version__ = eval(line.split('=')[1])
            break

kernel_json = {
    "argv": [
        "python", "-m", "markdown_kernel.kernel", "-f", "{connection_file}"
    ],
    "display_name": "Markdown",
    "language": "markdown",
}

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_long_description():
    with open(os.path.join(CURRENT_DIR, "README.md"), "r") as ld_file:
        return ld_file.read()


setup(
    name="markdown-kernel",
    version=__version__,
    description='A markdown kernel for Jupyter',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author='Bo Peng',
    url='https://github.com/vatlab/markdown-kernel',
    author_email='bpeng@mdanderson.org',
    maintainer='Bo Peng',
    maintainer_email='bpeng@mdanderson.org',
    license='3-clause BSD',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'notebook',
        'markdown',
    ])
