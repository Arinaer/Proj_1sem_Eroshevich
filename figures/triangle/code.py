import math


def triangle_perimeter(a=7, b=2, c=8):
    p = a + b + c
    print('Периметр треугольника:', p)


def triangle_area(a=7, b=2, c=8):
    p = (a + b + c) * 0.5
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь треугольника:', s)
