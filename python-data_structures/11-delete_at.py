#!/usr/bin/python3
"""
Module 11-delete_at
Supprime l’élément à un index spécifique dans une liste.
"""

def delete_at(my_list=[], idx=0):
    """Supprime l’élément à l’index idx si valide."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx + 1:]
