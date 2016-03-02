#!python3
"Hash - Hash table creation and operations\nImport with `std::Hash import"

from nustack.extensionbase import Module, Token
module = Module("std::Hash")

@module.register("empty")
def empty_hash(env) -> "( -- hash)":
    "Creates an empty hash table"
    env.stack.push(Token("lit_hash", dict()))

@module.register("from.list")
def from_list(env) -> "(list -- hash)":
    "Creates a hash from a list of [key value] lists"
    l = env.stack.pop().val
    env.stack.push(Token("lit_hash", {k:v for (k, v) in l}))

@module.register("get")
def get(env) -> "(hash key -- value)":
    "Retrieves the value asociated with the key in the hash"
    hash, key = env.stack.popN(2)
    env.stack.push(hash.val[key])

@module.register("set")
def set(env) -> "(hash key value -- hash)":
    "Sets the value asociated with the key in the hash"
    hash, key, val, = env.stack.popN(3)
    hash.val[key] = val
    env.stack.push(hash)

@module.register("del")
def delete(env) -> "(hash key -- hash)":
    "Deletes the value asociated with the key in the hash"
    hash, key = env.stack.popN(2)
    del hash.val[key]
    env.stack.push(hash)

@module.register("items")
def items(env) -> "(hash -- list)":
    "Returns a list of [key value] lists taken from the hash"
    hash = env.stack.pop().val
    env.stack.push(Token("lit_list", [Token("lit_list", val) for val in hash.items()]))
