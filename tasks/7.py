def sum_digits(num: int) -> int:
    num: str = str(num)
    return sum([int(i) for i in num])


def sum_digits_2(num: int) -> int:
    total_sum: int = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    return total_sum


# print(sum_digits(int(input('Введите целое положительное число: '))))
# print(sum_digits_2(int(input('Введите целое положительное число: '))))
# Вводится положительное целое число. Программа складывает цифры этого числа


# def say_hello():
#     print('Hello, World')
#     return  # return None
#
#
# print(say_hello())
