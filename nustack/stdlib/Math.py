#!python3
"""Math - Math ops

All of the trigometric words give and take radians. You can use to.degrees to convert to degrees."""
from nustack.extensionbase import Module, Token
import math, fractions
module = Module("std::Math")

@module.register("ceil")
def ceil(env) -> "(n -- n)":
    "Returns the ceiling of n"
    n = env.stack.pop()
    env.stack.push(Token(n.type, math.ceil(n.val)))

@module.register("floor")
def cfloor(env) -> "(n -- n)":
    "Returns the floor of n"
    n = env.stack.pop()
    env.stack.push(Token(n.type, math.floor(n.val)))

@module.register("abs")
def abs_(env) -> "(n -- n)":
    "Returns the abs of n"
    n = env.stack.pop()
    env.stack.push(Token(n.type, abs(n.val)))

@module.register("factorial")
def fact(env) -> "(n -- n)":
    "Returns the factorial of n"
    n = env.stack.pop()
    env.stack.push(Token(n.type, math.factorial(n.val)))

@module.register("modf")
def modf(env) -> "(n -- f f)":
    "Returns the fractional and integer parts of n"
    n = env.stack.pop()
    r = math.modf(n.val)
    env.stack.push(Token("lit_float", r[0]), Token("lit_float", r[1]))

@module.register("exp")
def exp(env) -> "(n -- n)":
    "Returns the e**n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.exp(n.val)))

@module.register("ln")
def ln(env) -> "(n -- n)":
    "Returns the natural log of n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.log(n.val)))

@module.register("log")
def log(env) -> "(n base -- n)":
    "Returns the base log of n"
    n, b = env.stack.pop()
    env.stack.push(Token("lit_float", math.log(n.val), b.val))

@module.register("sqrt")
def sqrt(env) -> "(n -- n)":
    "Returns the square root of n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.sqrt(n.val)))

@module.register("cos")
def cos(env) -> "(n -- n)":
    "Returns the cosine of n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.cos(n.val)))

@module.register("sin")
def sin(env) -> "(n -- n)":
    "Returns the sine of n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.sin(n.val)))

@module.register("tan")
def cos(env) -> "(n -- n)":
    "Returns the tangent of n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.tan(n.val)))

@module.register("acos")
def cos(env) -> "(n -- n)":
    "Returns the arc cosine of n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.acos(n.val)))

@module.register("asin")
def sin(env) -> "(n -- n)":
    "Returns the arc sine of n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.asin(n.val)))

@module.register("atan")
def cos(env) -> "(n -- n)":
    "Returns the arc tangent of n"
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.atan(n.val)))

@module.register("atan2")
def atan2(env) -> "(x y -- n)":
    "Returns the atan of y/x, but adjusted for x and y's signs."
    x, y = env.stack.popN(2)
    env.stack.push(Token("lit_float", math.atan2(y.val, x.val)))

@module.register("hypot")
def hypot(env) -> "(x y -- n)":
    "Returns sqrt(x**2 + y**2)."
    x, y = env.stack.popN(2)
    env.stack.push(Token("lit_float", math.hypot(x.val, y.val)))

@module.register("to.degrees")
def deg(env) -> "(n -- n)":
    "Converts n from radians to degrees."
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.degrees(n.val)))

@module.register("to.radians")
def rad(env) -> "(n -- n)":
    "Converts n from degrees to radians."
    n = env.stack.pop()
    env.stack.push(Token("lit_float", math.radians(n.val)))

@module.register("gcd")
def gcd(env) -> "(x y -- n)":
    "Returns the gcd of x and y"
    x, y = env.stack.popN(2)
    env.stack.push(Token("lit_float", fractions.gcd(y.val, x.val)))
