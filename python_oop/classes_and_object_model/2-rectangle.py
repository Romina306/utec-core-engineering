#!/usr/bin/env python3
"""
Módulo 2-rectangle
Define una clase Rectangle con atributos privados,
validaciones, área y perímetro.
"""


class Rectangle:
    """Representa un rectángulo con ancho, alto, área y perímetro."""

    def __init__(self, width=0, height=0):
        """Inicializa un rectángulo con width y height opcionales.
        Args:
            width (int): El ancho del rectángulo.
            height (int): El alto del rectángulo.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Recupera el valor de width (getter)."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el valor de width con validaciones (setter).
        Args:
            value (int): El nuevo ancho.
        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Recupera el valor de height (getter)."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el valor de height con validaciones (setter).
        Args:
            value (int): El nuevo alto.
        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula y devuelve el perímetro del rectángulo."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
