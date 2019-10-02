from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)

# The class MUST call this class decorator at creation time
@magics_class
class Parser(Magics):

    @line_magic
    def extract(self, line):
        value = 1
        error = None
        return value, error

def load_ipython_extension(ipython):
    ipython.register_magics(Parser)