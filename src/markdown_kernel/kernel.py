#!/usr/bin/env python3
#
# This file is part of Script of Scripts (markdown), a workflow system
# for the execution of commands and scripts in different languages.
# Please visit https://github.com/vatlab/SOS for more information.
#
# Copyright (C) 2016 Bo Peng (bpeng@mdanderson.org)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#


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
