#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase using only one loop and str.format()"""
    result = "".join(
        chr(ord(c) - 32) if "a" <= c <= "z" else c
        for c in str
    )
    print("{}".format(result))
