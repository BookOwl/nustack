
# Shell support.
## Exported Functions:

### encoding
`( -- s)`

Returns the character encoding of the shell


### run
`(s1 -- l)`

Runs s1 as a shell command string and returns a two item list [return-code output]
Note that this run using the subprocess module with shell=False,
so if you need to use a built in shell command use run.shell


### run.shell
`(s1 -- l)`

Runs s1 as a shell command string and returns a two item list [return-code output]
Note that this run using the subprocess module with shell=True, which can be a security risk!


