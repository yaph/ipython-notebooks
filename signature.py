# -*- coding: utf-8 -*-
from datetime import datetime
from IPython.core import display
from IPython.core.magic import Magics, magics_class, line_magic


__version__ = '0.1.0'


@magics_class
class Signature(Magics):

    @line_magic
    def signature(self, line):
        sig = '''Author: <a href="http://ramiro.org/">Ramiro Gómez</a>
            • Last edited: {}'''.format(datetime.now().strftime('%B %d, %Y'))
        return display.HTML(sig)


def load_ipython_extension(ipython):
    ipython.register_magics(Signature)
