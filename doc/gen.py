#!python3
# Creates a markdown formated documentation file for a Nustack extension Module
import sys, inspect, importlib

# Documentation templates
basetemplate = """
# %(modname)s
## Exported Functions:
%(exports)s
"""
functemplate = """
### %(funcname)s
`%(stackeffect)s`

%(description)s

"""
def invert(d):
    new = {}
    for (k, v) in d.items():
        new[v] = k
    return new
def clean(d):
    return invert(invert(d))

modname, filepath = sys.argv[1:3]
mod = importlib.import_module(modname)

mod_docs = {}
mod_docs["modname"] = inspect.getdoc(mod)
exports_docs = []
for (name, export) in clean(mod.module.contents).items():
    export_doc = {
        "funcname":    name,
        "stackeffect": export.__annotations__.get("return", " none "),
        "description": inspect.getdoc(export),
    }
    exports_docs.append( functemplate % export_doc)

mod_docs["exports"] = "".join(sorted(exports_docs))
docs = basetemplate % mod_docs
#print(docs)
with open(filepath, "w") as f:
    f.write(docs)
