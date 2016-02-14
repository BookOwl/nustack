#!python3
# Nustack Standard Library
import os
import importlib
from nustack.tokenize import Token
import nustack.interpreter

class NotDefinedError(Exception): pass

class ScopeWrapper:
    def __init__(self, s):
        self.scope = s._scopes[0]
    def get(self, name):
        return self.scope[name]
    def __repr__(self):
        return "ScopeWrapper: " + repr(self.scope)

def getword(name):
    def notImplimented(env):
        raise NotDefinedError("%s doesn't exist!" % name)
    try:
        return builtins[name]
    except KeyError:
        return notImplimented
builtins = {}

def register(*names):
    def dec(f):
        for name in names:
            builtins[name] = f
        return f
    return dec

@register("show")
def show(env):
    "Shows the top of the stack"
    thing = env.stack.pop()
    print(thing.val)

@register("peek")
def peek(env):
    "Shows the top of the stack without popping it."
    thing = env.stack.pop()
    print(thing.val)
    env.stack.push(thing)

@register("peek.repr")
def peek(env):
    "Shows the top of the stack without popping it."
    thing = env.stack.pop()
    print(thing)
    env.stack.push(thing)

@register("+", "add")
def plus(env):
    "Adds two numbers"
    a, b = env.stack.popN(2)
    t = a.type
    env.stack.push(Token(t, a.val + b.val))

@register("-", "sub")
def sub(env):
    "Subtracts 2 numbers"
    a, b = env.stack.popN(2)
    t = a.type
    env.stack.push(Token(t, a.val - b.val))

@register("*", "mul")
def mul(env):
    'Multiplies 2 numbers'
    a, b = env.stack.popN(2)
    t = a.type
    env.stack.push(Token(t, a.val * b.val))

@register("/", "div")
def div(env):
    'Divides 2 numbers'
    a, b = env.stack.popN(2)
    t = a.type
    env.stack.push(Token(t, a.val / b.val))

@register("if")
def if_(env):
    'Performs if branching'
    b, t, f = env.stack.popN(3)
    if b.val:
        env.eval(t.val)
    else:
        env.eval(f.val)

@register("define", "def")
def define(env):
    'Defines a value in the current scope'
    val, name = env.stack.popN(2)
    env.scope.assign(name.val, val)

@register("show.scopes")
def show_scopes(env):
    'Shows the current scopes'
    from pprint import pprint
    print("Scopes")
    for s in reversed(env.scope._scopes):
        pprint(s)
        print()

@register("importnu")
def impnu(env):
    'Import Nustack module'
    curdir = env.getDir()
    name = env.stack.pop().val
    pth = "/".join(name.split("::"))
    try:
        f = open(os.path.join(curdir, pth) + ".nu", "r")
        code = f.read()
        f.close()
        interp = nustack.interpreter.Interpreter()
        _, s = interp.run(code)
        scope = ScopeWrapper(s)
        env.scope.assign(name, scope)
    except IOError as e:
        raise e

@register("importext")
def impext(env):
    'Import extension module'
    name = env.stack.pop().val
    if name.startswith("std::"):
        usestd = True
        name = name[5:]
    else:
        usestd = False
    name = ".".join(name.split("::"))
    if usestd:
        m = importlib.import_module("nustack.stdlib.%s" % name)
    else:
        try:
            m = importlib.import_module("nu_ext_" + name)
        except ImportError:
            m = importlib.import_module("nustack.stdlib.%s" % name)
    env.scope.assign(name, m.module)
