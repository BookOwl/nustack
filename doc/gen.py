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
        if v not in new:
            new[v] = (k,)
        else:
            new[v] = new[v] + (k,)
    return new

def clean(d):
    return invert(invert(d))

def gendoc(modname, filepath):
    mod = importlib.import_module(modname)

    mod_docs = {}
    mod_docs["modname"] = inspect.getdoc(mod)
    exports_docs = []
    for (name, export) in clean(mod.module.contents).items():
        export = export[0]
        export_doc = {
            "funcname":    ", ".join(name),
            "stackeffect": export.__annotations__.get("return", " none "),
            "description": inspect.getdoc(export),
        }
        exports_docs.append( functemplate % export_doc)

    mod_docs["exports"] = "".join(sorted(exports_docs))
    docs = basetemplate % mod_docs
    #print(docs)
    with open(filepath, "w") as f:
        f.write(docs)

if __name__ == '__main__':
    gendoc(*tuple(sys.argv[1:3]))
