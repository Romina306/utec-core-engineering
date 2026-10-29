#!/usr/init/env python3  # noqa: E265
#!/usr/bin/env python3
"""
Módulo base_geometry
Define la clase BaseGeometry con el método area y integer_validator.
"""


class BaseGeometry:
    """Representa una clase base para la geometría."""

    def area(self):
        """Lanza una excepción indicando que no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero positivo mayor que 0.
        Args:
            name (str): Nombre del parámetro.
            value (int): Valor a validar.
        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor o igual a 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

