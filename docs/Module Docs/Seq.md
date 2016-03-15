
# Seq - Sequence operations
Import with `std::Seq import
## Exported Functions:

### append
`(sequence a -- sequence)`

Appends a datum to a sequence


### butfirst
`(sequence -- a)`

None


### contains
`(sequence a -- b)`

Returns #t if the sequence contains a.
Do not use this for string, use String::contains instead.


### first
`(sequence -- a)`

None


### length, len
`(sequence -- i)`

Return the length of a sequence


### nth
`(sequence n -- a)`

Returns the nth item of a sequence (eg. list or string)


### pack.n
`(... i -- l)`

Creates a list from the top i items on the stack not including i


### pack2
`(a1 a2 -- [a1 a2])`

Creates a list from the top 2 items on the stack


### pack3
`(a1 a2 a3 -- [a1 a2 a3])`

Creates a list from the top 3 items on the stack


### pop
`(sequence --  a)`

Pops an item from the end of a sequence


### range
`(n n -- l)`

None


### range.step
`(n n -- l)`

None


### repeat
`(sequence1 i -- sequence2)`

Repeats sequence1 i times


### reverse
`(sequence1 -- sequence2)`

Reverses a sequence


### set.nth
`(sequence a n -- sequence)`

None


### slice
`(sequence1 n1 n2 -- sequence2)`

Slices a seuence from n1 to n2


### unpack
`(sequence -- a...)`

Unpacks a sequence


