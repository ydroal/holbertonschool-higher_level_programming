#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return (True)
    except ValueError:
        sys.stderr.write(
            'Exception: Unknown format code \'d\''
            ' for object of type \'str\'\n')
        return (False)
    except TypeError:
        sys.stderr.write(
            'Exception: unsupported format string passed to set.__format__\n')
        return (False)
