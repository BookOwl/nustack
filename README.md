[![Join the chat at https://gitter.im/BookOwl/nustack](https://badges.gitter.im/BookOwl/nustack.svg)](https://gitter.im/BookOwl/nustack?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# Nustack
Nustack is a stack-oriented concatenative programming language with support for high-level modular programming and Python integration.
For an excellent introduction to concatenative programming, please see http://evincarofautumn.blogspot.com/2012/02/why-concatenative-programming-matters.html?m=1

## Installing.
Installing Nustack is easy. ~~Just run `pip install nustack` at a command prompt.~~ The version on Pypi is broken. To install, clone this repository and put the contents in a folder called nustack that is on your module search path.

Nustak is compatible with Python 3.
## Running
To run a Nustack program, just run the following command line: `python -m nustack path/to/program.nu`

`python -m nustack` starts the Nustack interactive prompt.

## Help
Currently, there is little documentation for Nustack, but I am working on it. For now, create an issue with your questions, ask on gitter, or post them in the [Nustack Scratch forum topic](https://scratch.mit.edu/discuss/topic/184118/)
## Example
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
