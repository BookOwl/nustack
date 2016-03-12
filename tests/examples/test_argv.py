from nustack.interpreter import Interpreter
from nustack.utils import StdinWrapper

expected = (
"""Arguments:
['-a', '-b', '--spam']
"""
)

def test_argv(capsys):
    with open("examples/argv.nu") as f:
        prog = f.read()
    interp = Interpreter(argv=["-a", "-b", "--spam"])
    interp.run(prog)
    out, err = capsys.readouterr()
    print(out)
    assert out == expected
