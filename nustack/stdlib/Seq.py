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

@module.register("butfirst")
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

@module.register("append")
def append(env) -> "(sequence a -- sequence)":
    "Appends a datum to a sequence"
    seq, a  = env.stack.popN(2)
    seq.val.append(a)
    env.stack.push(seq)

@module.register("pop")
def pop(env) -> "(sequence --  a)":
    "Pops an item from the end of a sequence"
    seq = env.stack.pop()
    env.stack.push(seq.val.pop())

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

@module.register("length", "len")
def length(env) -> "(sequence -- i)":
    "Return the length of a sequence"
    seq = env.stack.pop().val
    env.stack.push(Token("lit_int", len(seq)))

@module.register("contains")
def contains(env) -> "(sequence a -- b)":
    "Returns #t if the sequence contains a.\nDo not use this for string, use String::contains instead."
    seq, thing = env.stack.popN(2)
    b = thing in seq.val
    env.stack.push(Token("lit_bool", b))

@module.register("repeat")
def repeat(env) -> "(sequence1 i -- sequence2)":
    "Repeats sequence1 i times"
    seq, i = env.stack.popN(2)
    newseq = seq.val * i.val
    env.stack.push(Token(seq.type, newseq))

@module.register("pack2")
def pack2(env) -> "(a1 a2 -- [a1 a2])":
    "Creates a list from the top 2 items on the stack"
    env.stack.push(Token("lit_list", list(env.stack.popN(2))))

@module.register("pack3")
def pack3(env) -> "(a1 a2 a3 -- [a1 a2 a3])":
    "Creates a list from the top 3 items on the stack"
    env.stack.push(Token("lit_list", list(env.stack.popN(3))))

@module.register("pack.n")
def packn(env) -> "(... i -- l)":
    "Creates a list from the top i items on the stack not including i"
    i = env.stack.pop().val
    env.stack.push(Token("lit_list", list(env.stack.popN(i))))

@module.register("unpack")
def unpack(env) -> "(sequence -- a...)":
    "Unpacks a sequence"
    seq = env.stack.pop()
    if seq.type == "lit_string":
        seq = [Token("lit_string", c) for c in seq.val]
    else:
        seq = seq.val
    env.stack.push(*seq)
