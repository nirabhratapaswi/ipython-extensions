def hello(line):
    ret = str(line) + " - is magic"
    print(ret)
    return ret

def load_ipython_extension(ipython):
    ipython.register_magic_function(hello, 'line')