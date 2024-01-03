#  функция принимает один аргумент radius и возвращает площадь круга
import math


def circle_square(radius: float) -> float:
    return round(math.pi * radius**2, 2)


print(circle_square(float(input('Введите радиус круга: '))))
