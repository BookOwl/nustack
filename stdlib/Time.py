#!python3
import time
from nustack.extensionbase import Module, Token

module = Module()

@module.register("time")
def time_(env):
    env.stack.push(Token("lit_float", time.time()))

@module.register("sleep")
def sleep(env):
    n = env.stack.pop().val
    time.sleep(n)

@module.register("ctime")
def ctime(env):
    n = env.stack.pop().val
    env.stack.push(Token("lit_string", time.ctime(n)))
