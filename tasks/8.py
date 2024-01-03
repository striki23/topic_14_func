# Функция принимает трехзначное положительное число,
# вычисляет a + ab + abc и возвращает результат

def sum_digits(num: str) -> int:
    a, b, c = list(num)
    return int(a) + int(a+b) + int(a + b + c)


print(sum_digits(input('Введите трехзначное положительное число: ')))
