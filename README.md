[![Join the chat at https://gitter.im/BookOwl/nustack](https://badges.gitter.im/BookOwl/nustack.svg)](https://gitter.im/BookOwl/nustack?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Build Status](https://travis-ci.org/BookOwl/nustack.svg?branch=tests)](https://travis-ci.org/BookOwl/nustack) [![Codacy Badge](https://api.codacy.com/project/badge/grade/41debe98009e4455bdd96eb20b6606f8)](https://www.codacy.com/app/stanleybookowl/nustack)

# Nustack
Nustack is a stack-oriented concatenative programming language with support for high-level modular programming and Python integration.
For an excellent introduction to concatenative programming, please see http://evincarofautumn.blogspot.com/2012/02/why-concatenative-programming-matters.html?m=1

## Installing.
Run `pip install nustack`

Nustak has been tested on Pythons 3.2-3.5, 3.6-nightly, and PyPy3 but should also work Python 3.1
## Running
To run a Nustack program, just run the following command line: `nustack path/to/program.nu`

`nustack` starts the Nustack interactive prompt.

For a full lists of options, run `nustack -h`

## Help
Currently, there is little documentation for Nustack, but I am working on it. For now, create an issue with your questions, ask on gitter, or post them in the [Nustack Scratch forum topic](https://scratch.mit.edu/discuss/topic/184118/)
## Examples
Here is an example Nustack program:

```
/* examples/testprog.nu */
`std::IO importext
`std::Time importext
`std::Control importext /* Import the IO, Time and Control modules */
'file.txt' "r" IO::open IO::readall IO::close /*Open, read, and close the file 'file.txt' */
show /*Show the contents of the file*/
{ "spam" show /*Print spam*/
  1 Time::sleep /*Pause for 1 second*/
} `spam define
{ spam } Control::forever
```

Here is a more complex example that draws a tree using the Turtle module:

```
/* turtle_tree.nu - A recursive tree drawn with turtle graphics. */
/* Import the Seq and Turtle modules */
`Seq import `Turtle import*

/* Set up the turtle and the states list */
Turtle `t define
[] `states define

/* Save the turtle's current state */
{`tcopy def [tcopy get.pos rot get.dir swap drop] states swap Seq::append tcopy} `save.state define

/* Set the turtle's state to the last one saved */
{`tcopy def states Seq::pop `newstate def
  tcopy pu
  tcopy newstate 0 Seq::nth newstate 1 Seq::nth set.pos
  tcopy newstate 2 Seq::nth  set.dir
  tcopy pd
  } `pop.state define

/* Here is the tree function */
{`angle def `d def `n def `t def /* Save our arguments */
  n 0 eq /* Test if we have hit the base case */
  {t "#0fd268" /*green*/ pencolor 10 dot "#4f3c0c" pencolor} /* If so, draw a leaf */
  { /* Else, recursivly draw the rest of the tree */
    t save.state
    t n pensize
    d fd
    angle rt n 1 - d 0.7 * angle tree
    t angle 2 * lt n 1 - d 0.7 * angle tree
    t pop.state
  }
  if
} `tree def

/* Configure the screen */
Screen ["Nustack Turtle Graphics - Recursive Tree" 600 500] config.screen
/* Write some text */
t pu -280 200 set.pos "Recursive Tree" 20 write

/* Get the turtle ready to draw */
t pu 0 -250 set.pos 90 set.dir pd
t "#4f3c0c" /*brown*/ pencolor
hide.turtle 0 speed /* 0 speed means no animation */

/* Draw the tree. */
"Turtle" "How many iterations?" number.input `iters def
"Turtle" "What is the length of the first segment?" number.input `len def
"Turtle" "What is the branching angle?" number.input `angle def
t iters len angle tree
/* Start the turtle mainloop so that our drawing stays on the screen. */
done
```
Here is a screenshot:

![Screenshot](/screenshots/screenshot1.png)

Both example programs can be found in the examples directory.
