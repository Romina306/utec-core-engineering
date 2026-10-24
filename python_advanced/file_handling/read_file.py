#!/usr/bin/env python3
"""
Módulo para leer archivos de texto.
"""


def read_file(filename=""):
    """
    Función que lee un archivo de texto en UTF-8
    y lo imprime en la salida estándar (stdout).
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
