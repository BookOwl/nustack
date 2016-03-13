from nustack.interpreter import Interpreter
from nustack.utils import StdinWrapper

expected = (
"""Enter a number ->5
factorial is
120
Enter a number ->7
factorial is
5040
Enter a number ->"""
)

def test_factorial(capsys):
    with open("examples/factorial.nu") as f:
        prog = f.read()
    interp = Interpreter()
    with StdinWrapper(["5", "7", ""]):
        try:
            interp.run(prog)
        except:
            pass
    out, err = capsys.readouterr()
    print(out)
    assert out == expected
