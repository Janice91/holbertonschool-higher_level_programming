#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class

    Args:
        obj: object to check
        a_class: class to compare with

    Returns:
        True if obj inherits from a_class (but not exactly a_class itself)
        False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
