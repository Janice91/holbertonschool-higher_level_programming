#!/usr/bin/python3
"""
Module 10-divisible_by_2
Indique si un nombre est divisible par 2.
"""

def divisible_by_2(my_list=[]):
    """Retourne une liste de True/False pour divisibilité par 2."""
    return [i % 2 == 0 for i in my_list]
