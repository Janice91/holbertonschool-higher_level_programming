#!/usr/bin/python3
"""
Module 12-switch
Exemple de fonction switch-case simulée en Python.
"""

def switch(case_value):
    """Retourne un message selon la valeur donnée."""
    switcher = {
        0: "Zero",
        1: "One",
        2: "Two",
    }
    return switcher.get(case_value, "Unknown")
