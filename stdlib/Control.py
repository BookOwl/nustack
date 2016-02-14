from nustack.extensionbase import Module, Token

module = Module()

shouldbreak = False

@module.register("forever")
def forever(env):
    global shouldbreak
    code = env.stack.pop().val
    while True:
        if shouldbreak:
            shouldbreak = False
            break
        env.eval(code)

@module.register("break")
def break_(env):
    global shouldbreak
    shouldbreak = True

@module.register("while")
def while_(env):
    global shouldbreak
    cond, code = env.stack.popN(2)
    while True:
        env.eval(cond.val)
        if not env.stack.pop().val or shouldbreak:
            shouldbreak = False
            break
        env.eval(code.val)
