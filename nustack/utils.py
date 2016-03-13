import sys, io

def config_logging(on=False, file=sys.stderr):
    global log_config
    log_config = {
                  "on": on,
                  "file": file,
                  }
config_logging()

def log(*args, **kwargs):
    if log_config["on"]:
        print("DEBUG LOG:", *args, file=log_config["file"], **kwargs)

class StdoutCapture:
    def __init__(self):
        self.orig = sys.stdout
    def __enter__(self):
        self._out = io.StringIO()
        sys.stdout = self._out
        return self
    def __exit__(self, type, val, trace):
        sys.stdout = self.orig
        return False
    def getvalue(self):
        return self._out.getvalue()

class StderrCapture:
    def __init__(self):
        self.orig = sys.stderr
    def __enter__(self):
        self._out = io.StringIO()
        sys.stderr = self._out
        return self
    def __exit__(self, type, val, trace):
        sys.stderr = self.orig
        return False
    def getvalue(self):
        return self._out.getvalue()

class StdinWrapper:
    def __init__(self, lines):
        self.lines = iter(lines)
        self.orig = sys.stdin
    def __enter__(self):
        sys.stdin = self
    def __exit__(self, type, val, trace):
        sys.stdin = self.orig
        return False
    def readline(self):
        return next(self.lines)
    def read(self, size=None):
        txt, rest = "\n".join(self.lines), ""
        if size:
            txt, rest = txt[:size], txt[size:]
        self.lines = (line for line in rest.split("\n") if line)
        return txt
