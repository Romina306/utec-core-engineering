#!/usr/bin/python3
number = __import__('random').randint(-10, 10)

if number > 0:
    print(f"{number} es positivo")
elif number == 0:
    print(f"{number} es cero")
else:
    print(f"{number} es negativo")