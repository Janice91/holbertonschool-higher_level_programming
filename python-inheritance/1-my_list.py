#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list
"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
