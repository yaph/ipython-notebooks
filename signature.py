# -*- coding: utf-8 -*-
import IPython
import platform
import matplotlib
import numpy
import pandas

from datetime import datetime
from IPython.core import display
from IPython.core.magic import Magics, magics_class, line_magic


__version__ = '0.1.1'


@magics_class
class Signature(Magics):

    @line_magic
    def signature(self, line):
        sig = '''Author: <a href="http://ramiro.org/">Ramiro Gómez</a>
            • Last edited: {}<br>{} {} - {} {} - IPython {} - matplotlib {} - numpy {} - pandas {}'''.format(
                datetime.now().strftime('%B %d, %Y'),
                platform.system(),
                platform.release(),
                platform.python_implementation(),
                platform.python_version(),
                IPython.__version__,
                matplotlib.__version__,
                numpy.__version__,
                pandas.__version__)

        return display.HTML(sig)


def load_ipython_extension(ipython):
    ipython.register_magics(Signature)
