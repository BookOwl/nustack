#!python3
# Nustack extension module base class
from nustack.tokenize import Token # Re-export Token
class NotDefinedError(Exception): pass

class Module:
    def __init__(self, modname=""):
        self.contents = {}
        self.modname = modname
    def register(self, *names):
        def dec(f):
            for name in names:
                self.contents[name] = f
            return f
        return dec
    def get(self, name):
        try:
            return self.contents[name]
        except KeyError:
            raise NotDefinedError("%s is not defined in module %s!" % (name, self.modname))
