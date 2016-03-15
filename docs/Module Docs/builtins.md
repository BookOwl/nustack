
# Nustack Standard Library
You don't need to import this, it is loaded automatically.
## Exported Functions:

### %, mod
`(n n -- n)`

Returns the modulo of 2 numbers


### &, and
`(b1 b2 -- b)`

Returns true if b1 and b2 are true


### *, mul
`(n n -- n)`

Multiplies 2 numbers


### <, lt
`(a1 a2 -- b)`

Returns true if a1 < a2


### >, gt
`(a1 a2 -- b)`

Returns true if a1 > a2


### add, +
`(n n -- n)`

Adds two numbers


### argv
`( -- l)`

Returns a list of the command line arguments passed to the program.
The first item is either the name of the program or <<INTERACTIVE>>


### break
`( -- )`

Breaks out of a loop


### call
`(code -- )`

Runs `code`, which can be either a code object or a python function


### cond
`(l -- )`

Takes a list of 2 item lists.
The first item must be a code object that is run to produce a boolean value.
If the result of running the first code object is `#t`, the second item in the list,
which must be a code object, is run.


### define, def
`(a s -- )`

Defines a value in the current scope


### div, /
`(n n -- n)`

Divides 2 numbers


### do.while
`(c c -- )`

Pops two code objects. While running the first code object results in #t, the second code object is run.
The second code object is run at least once.


### drop
`(a -- )`

Pops the top of the stack


### dup
`(a -- a a)`

Duplicates the top of the stack


### eq, =
`(a1 a2 -- b)`

Returns true if the top two values on the stack equal each other


### filter
`(sequence1 c -- sequence2)`

Filters a sequence.


### for.each
`(sequence c -- )`

Calls a code object for each item of a sequence


### forever
`(c -- )`

Executes a code object repeatedly forever


### if
`(b c c -- )`

Performs if branching


### imp, import
`(sym -- )`

None


### import*, imp*
`(sym -- )`

None


### in, input
`(a -- s)`

Shows a, prompts for input, and returns it as a string


### lookup
`(sym -- any)`

Returns the variable that has the name of sym's val. Useful for dynamic variable lookup


### map
`(sequence1 c -- sequence2)`

Maps a code object over each item of a sequence and collects the results as a new list.


### not
`(b1 -- b)`

Returns true if b1 and b2 are true


### or, |
`(b1 b2 -- b)`

Returns true if b1 or b2 are true


### over
`(a1 a2 -- a1 a2 a1)`

Adds the item next to the top of the stack to the top of the stack


### peek
`(a -- a)`

Shows the top of the stack without popping it.


### peek.repr
`(a -- a)`

Shows the top of the stack and its type without popping it.


### raise
` none `

None


### raise.details
` none `

None


### reduce
`(sequence1 a c -- a)`

Reduces a sequence to a single value


### repeat.n
`(cn -- )`

Calls c n times


### rot
`(a1 a2 a3 -- a2 a3 a1)`

Rotates the top 3 items on the stack


### show
`(a -- )`

Shows the top of the stack


### show.repr
`(a -- a)`

Shows the top of the stack and its type


### show.scopes
`( -- )`

Shows the current scopes


### sub, -
`(n n -- n)`

Subtracts 2 numbers


### swap
`(a1 a2 -- a2 a1)`

Swaps the two things on top of the stack


### to.bool
`(a -- b)`

Pops a value a from the stack and converts it to a bool


### to.float
`(a -- f)`

Pops a value a from the stack and converts it to a float


### to.int
`(a -- i)`

Pops a value a from the stack and converts it to an int


### to.string
`(a -- s)`

Pops a value a from the stack and converts it to a string


### to.symbol
`(a -- sym)`

Pops a value a from the stack and converts it to a symbol


### try
` none `

None


### while
`(c c -- )`

Pops two code objects. While running the first code object results in #t, the second code object is run.
The second code object might not run at all


