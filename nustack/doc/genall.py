#!python3
import os, glob, sys
import nustack
import gen

exportdir = sys.argv[1]

# Get module names
path = os.path.join(nustack.__path__[0], "stdlib")
print("Path to standard library:", path)
#os.chdir(path)
modnames = (os.path.basename(f)[:-3] for f in glob.iglob(os.path.join(path, "*.py")) if '__init__' not in f)

for mod in modnames:
    print("Generating docs for %s..." % mod)
    gen.gendoc("nustack.stdlib.%s" % mod, os.path.join(exportdir, mod + ".md"))
print("Done!")
