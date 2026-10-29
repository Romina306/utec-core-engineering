#!/usr/bin/env python3
"""
Módulo 6-square
Define una clase Square con tamaño, posición,
área, impresión y representación __str__.
"""


class Square:
    """Representa un cuadrado con tamaño, posición
    y representación en cadena.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con size y position opcionales.
        Args:
            size (int): El tamaño del cuadrado.
            position (tuple): La posición del cuadrado.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Recupera el valor de position (getter)."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece el valor de position con validaciones (setter).
        Args:
            value (tuple): La nueva posición.
        Raises:
            TypeError: Si position no es una tupla de 2 enteros positivos.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2

    def __str__(self):
        """Devuelve la representación en cadena del cuadrado."""
        if self.__size == 0:
            return ""

        lines = []
        for _ in range(self.__position[1]):
            lines.append("")

        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)

    def my_print(self):
        """Imprime en stdout el cuadrado usando su representación __str__."""
        print(self)
