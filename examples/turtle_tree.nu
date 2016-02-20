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
