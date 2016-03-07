#!python3
"""Requests - A nustack wrapper for the python requests module

Makes heavy use of the new (v0.10) attribute access. For example, to get the text of the webpage "http://example.com"
just run
```
`Requests import
"http://example.com" Requests::get
/* We now get the text attribute of the response object on top of the stack */
::text show
```
You can access every attribute and method of the [python requests Response object](http://docs.python-requests.org/en/master/api/#lower-level-classes) this way.
"""

from nustack.extensionbase import Module, Token
module = Module("std::Requests")

import requests
import urllib.parse

def wrap_req(req):
    return Token("request_obj", req)

@module.register("get")
def get(env) -> "(url -- response_object)":
    "Returns a request object that represents a GET request to the given url"
    url = env.stack.pop().val
    req = wrap_req(requests.get(url))
    env.stack.push(req)

@module.register("head")
def get(env) -> "(url -- response_object)":
    "Returns a request object that represents a HEAD request to the given url"
    url = env.stack.pop().val
    req = wrap_req(requests.head(url))
    env.stack.push(req)

@module.register("head")
def get(env) -> "(url -- response_object)":
    "Returns a request object that represents a HEAD request to the given url"
    url = env.stack.pop().val
    req = wrap_req(requests.head(url))
    env.stack.push(req)

@module.register("delete")
def get(env) -> "(url -- response_object)":
    "Returns a request object that represents a DELETE request to the given url"
    url = env.stack.pop().val
    req = wrap_req(requests.delet(url))
    env.stack.push(req)

@module.register("options")
def get(env) -> "(url -- response_object)":
    "Returns a request object that represents a OPTIONS request to the given url"
    url = env.stack.pop().val
    req = wrap_req(requests.options(url))
    env.stack.push(req)

@module.register("post")
def get(env) -> "(url data -- response_object)":
    "Returns a request object that represents a POST request to the given url. `data` is a hash map."
    url, data = env.stack.popN(2)
    url = url.val
    data = {k.val: v.val for (k,v) in data.val.items()}
    req = wrap_req(requests.post(url, data=data))
    env.stack.push(req)

@module.register("put")
def get(env) -> "(url data -- response_object)":
    "Returns a request object that represents a PUT request to the given url. `data` is a hash map."
    url, data = env.stack.popN(2)
    url = url.val
    data = {k.val:  v.val for (k,v) in data.val.items()}
    req = wrap_req(requests.put(url, data=data))
    env.stack.push(req)

@module.register("encode.params")
def enc_params(env) -> "(hash -- string)":
    "Encode the hash mqp `hash` as a query string suitable to concatenate to the end of an url"
    params = env.stack.pop().val
    params = {k.val: v.val for (k,v) in params.val.items()}
    env.stack.push(Token("lit_string", urllib.parse.urlencode(params)))
