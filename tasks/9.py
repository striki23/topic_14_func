import math


def circle_square(radius: float) -> float:
    # PI: float = 3.14
    return round(math.pi * radius ** 2, 2)
    # return round(PI * radius ** 2, 2)


print(circle_square(float(input('Введите радиус круга: '))))
#  функция принимает один аргумент radius и возвращает площадь круга
