#!/usr/bin/env python3
"""
Módulo 2-square
Define una clase Square con validaciones para el atributo privado size.
"""


class Square:
    """Representa un cuadrado con tamaño validado y privado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con tamaño opcional y validaciones.
        
        Args:
            size (int): El tamaño del cuadrado (por defecto 0).
        
        Raises:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
