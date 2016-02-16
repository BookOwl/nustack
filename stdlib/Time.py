#!python3
"Time - time wrapper for Nustack\nImport with`std::Time importext"
import time
from nustack.extensionbase import Module, Token

module = Module("std::Time")

@module.register("time")
def time_(env) -> "( -- f)":
    "Returns the seconds since the epoch"
    env.stack.push(Token("lit_float", time.time()))

@module.register("sleep")
def sleep(env) -> "(n -- )":
    "Sleeps for n seconds"
    n = env.stack.pop().val
    time.sleep(n)

@module.register("ctime")
def ctime(env) -> "(n -- s)":
    "Converts n, the number of seconds since the epoch to a human readable time string"
    n = env.stack.pop().val
    env.stack.push(Token("lit_string", time.ctime(n)))

@module.register("timestr")
def timestr(env) -> "( -- s)":
    "Returns a human readable time string"
    n = env.stack.pop().val
    env.stack.push(Token("lit_string", time.ctime()))
