import math


def circle_perimeter(default_radius=5):
    p = 2 * math.pi * default_radius
    print('Длина окружности:', p)


def circle_area(default_radius=5):
    s = math.pi * default_radius ** 2
    print('Площадь окружности:', s)
