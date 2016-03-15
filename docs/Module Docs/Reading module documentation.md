# Reading the module documentation
The first section in a module documentation page gives the name of the module and a short description of it.

The rest of the page describes all of the words exported by the module. Here is a sample description to demonstrate:

> ### close
> `(file -- )`
>
> Takes a file object and closes it. Returns nothing

This description is actually quite simple. The first line gives the name of the word, the second line gives that word's stack effect (more on that later), and the rest of the description describes the word. Simple, right?

## Stack effects
A stack effect is a simple description of what a word does to the stack. For example, the stack effect `(n -- s)` means that a number (an integer or float) is popped off the stack and a string is pushed onto the stack. Here is a complete table of most stack effect symbols and what they mean:

| Symbol  | Meaning |
---------------------
| i   | An integer |
| f   | A float |
| n   | An int or a float
| s   | A string |
| c   | A code object |
| l   | A list |
| a   | Anything |
| sym | A symbol |
| b   | A bool |

If a word deals with other types of data, it will explictly name it in the stack effect. For example, `(file -- )` means that a file object is popped off and nothing is pushed onto the stack.
