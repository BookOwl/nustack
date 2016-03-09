#!python3
# Nustack main entry point

import nustack
from nustack import utils
import sys, imp, os, argparse

desc = "Nustack is a stack-oriented concatenative programming language with support\
 for high-level modular programming and Python integration."
epilog = "For more information, please see https://github.com/BookOwl/nustack"
parser = argparse.ArgumentParser(prog="nustack",
                                 description=desc,
                                 epilog=epilog,
                                )
parser.add_argument("-d", "--debug", action="store_true", help="Turn on debug messages (default: False)")
parser.add_argument("sourcefile", nargs="?", help="Source file to run, or run the interactive prompt if ommited")
parser.add_argument("rest", nargs=argparse.REMAINDER, help="Arguments that will be passed to the nustack program.")
args = parser.parse_args()
utils.config_logging(on=args.debug)

def main():
    if args.sourcefile:
        # Run code from a file
        fname = args.sourcefile
        with open(fname) as f:
            code = f.read()
        interp = nustack.interpreter.Interpreter(args.rest)
        try:
            interp.run(code, file=fname)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print("--ERROR--")
            print("%s - %s" % (e.__class__.__name__, str(e)))
            if input("Raise error? (y/n) ") in "yY":
                raise
    else:
        # import readline on *nix
        try:
            import readline
        except (ImportError, TypeError):
            pass
        print("Nustack v%s Interactive Prompt" % nustack.version)
        print("Running on Python %s" % sys.version)
        print("Enter your EOF character to exit.")
        print("Press Ctrl-C to stop any running code and go back to the prompt.")
        interp = nustack.interpreter.Interpreter()
        while True:
            try:
                code = input(">>> ")
                if code == "reload":
                    imp.reload(nustack.interpreter)
                    imp.reload(nustack.stdlib.builtins)
                    interp = nustack.interpreter.Interpreter()
                else:
                    try:
                        interp.eval(code)
                    except KeyboardInterrupt:
                        pass
            except EOFError:
                break
            except Exception as e:
                print("--ERROR--")
                print("%s - %s" % (e.__class__.__name__, str(e)))
                if input("Raise error? (y/n) ") in "yY":
                    raise

if __name__ == '__main__':
    main()
