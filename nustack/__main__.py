#!python3
# Nustack main entry point

import nustack
import sys, imp, os

helptext = """Usage:
python -m nustack
Start the interactive prompt

python -m nustack -h | --help | help
Displays this help message

python -m nustack path
Runs the code in the file "path" """

def main():
    if "-h" in sys.argv or "help" in sys.argv or "--help" in sys.argv:
        print(helptext, end="")
        sys.exit(1)
    elif len(sys.argv) >= 2:
        # Run code from a file
        fname = sys.argv[1]
        with open(fname) as f:
            code = f.read()
        interp = nustack.interpreter.Interpreter(sys.argv[1:])
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
