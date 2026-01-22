#!/usr/bin/python3
"""
Module 9-max_integer
Retourne le plus grand entier d'une liste.
"""

def max_integer(my_list=[]):
    """Retourne le plus grand entier dans la liste, ou None si vide."""
    if not my_list:
        return None
    max_val = my_list[0]
    for i in my_list:
        if i > max_val:
            max_val = i
    return max_val
