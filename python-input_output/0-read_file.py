#!/usr/bin/python3
"""Module pour lire un fichier texte"""


def read_file(filename=""):
    """
    Lit un fichier texte (UTF-8) et l'affiche sur stdout
    
    Args:
        filename: Le nom du fichier à lire (par défaut "")
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
