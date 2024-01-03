def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    # Функция проверяет является ли введенное число простым
    num: int = int(input('Введите положительно целое число: '))
    if num in (0, 1):
        print('0 и 1 не простые числа')
    elif num < 0:
        print('Отрицателдьные числа не могут быть простыми')
    else:
        print(is_prime(num))
