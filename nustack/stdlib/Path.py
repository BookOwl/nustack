#!python3
"""Path - Path, file, and directory operations
Import with `std::Path import

In this module, `path` always refers to a string that is a pathname."""

import os, os.path, glob
from nustack.extensionbase import Module, Token
module = Module("std::Path")


@module.register("change.dir")
def change_dir(env) -> "(path -- )":
    "Changes the current working directory to path"
    os.chdir(env.stack.pop().val)

@module.register("get.cwd")
def get_cwd(env) -> "( -- path)":
    "Returns the path of the current working directory"
    env.stack.push(Token("lit_string", os.getcwd()))

@module.register("list.dir")
def list_dir(env) -> "(path -- list)":
    "Lists all the directories and files in a directory given by path"
    path = env.stack.pop().val
    listing = os.listdir(path)
    env.stack.push(Token("lit_list", [Token("lit_string", item) for item in listing]))

@module.register("make.dir")
def make_dir(env) -> "(path -- )":
    "Creates the directory given by path"
    os.mkdir(env.stack.pop().val)

@module.register("make.dirs")
def make_dirs(env) -> "(path -- )":
    "Creates the directory given by path. Like make.dir, but makes all intermediate-level directories needed to contain the leaf directory"
    os.mkdirs(env.stack.pop().val)

@module.register("remove.dir")
def remove_dir(env) -> "(path -- )":
    "Deletes the directory given by path as long as it is empty."
    os.rmdir(env.stack.pop().val)

@module.register("delete")
def delete(env) -> "(path -- )":
    "Deletes the file given by path."
    os.remove(env.stack.pop().val)

@module.register("join")
def join(env) -> "(path1 path2 -- path3)":
    "Joins two strings together to make a new path"
    p1, p2 = env.stack.popN(2)
    p3 = Token("lit_string", os.path.join(p1.val, p2.val))

@module.register("abspath")
def abspath(env) -> "(path -- path)":
    "Returns the absolute version of path"
    env.stack.push(Token("lit_string", os.path.abspath(env.stack.pop().val)))

@module.register("base.name")
def basename(env) -> "(path -- path)":
    "Returns the base name of path"
    env.stack.push(Token("lit_string", os.path.basename(env.stack.pop().val)))

@module.register("dir.name")
def dirname(env) -> "(path -- path)":
    "Returns the directory name of path"
    env.stack.push(Token("lit_string", os.path.dirname(env.stack.pop().val)))

@module.register("exists?")
def exists(env) -> "(path -- bool)":
    "Returns #t if path exists."
    env.stack.push(Token("lit_bool", os.path.exists(env.stack.pop().val)))

@module.register("size")
def size(env) -> "(path -- int)":
    "Returns the size of the file given by path in bytes"
    env.stack.push(Token("lit_int", os.path.getsize(env.stack.pop().val)))

@module.register("is.dir?")
def is_dir(env) -> "(path -- bool)":
    "Returns #t if path is a directory"
    env.stack.push(Token("lit_bool", os.path.isdir(env.stack.pop().val)))

@module.register("is.file?")
def is_file(env) -> "(path -- bool)":
    "Returns #t if path is a file"
    env.stack.push(Token("lit_bool", os.path.isfile(env.stack.pop().val)))

@module.register("is.link?")
def is_link(env) -> "(path -- bool)":
    "Returns #t if path is a directory entry that is a symbolic link"
    env.stack.push(Token("lit_bool", os.path.islink(env.stack.pop().val)))

@module.register("glob")
def glob_(env) -> "(pattern -- list)":
    "Returns a list of file names that match the pattern `pattern`"
    pattern = env.stack.pop().val
    matches = glob.glob(pattern)
    env.stack.push(Token("lit_list", [Token("lit_string", match) for match in matches]))
