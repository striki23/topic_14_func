def cubic_root(num: int) -> float:
    if num < 0:
        raise ValueError('Число должно быть положительным')
    return round(num ** (1 / 3), 1)


print(cubic_root(int(input('Введите положительное целое число: '))))
# Функция находит кубический корень введенного числа
