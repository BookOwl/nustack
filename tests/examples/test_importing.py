from nustack.interpreter import Interpreter

import os.path
path = os.path.abspath("examples/importing/p1.nu")
expected = (
"""(p1) Starting p1...
(p1) Importing p2...
(p2) Starting p2
(p2) Importing Time
(p2) Defining `spam`
(p2) Done!
(p1) Imported p2
(p1) Calling p2::spam
spam1
spam2
(p1) Done!
"""
)

def test_importing(capsys):
    with open(path) as f:
        prog = f.read()
    interp = Interpreter()
    interp.run(prog, file=path)
    out, err = capsys.readouterr()
    print(out)
    assert out == expected
