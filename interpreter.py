#!python3
import types, os
from nustack import tokenize
from nustack.stdlib import builtins

class StackUnderflowError(Exception): pass
class ScopeUnderflowError(Exception): pass
class ScopeLookupError(Exception): pass

class Stack:
    def __init__(self, start=None):
        if start:
            self._stack = list(start)
        else:
            self.clear()

    def clear(self):
        self._stack = []

    def pop(self):
        if len(self) == 0:
            raise StackUnderflowError("Stack is empty!")
        return self._stack.pop()

    def popN(self, n):
        pops = reversed([self.pop() for _ in range(n)])
        return tuple(pops)

    def push(self, *args):
        for arg in args:
            self._stack.append(arg)

    def __len__(self):
        return len(self._stack)

    def __repr__(self):
        return "Stack( %s )" % repr(self._stack)

class Scope:
    def __init__(self):
        self._scopes = []
        self.pushScope()

    def pushScope(self, scope=None):
        if scope == None:
            self._scopes.append({})
        else:
            self._scopes.append(scope)

    def popScope(self):
        if len(self._scopes) <= 1:
            raise ScopeUnderflowError("Can not pop global scope!")
        self._scopes.pop()

    def lookup(self, name):
        for scope in reversed(self._scopes):
            if name in scope:
                return scope[name]
        raise ScopeLookupError("%s does not exist!" % name)

    def assign(self, name, val):
        self._scopes[-1][name] = val

    def getGlobal(self, name):
        try:
            return self._scopes[0][name]
        except KeyError:
            raise ScopeLookupError("%s does not exist!" % name)

    def __repr__(self):
        return "Scope: %s" % repr(self._scopes)

class Interpreter:
    def __init__(self):
        self._reset()
        self.file = os.path.abspath(os.curdir)

    def getDir(self):
        if '.' in os.path.basename(self.file):
            return os.path.dirname(self.file)
        else:
            return env.file

    def run(self, code, file=None):
        if not file:
            self.file = os.path.abspath(os.curdir)
        else:
            self.file = os.path.abspath(file)
        self._code = code
        self._reset()
        self._parse()
        self.eval(self._code)
        return self.stack, self.scope

    def _reset(self):
        self.stack = Stack()
        self.scope = Scope()

    def _parse(self):
        self._toks = tokenize.tokenize(self._code)

    def eval(self, code):
        if type(code) == str:
            toks = tokenize.tokenize(code)
        else:
            toks = code
        for tok in toks:
            # Push any literals to the stack
            if tok.type.startswith("lit_"):
                self.stack.push(tok)
            # Create a list
            elif tok.type == "listend":
                contents = []
                while True:
                    thing = self.stack.pop()
                    if thing.type == "lit_liststart":
                        break
                    contents.append(thing)
                self.stack.push(tokenize.Token("lit_list", list(reversed(contents))))
            # "Call" something
            elif tok.type == "call":
                # This is the tricky one
                # First, if we are actually loading something from a module ("Mod::thing"), split it up around the "::"
                if "::" in tok.val:
                    valname = tok.val.split("::")
                else:
                    # Else, we are only getting the top-leval object
                    valname = [tok.val]
                # Now we locate it
                try:
                    # First, we try to look it up through the scpes
                    val = self.scope.lookup(valname[0])
                except ScopeLookupError:
                    # If it's not defined by the program, it might be a builtin. If it's not, the builtins module will raise a NotDefinedError
                    f = builtins.module.get(valname[0])
                    f(self)
                else:
                    # The scope lookup completed without an error
                    # If len(valname) > 1, we need to lookup any sub-modules
                    if len(valname) > 1:
                        # Lookup any sub-modules
                        top = valname[0]
                        valname = valname[1:]
                        for name in valname:
                            val = val.get(name)
                        if type(val) == types.FunctionType:
                            # If the final value is a function, we call it. This is how extension modules work
                            val(self)
                        elif val.type == "lit_code":
                            # We got a Nustack function, so we should call it.
                            topscope = self.scope.getGlobal(top)
                            self.scope.pushScope(topscope.scope)
                            self.eval(val.val)
                            self.scope.popScope()
                        else:
                            # Else, we got a iteral and we should push it on the stack
                            self.stack.push(val)
                    # Otherwise, we just directly handle the value
                    elif type(val) == types.FunctionType:
                        val(self)
                    elif val.type != "lit_code":
                        # If the value is not code, push it to the stack
                        self.stack.push(val)
                    else:
                        # Else, call it with a new scope.
                        self.scope.pushScope()
                        self.eval(val.val)
                        self.scope.popScope()
