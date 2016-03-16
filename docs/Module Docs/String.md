
# String - String utils and constants
Import with `std::String import
## Exported Functions:

### contains
`(s1 s2 -- b)`

Returns #t if the string s1 contains s2.
Do not use this for arbitary sequences, use Seq::contains instead.


### join
`(sequence s1 -- s2)`

Returns a new string formed by inserting s1 between every member of sequence.


### replace
`(s1 s2 s3 -- s4)`

Returns a new string obtained by replacing all instances of s2 in s1 with s3


### split
`(s1 s2 -- l)`

Splits s1 by s2


### to.bytes
`(string encoding -- bytes)`

Converts `string` to bytes using the encoding `encoding`


### to.string
`(bytes encoding -- string)`

Converts `bytes` to a string using the encoding `encoding`

#### Constant
```
lit_string: ('ascii_letters',) = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```
#### Constant
```
lit_string: ('ascii_lowercase',) = abcdefghijklmnopqrstuvwxyz
```
#### Constant
```
lit_string: ('ascii_uppercase',) = ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
#### Constant
```
lit_string: ('digits',) = 0123456789
```
#### Constant
```
lit_string: ('hexdigits',) = 0123456789abcdefABCDEF
```
#### Constant
```
lit_string: ('octdigits',) = 01234567
```
#### Constant
```
lit_string: ('printable',) = 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	

```
#### Constant
```
lit_string: ('punctuation',) = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```
#### Constant
```
lit_string: ('whitespace',) =  	

```

