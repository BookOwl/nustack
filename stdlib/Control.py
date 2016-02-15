"Control - Extra control flow tools\nImport with `std::Control importext"
from nustack.extensionbase import Module, Token

module = Module('std::Control')

shouldbreak = False

@module.register("forever")
def forever(env) -> "(c -- )":
    "Executes a code object repeatedly forever"
    global shouldbreak
    code = env.stack.pop().val
    while True:
        if shouldbreak:
            shouldbreak = False
            break
        env.eval(code)

@module.register("break")
def break_(env) -> "( -- )":
    "Breaks out of a loop"
    global shouldbreak
    shouldbreak = True

@module.register("while")
def while_(env) -> "(c c -- )":
    "Pops two code objects. While running the first code object results in #t, the second code object is run."
    global shouldbreak
    cond, code = env.stack.popN(2)
    while True:
        env.eval(cond.val)
        if not env.stack.pop().val or shouldbreak:
            shouldbreak = False
            break
        env.eval(code.val)
