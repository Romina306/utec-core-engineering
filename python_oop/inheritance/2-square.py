#!/usr/bin/env python3
"""
Módulo 2-square
Define una clase Square que hereda de Rectangle
y sobreescribe __str__.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado que hereda de Rectangle
    con su propia representación __str__.
    """

    def __init__(self, size):
        """Inicializa un cuadrado validando su tamaño.
        Args:
            size (int): El tamaño del cuadrado.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Devuelve la representación en cadena del cuadrado."""
        return "[Square] {}/{}".format(self.__size, self.__size)
