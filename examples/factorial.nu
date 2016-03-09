/* Factorial program */
{dup 1 eq {} {dup 1 - fact *} if} `fact def
{"Enter a number ->" input to.int dup fact swap show "factorial is" show show} forever
