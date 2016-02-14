# Nustack

[![Join the chat at https://gitter.im/BookOwl/nustack](https://badges.gitter.im/BookOwl/nustack.svg)](https://gitter.im/BookOwl/nustack?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Nustack is a stack-oriented concatenative programming language with support for high-level modular programming and Python integration.

## Installing.
Installing Nustack is easy. Just download this repository to your computer as a zip, extract the contents of the nustack-master folder to a folder called nustack that is on the module search path.

Nustak is compatable with Python 3.
## Running
To run a Nustack program, just run the following command line: `python -m nustack path/to/program.nu`

`python -m nustack` starts the Nustack interactive prompt.
## Help
Currently, there is no documentation for Nustack, but once I finish implementing the built-in functions, I create the documentation in the wiki. For now, create an issue with your questions.
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
