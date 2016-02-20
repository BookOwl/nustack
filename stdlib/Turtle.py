#!python3
"Turtle - Turtle graphics for Nustack.\nImport with `std::Turtle import"
import turtle
from nustack.extensionbase import Module, Token
module = Module("std::Turtle")

def start():
    if not start.started:
        turtle.Screen().title("Nustack Turtle Graphics")
        start.started = True
start.started = False

@module.register("Turtle")
def Turtle(env) -> "( -- turtle)":
    "Creates a new turtle"
    start()
    t = Token("lit_turtle", turtle.Turtle())
    env.stack.push(t)

@module.register("Screen")
def Screen(env) -> "( -- screen)":
    start()
    "Returns the Screen used by turtles"
    s = Token("lit_screen", turtle.Screen())
    env.stack.push(s)

@module.register("config.screen")
def config_screen(env) -> "(screen l -- screen)":
    """Configs the screen according to the options given in l.
    l[0] is the title, and the rest of the list configures the screen size."""
    screen, options = env.stack.popN(2)
    title, size = options.val[0], options.val[1:]
    screen.val.title(title.val)
    screen.val.setup(*[t.val for t in size])
    env.stack.push(screen)

@module.register("fd")
def fd(env) -> "(turtle n -- turtle)":
    "Moves the turtle forward n steps"
    t, n = env.stack.popN(2)
    t.val.fd(n.val)
    env.stack.push(t)

@module.register("rt")
def rt(env) -> "(turtle n -- turtle)":
    "Moves the turtle forward n steps"
    t, n = env.stack.popN(2)
    t.val.rt(n.val)
    env.stack.push(t)

@module.register("lt")
def lt(env) -> "(turtle n -- turtle)":
    "Moves the turtle forward n steps"
    t, n = env.stack.popN(2)
    t.val.lt(n.val)
    env.stack.push(t)

@module.register("pd")
def pd(env) -> "(turtle -- turtle)":
    "Sets the turtles pen to down"
    t = env.stack.pop()
    t.val.pd()
    env.stack.push()

@module.register("pu")
def pu(env) -> "(turtle -- turtle)":
    "Sets the turtles pen to up"
    t = env.stack.pop()
    t.val.up()
    env.stack.push(t)

@module.register("pensize")
def lt(env) -> "(turtle n -- turtle)":
    "Sets the turtle's pensize to n"
    t, n = env.stack.popN(2)
    t.val.pensize(n.val)
    env.stack.push(t)

@module.register("pencolor")
def lt(env) -> "(turtle a -- turtle)":
    "Sets the turtle's pensize to a, which is a 3 item list or a string"
    t, color = env.stack.popN(2)
    if color.type == 'lit_list':
        t.val.pencolor(*[t.val for t in color.val])
    else:
        t.val.pencolor(color.val)
    env.stack.push(t)

@module.register("get.pos")
def get_pos(env) -> "(turtle -- turtle x y)":
    "Returns the position of the turtle"
    t = env.stack.pop()
    pos =  t.val.pos()
    env.stack.push(t, *[Token("lit_float", cord) for cord in pos])

@module.register("set.pos")
def set_pos(env) -> "(turtle x y -- turtle)":
    "Sets the position of the turtle to x, y"
    t, x, y = env.stack.popN(3)
    t.val.setpos(x.val, y.val)
    env.stack.push(t)

@module.register("get.dir")
def get_dir(env) -> "(turtle -- turtle n)":
    "Returns the direction of the turtle"
    t = env.stack.pop()
    d = t.val.heading()
    env.stack.push(t, Token("lit_float", d))

@module.register("set.dir")
def set_dir(env) -> "(turtle n -- turtle)":
    "Sets the direction of the turtle"
    t, d = env.stack.popN(2)
    t.val.seth(d.val)
    env.stack.push(t)

@module.register("dot")
def dot(env) -> "(turtle n -- turtle)":
    "Creates a dot of size n"
    t, n = env.stack.popN(2)
    t.val.dot(n.val)
    env.stack.push(t)

@module.register("write")
def write(env) -> "(turtle s -- turtle)":
    "Writes s at the current turtle position"
    t, s, size = env.stack.popN(3)
    print(("Arial", size.val, "normal"))
    t.val.write(s.val, font=("Arial", size.val, "normal"))
    env.stack.push(t)

@module.register("speed")
def speed(env) -> "(turtle n -- turtle)":
    "Sets the speed of the turtle to n"
    t, n = env.stack.popN(2)
    t.val.speed(n.val)
    env.stack.push(t)

@module.register("hide")
def hide(env) -> "(turtle -- turtle)":
    "Hides the turtle"
    t = env.stack.pop()
    t.val.ht()
    env.stack.push(t)

@module.register("show")
def show(env) -> "(turtle -- turtle)":
    "Shows the turtle"
    t = env.stack.pop()
    t.val.st()
    env.stack.push(t)

@module.register("done")
def done(env) -> "( -- )":
    "Starts turtle graphics main loop. Must be last function run"
    turtle.done()
