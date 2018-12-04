#!/usr/bin/env python
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

import json
import os
import sys
import argparse
import shutil
import logging

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

kernel_json = {
    "argv":         [sys.executable, "-m", "markdown_kernel.kernel", "-f", "{connection_file}"],
    "display_name": "Markdown",
    "language":     "markdown",
}


def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False  # assume not an admin on non-Unix platforms


def install_markdown_kernel_spec(args):
    user = False
    prefix = None
    if args.sys_prefix:
        prefix = sys.prefix
    elif args.prefix:
        prefix = args.prefix
    elif args.user or not _is_root():
        user = True

    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        # Copy resources once they're specified
        shutil.copy(os.path.join(os.path.split(__file__)[
                    0], 'kernel.js'), os.path.join(td, 'kernel.js'))
        # Copy resources once they're specified
        shutil.copy(os.path.join(os.path.split(__file__)[
                    0], 'logo-64x64.png'), os.path.join(td, 'logo-64x64.png'))

        KS = KernelSpecManager()
        KS.log.setLevel(logging.ERROR)
        KS.install_kernel_spec(td, 'markdown', user=user,
                               replace=True, prefix=prefix)
        print('markdown jupyter kernel spec is installed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Install KernelSpec for markdown Kernel')
    prefix_locations = parser.add_mutually_exclusive_group()
    prefix_locations.add_argument('--user',
                                  help='Install KernelSpec in user homedirectory',
                                  action='store_true')
    prefix_locations.add_argument('--sys-prefix',
                                  help='Install KernelSpec in sys.prefix. Useful in conda / virtualenv',
                                  action='store_true',
                                  dest='sys_prefix')
    prefix_locations.add_argument('--prefix',
                                  help='Install KernelSpec in this prefix',
                                  default=None)
    args = parser.parse_args()
    install_markdown_kernel_spec(args)
