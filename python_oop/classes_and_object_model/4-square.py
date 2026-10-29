#!/usr/bin/env python3
"""
Módulo 4-square
Define una clase Square con getters y setters para size.
"""


class Square:
    """Representa un cuadrado con tamaño privado,
    validaciones, área y propiedad size.
    """

    def __init__(self, size=0):
        """Inicializa un cuadrado.
        Args:
            size (int): El tamaño del cuadrado.
        """
        self.size = size

    @property
    def size(self):
        """Recupera el valor de size (getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el valor de size con validaciones (setter).
        Args:
            value (int): El nuevo tamaño.
        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2
