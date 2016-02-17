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
