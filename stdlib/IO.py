#!python3
"IO - basic file IO\nImport with `std::IO importext"
import os.path
from nustack.extensionbase import Module, Token

module = Module("std::IO")

@module.register("open")
def open_(env) -> "(s s -- file)":
    "Pops a string naming a file path and a string used as open flags, returns a file object"
    name, flags = env.stack.popN(2)
    path = env.getDir()
    path = os.path.join(path, name.val)
    f = open(path, flags.val)
    t = Token("file", f)
    env.stack.push(t)

@module.register("readall")
def readall(env) -> "(file -- s file)":
    "Takes a file object, reads everything from it as a string, and returns that string and the original file object"
    f = env.stack.pop()
    cont = f.val.read()
    env.stack.push(Token("lit_string", cont), f)

@module.register("read.n")
def readn(env) -> "(file i -- s file)":
    "Takes a file object and an integer i, reads i charactors or bytes from it as a string, and returns that string and the original file object"
    f, n = env.stack.popN(2)
    cont = f.val.read(n.val)
    env.stack.push(Token("lit_string", cont), f)

@module.register("write")
def write(env) -> "(file s -- file)":
    "Takes a file object and a string, writes that string to the file, and returns the file"
    f, s =  env.stack.popN(2)
    f.val.write(s.val)
    env.stack.push(f)
@module.register("close")
def close(env) -> "(file -- )":
    "Takes a file object and closes it. Returns nothing"
    f = env.stack.pop()
    f.val.close()
