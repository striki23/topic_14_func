from typing import Callable


def sum_digits(num: int) -> int:
    num: str = str(num)

    a, b, c = list(num)
    return int(a) + int(a + b) + int(a + b + c)


def sum_digits_2(num: int) -> int:
    first: int = num // 100
    second: int = num // 10

    return first + second + num


sum_digits_3: Callable = lambda x: x // 100 + x // 10 + x


print(sum_digits(int(input('Введите трехзначное положительное число: '))))
print(sum_digits_2(int(input('Введите трехзначное положительное число: '))))
print(sum_digits_3(int(input('Введите трехзначное положительное число: '))))
# Функция принимает трехзначное положительное число,
# вычисляет a + ab + abc и возвращает результат
