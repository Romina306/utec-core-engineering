#!/usr/bin/env python3
"""
Módulo 2-rectangle
Define una clase Rectangle que hereda de BaseGeometry,
implementa area y la representación __str__.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con área y representación __str__."""

    def __init__(self, width, height):
        """Inicializa un rectángulo validando ancho y alto.
        Args:
            width (int): Ancho del rectángulo.
            height (int): Alto del rectángulo.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la representación en cadena del rectángulo."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
