import os.path
from nustack.extensionbase import Module, Token

module = Module()

@module.register("open")
def open_(env):
    name, flags = env.stack.popN(2)
    path = env.getDir()
    path = os.path.join(path, name.val)
    f = open(path, flags.val)
    t = Token("lit_file", f)
    env.stack.push(t)

@module.register("readall")
def readall(env):
    f = env.stack.pop()
    cont = f.val.read()
    env.stack.push(Token("lit_string", cont), f)

@module.register("read.n")
def readn(env):
    f, n = env.stack.popN(2)
    cont = f.val.read(n.val)
    env.stack.push(Token("lit_string", cont), f)

@module.register("write")
def write(env):
    f, s =  env.stack.popN(2)
    f.val.write(s.val)
    env.stack.push(f)
@module.register("close")
def close(env):
    f = env.stack.pop()
    f.val.close()
