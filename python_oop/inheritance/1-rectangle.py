#!/usr/bin/env python3
"""
Módulo 1-rectangle
Define una clase Rectangle que hereda de BaseGeometry.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo que hereda validaciones de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa un rectángulo validando ancho y alto con integer_validator.
        Args:
            width (int): El ancho del rectángulo.
            height (int): El alto del rectángulo.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
