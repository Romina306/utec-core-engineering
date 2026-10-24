#!/usr/bin/env python3
"""
Módulo para añadir texto al final de archivos.
"""


def append_write(filename="", text=""):
    """
    Añade una cadena al final de un archivo de texto (UTF-8)
    y devuelve el número de caracteres añadidos.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
