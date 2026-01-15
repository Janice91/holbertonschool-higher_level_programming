#!/usr/bin/python3
def pow(a, b):
    """Return a to the power of b."""
    if b < 0:
        return 1 / (a ** -b)
    return a ** b
