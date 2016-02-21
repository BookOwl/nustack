#!python3
"Shell support."
from nustack.extensionbase import Module, Token
module = Module("std::Shell")

import subprocess, shlex, sys

if sys.platform == "win32":
    out = subprocess.check_output("chcp", shell=True)
    enc = "cp" + out.split()[-1].decode()
else:
    # UNTESTED. Untill I can check this works, assume utf8
    #enc = subprocess.check_output("locale charmap", shell=True).decode()
    enc = "utf8"

@module.register("encoding")
def encoding(env) -> "( -- s)":
    "Returns the character encoding of the shell"
    env.stack.push(Token("lit_string", enc))

@module.register("run")
def run(env) -> "(s1 -- l)":
    """Runs s1 as a shell command string and returns a two item list [return-code output]
    Note that this run using the subprocess module with shell=False,
    so if you need to use a built in shell command use run.shell"""
    args = env.stack.pop().val
    args = shlex.split(args)
    try:
        out = subprocess.check_output(
                args,
                stderr=subprocess.STDOUT,
                shell=False,
        )
        ret = 0
    except subprocess.CalledProcessError as e:
        out = e.output
        ret = e.returncode
    env.stack.push(Token('lit_list', [Token('lit_int', ret), Token('lit_string', out.decode(enc))]))

@module.register("run.shell")
def run_shell(env) -> "(s1 -- l)":
    """Runs s1 as a shell command string and returns a two item list [return-code output]
    Note that this run using the subprocess module with shell=True, which can be a security risc!"""
    args = env.stack.pop().val
    args = shlex.split(args)
    try:
        out = subprocess.check_output(
                args,
                stderr=subprocess.STDOUT,
                shell=True,
        )
        ret = 0
    except subprocess.CalledProcessError as e:
        out = e.output
        ret = e.returncode
    env.stack.push(Token('lit_list', [Token('lit_int', ret), Token('lit_string', out.decode(enc))]))
