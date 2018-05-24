#!/usr/bin/env python3
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

from ipykernel.kernelbase import Kernel
from ._version import __version__


class markdown_kernel(Kernel):
    implementation = 'markdown'
    implementation_version = __version__
    banner = "markdown kernel"
    help_links = 'http://github.com/vatlab/markdown_kernel'
    language = 'markdown'
    language_info = {
        'mimetype': 'text/markdown',
        'name': 'Markdown',
        'file_extension': '.md',
        'pygments_lexer': 'markdown',
        'codemirror_mode': 'markdown',
    }

    def __init__(self, **kwargs):
        super(markdown_kernel, self).__init__(**kwargs)

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        self.send_response(
            self.iopub_socket,
            'display_data',
            {
                'source': 'markdown', 'metadata': {},
                'data': {'text/markdown': code}
            })
        return {'status': 'ok',
                'payload': [],
                'user_expressions': {}
                }


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=markdown_kernel)
