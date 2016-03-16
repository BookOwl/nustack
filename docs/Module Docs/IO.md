
# IO - basic file IO
Import with `std::IO import
## Exported Functions:

### close
`(file -- )`

Takes a file object and closes it. Returns nothing


### open
`(s s -- file)`

Pops a string naming a file path and a string used as open flags, returns a file object


### read.n
`(file i -- s file)`

Takes a file object and an integer i, reads i charactors or bytes from it as a string, and returns that string and the original file object


### readall
`(file -- s file)`

Takes a file object, reads everything from it as a string, and returns that string and the original file object


### write
`(file s -- file)`

Takes a file object and a string, writes that string to the file, and returns the file


