#!python3
# Nustack extension module base class
from nustack.tokenize import Token # Re-export Token
class Module:
    def __init__(self):
        self.contents = {}
    def register(self, *names):
        def dec(f):
            for name in names:
                self.contents[name] = f
            return f
        return dec
    def get(self, name):
        return self.contents[name]
