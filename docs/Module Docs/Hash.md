
# Hash - Hash table creation and operations
Import with `std::Hash import
## Exported Functions:

### del
`(hash key -- hash)`

Deletes the value asociated with the key in the hash


### empty
`( -- hash)`

Creates an empty hash table


### from.list
`(list -- hash)`

Creates a hash from a list of [key value] lists


### get
`(hash key -- value)`

Retrieves the value asociated with the key in the hash


### items
`(hash -- list)`

Returns a list of [key value] lists taken from the hash


### set
`(hash key value -- hash)`

Sets the value asociated with the key in the hash


