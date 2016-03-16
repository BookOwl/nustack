
# Requests - A nustack wrapper for the python requests module

Makes heavy use of the new (v0.10) attribute access. For example, to get the text of the webpage "http://example.com"
just run
```
`Requests import
"http://example.com" Requests::get
/* We now get the text attribute of the response object on top of the stack */
::text show
```
You can access every attribute and method of the [python requests Response object](http://docs.python-requests.org/en/master/api/#lower-level-classes) this way.
## Exported Functions:

### delete
`(url -- response_object)`

Returns a request object that represents a DELETE request to the given url


### encode.params
`(hash -- string)`

Encode the hash mqp `hash` as a query string suitable to concatenate to the end of an url


### get
`(url -- response_object)`

Returns a request object that represents a GET request to the given url


### head
`(url -- response_object)`

Returns a request object that represents a HEAD request to the given url


### options
`(url -- response_object)`

Returns a request object that represents a OPTIONS request to the given url


### post
`(url data -- response_object)`

Returns a request object that represents a POST request to the given url. `data` is a hash map.


### put
`(url data -- response_object)`

Returns a request object that represents a PUT request to the given url. `data` is a hash map.


