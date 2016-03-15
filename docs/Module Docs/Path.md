
# Path - Path, file, and directory operations
Import with `std::Path import

In this module, `path` always refers to a string that is a pathname.
## Exported Functions:

### abspath
`(path -- path)`

Returns the absolute version of path


### base.name
`(path -- path)`

Returns the base name of path


### change.dir
`(path -- )`

Changes the current working directory to path


### delete
`(path -- )`

Deletes the file given by path.


### dir.name
`(path -- path)`

Returns the directory name of path


### exists?
`(path -- bool)`

Returns #t if path exists.


### get.cwd
`( -- path)`

Returns the path of the current working directory


### glob
`(pattern -- list)`

Returns a list of file names that match the pattern `pattern`


### is.dir?
`(path -- bool)`

Returns #t if path is a directory


### is.file?
`(path -- bool)`

Returns #t if path is a file


### is.link?
`(path -- bool)`

Returns #t if path is a directory entry that is a symbolic link


### join
`(path1 path2 -- path3)`

Joins two strings together to make a new path


### list.dir
`(path -- list)`

Lists all the directories and files in a directory given by path


### make.dir
`(path -- )`

Creates the directory given by path


### make.dirs
`(path -- )`

Creates the directory given by path. Like make.dir, but makes all intermediate-level directories needed to contain the leaf directory


### remove.dir
`(path -- )`

Deletes the directory given by path as long as it is empty.


### size
`(path -- int)`

Returns the size of the file given by path in bytes


