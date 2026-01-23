#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square of all integers in a matrix."""
    new_matrix = []
    for row in matrix:
        new_row = [val ** 2 for val in row]
        new_matrix.append(new_row)
    return new_matrix
