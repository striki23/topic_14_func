# Вводится положительное целое число. Программа складывает цифры этого числа

def sum_digits(num: str) -> int:
    return sum([int(i) for i in num])


print(sum_digits(input('Введите целое положительное число: ')))
