#!/usr/bin/python3
"""
Module 8-multiple_returns
Retourne la taille d'une chaîne et son premier caractère.
"""

def multiple_returns(sentence):
    """Retourne la longueur de sentence et le premier caractère ou None."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
