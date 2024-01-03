# Функция проверяет является ли введенное число простым

def is_prime(num: int) -> bool:
    if num in (0, 1):
        return '0 и 1 не простые числа'
    elif num < 0:
        return 'Отрицателдьные числа не могут быть простыми'
    else:
        for i in range(2, num):
            if num % 2 == 0:
                return False
                break
            return True


print(is_prime(int(input('Введите положительно целое число: '))))
