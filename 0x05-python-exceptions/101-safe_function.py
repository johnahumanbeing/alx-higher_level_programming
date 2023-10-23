#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    safe_x = 0
    try:
        safe_x = fct(*args)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        safe_x = None
        return safe_x
