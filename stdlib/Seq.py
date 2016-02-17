#!python3
"Seq - Sequence operations\nImport with `std::Seq import"

from nustack.extensionbase import Module, Token
module = Module("std::Seq")

@module.register("nth")
def nth(env) -> "(sequence n -- a)":
    "Returns the nth item of a sequence (eg. list or string)"
    seq, n = env.stack.popN(2)
    a = seq.val[n.val]
    if isinstance(a, Token):
        env.stack.push(a)
    else:
        env.stack.push(Token("lit_any", a))

@module.register("first")
def first(env) -> "(sequence -- a)":
    seq = env.stack.pop()
    a = seq.val[0]
    if isinstance(a, Token):
        env.stack.push(a)
    else:
        env.stack.push(Token("lit_any", a))

@module.register("rest")
def first(env) -> "(sequence -- a)":
    seq = env.stack.pop()
    a = seq.val[1:]
    if isinstance(a, Token):
        env.stack.push(a)
    else:
        env.stack.push(Token("lit_any", a))

@module.register("slice")
def slice_(env) -> "(sequence1 n1 n2 -- sequence2)":
    "Slices a seuence from n1 to n2"
    seq, n1, n2 = env.stack.popN(3)
    t = seq.type
    env.stack.push(Token(t, seq.val[n1.val:n2.val]))

@module.register("set.nth")
def set_nth(env) -> "(sequence a n -- sequence)":
    seq, a, n = env.stack.popN(3)
    if seq.type == "lit_string":
        s = seq.val
        newstr = s[0:n.val] + a.val + s[n.val+1:]
        env.stack.push(Token("lit_string", newstr))
    else:
        seq.val[n.val] = a
        env.stack.push(seq)

@module.register("for.each")
def for_each(env) -> "(sequence c -- )":
    "Calls a code object for each item of a sequence"
    seq, code = env.stack.popN(2)
    for item in seq.val:
        if isinstance(item, Token):
            env.stack.push(item)
        else:
            env.stack.push(Token("lit_any", item))
        env.eval(code.val)

@module.register("map")
def map_(env) -> "(sequence1 c -- sequence2)":
    "Maps a code object over each item of a sequence and collects the results as a new list."
    seq, code = env.stack.popN(2)
    res = []
    for item in seq.val:
        if isinstance(item, Token):
            env.stack.push(item)
        else:
            env.stack.push(Token("lit_any", item))
        env.eval(code.val)
        res.append(env.stack.pop())
    env.stack.push(Token("lit_list", res))

@module.register("filter")
def filter_(env) -> "(sequence1 c -- sequence2)":
    "Filters a sequence."
    seq, code = env.stack.popN(2)
    res = []
    for item in seq.val:
        if isinstance(item, Token):
            item = item
        else:
            item = Token("lit_any", item)
        env.stack.push(item)
        env.eval(code.val)
        cond = env.stack.pop().val
        if cond:
            res.append(item)
    env.stack.push(Token("lit_list", res))

@module.register("reduce")
def reduce_(env) -> "(sequence1 a c -- a)":
    "Reduces a sequence to a single value"
    seq, start, code = env.stack.popN(3)
    for item in seq.val:
        if isinstance(item, Token):
            item = item
        else:
            item = Token("lit_any", item)
        env.stack.push(start, item)
        env.eval(code.val)
        start = env.stack.pop()
    env.stack.push(start)

@module.register("reverse")
def reverse_(env) -> "(sequence1 -- sequence2)":
    "Reverses a sequence"
    seq = env.stack.pop()
    rev = seq.val[::-1]
    env.stack.push(Token(seq.type, rev))

@module.register("range")
def range_(env) -> "(n n -- l)":
    start, stop = env.stack.popN(2)
    step = 1 if start.val < stop.val else -1
    res = [Token("lit_int", i) for i in range(start.val, stop.val, step)]
    env.stack.push(Token("lit_list", res))

@module.register("range.step")
def range_step(env) -> "(n n -- l)":
    start, stop, step = env.stack.popN(3)
    res = [Token("lit_int", i) for i in range(start.val, stop.val, step.val)]
    env.stack.push(Token("lit_list", res))
