#!/usr/bin/python3
"""
Module 3-print_reversed_list_integer
Affiche tous les entiers d'une liste dans l'ordre inverse.
"""

def print_reversed_list_integer(my_list=[]):
    """Affiche tous les entiers d'une liste dans l'ordre inverse."""
    for i in my_list[::-1]:
        print("{}".format(i))
