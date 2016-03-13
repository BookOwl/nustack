[![Build Status](https://travis-ci.org/BookOwl/nustack.svg?branch=tests)](https://travis-ci.org/BookOwl/nustack)
# What is this?
This is a collection of py.test style tests for Nustack. To run the tests, install py.test, cd to the project root dir and run `py.test`, or `py.test -v` for more details.

The goal is for nearly 100% test coverage. Currently, we have tests for
- The interpreter.Scope class
- The interpreter.Stack class
- The tokenizer
- The tokenize.Token class
- Many of the examples (argv.nu, factorial.nu, fizzbuzz.nu, and the multi-file importing example)
