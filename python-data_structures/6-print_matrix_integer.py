#!/usr/bin/python3
"""
Module 6-print_matrix_integer
Affiche une matrice d'entiers.
"""

def print_matrix_integer(matrix=[[]]):
    """Affiche la matrice d'entiers."""
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))
