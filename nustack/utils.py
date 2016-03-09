import sys

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
