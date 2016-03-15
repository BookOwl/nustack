
# Turtle - Turtle graphics for Nustack.
Import with `std::Turtle import
## Exported Functions:

### Screen
`( -- screen)`

Returns the Screen used by the turtles.


### Turtle
`( -- turtle)`

Creates a new turtle


### bye
`( -- )`

Shuts down the turtlegraphics window.


### clear
`(turtle -- turtle)`

Clears a turtle's drawings


### config.screen
`(screen l -- screen)`

Configs the screen according to the options given in l.
l[0] is the title, and the rest of the list configures the screen size.


### done
`( -- )`

Starts turtle graphics main loop. Must be last function run


### dot
`(turtle n -- turtle)`

Draws a dot of size n


### fd
`(turtle n -- turtle)`

Moves the turtle forward n steps


### get.dir
`(turtle -- turtle n)`

Returns the direction of the turtle


### get.pos
`(turtle -- turtle x y)`

Returns the position of the turtle


### hide.turtle
`(turtle -- turtle)`

Hides the turtle


### lt
`(turtle n -- turtle)`

Moves the turtle forward n steps


### number.input
`(title prompt -- n)`

Prompts for a number


### on.screen.click
`(turtle c i -- turtle)`

Runs the code object when ever the screene is clicked with the mouse button given by i


### on.turtle.click
`(turtle c i -- turtle)`

Runs the code object when ever the turtle is clicked with the mouse button given by i


### pd
`(turtle -- turtle)`

Sets the turtles pen to down


### pencolor
`(turtle a -- turtle)`

Sets the turtle's pensize to a, which is a 3 item list or a string


### pensize
`(turtle n -- turtle)`

Sets the turtle's pensize to n


### pu
`(turtle -- turtle)`

Sets the turtles pen to up


### rt
`(turtle n -- turtle)`

Moves the turtle forward n steps


### set.dir
`(turtle n -- turtle)`

Sets the direction of the turtle


### set.pos
`(turtle x y -- turtle)`

Sets the position of the turtle to x, y


### set.shape
`(turtle s -- turtle)`

Sets the shape of the turtle to s, which should be one of "arrow", "turtle", "circle", "square", "triangle", "classic"


### show.turtle
`(turtle -- turtle)`

Shows the turtle


### speed
`(turtle n -- turtle)`

Sets the speed of the turtle to n


### text.input
`(title prompt -- s)`

Prompts for a string


### turtle.size
`(turtle n -- turtle)`

Sets the sizeof the turtle to n


### write
`(turtle s -- turtle)`

Writes s at the current turtle position


