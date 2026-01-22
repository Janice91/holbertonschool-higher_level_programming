#!/usr/bin/python3
"""
Module 0-print_list_integer
Ce module contient une fonction qui affiche tous les entiers d'une liste.
"""


def print_list_integer(my_list=[]):
    """
    Affiche tous les entiers d'une liste, un par ligne, en utilisant str.format().
    """
    for i in my_list:
        print("{}".format(i))
