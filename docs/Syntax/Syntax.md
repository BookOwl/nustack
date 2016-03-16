# Syntax
At Nustack's core, there are only three types of syntax, **Comments**, **Data**, and **Calls**.

### Comments
**Comment** are very simple in Nustack. All that you do is put your comment between a `/*` and a `*/`. Anything can go inside a comment, even new lines.

There are also single line comments that start with `//` and end with a new line.

### Data
**Data** are just literal values in your source code. All data is first class. Currently there are 5 kinds of data in stack:

#### Integers and Floats
**Integers** are just sequences of digits. For example, `1234567890` is an integer. **Floats** are decimals. `3.14159` is a float. Unlike in typed languages like C, there isn't really much of a distinction between the two other than integers are infinite precision and can be used in places floats cant. (It doesn't make sense to read 3.14 characters from a file, does it?)

#### Strings
**Strings** are just sequences of characters wrapped up in double or single quotes. They support most of the escape characters found in Python, including \\ for \, \n for newline, \' for ', \" for ", \b for backspace, \r for carriage return, \t for tab, and \v for vertical tab.

#### Bytes
**Bytes** are written the same way as strings except that they have a "b" in front of the first quote character. They are mostly useful for binary data and sockets.

#### Bools
**Bools** represent true and false. They are coded as `#t` and `#f`

#### Symbols
**Symbols** are much like strings, except that they must be made up of characters that can be used as identifiers and they do not support escapes. They are most commonly used in define or import to name the thing that you are defining or importing.

The legal characters that can appear in a symbol (or a call) are `0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@\\^_|~`

### Lists and Code objects
**Lists** and **Code** objects are also data, but you represent them differently in source code. To code a list, you would write
```
[ /*Expressions go here*/ ]
```
Lists are actually created at run-time. This allows you to put expressions inside of lists. For example, `[ 1 2 3 +]` would create a 2 item list containing the integers 1 and 6. The `+` would run before the list was created.

Code objects are similar to lists. You just wrap some code between a `{` and a `}` to create a code object. Code objects are formed at parsing time, which means that the expressions inside are not evaluated.

### Separating tokens
Tokens (data and calls) are seperated by whitespace. Any whitespace will work, including newline, spaces and tabs. Lots of times, you will not have to separate tokens by whitespace though. Here are the rules for when you have to add whitespace:

- You must have whitespace or another symbol between two integers, floats, or calls. `123"spam"456.6` is valid, but `spamham` is ambiguous. (Do we want to call spam and ham or spamham? Nustack would call spamham)
- You do not need to have whitespace between any two strings, symbols, or between brackets (`{}[]`) and surrounding tokens.

### Calls
**Calls** are how you do things. For example, adding two numbers is done by `1 2 +`. The `+` is a call. It pops two numbers (1 and 2), adds them, and pushes the result to the stack. Calls are also how variables are pushed onto the stack. For example, if x is set equal to "spam", running `x` will lookup the variable x and push it's value onto the stack.

---
And that's the whole story on Nustack's syntax! If you have any questions, please ask on Gitter or create an issue.
