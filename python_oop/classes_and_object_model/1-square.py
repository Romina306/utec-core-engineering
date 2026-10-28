#!/usr/bin/env python3
"""
Módulo 1-square
Define una clase Square con un atributo de instancia privado size.
"""


class Square:
    """Representa un cuadrado con un tamaño privado."""

    def __init__(self, size):
        """Inicializa un cuadrado con un tamaño dado.

        Args:
            size (int): El tamaño del cuadrado.
        """
        self.__size = size
