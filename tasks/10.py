# Функция находит кубический корень введенного числа

def cubic_root(num: int) -> float:
    if num > 0:
        return round(num ** (1/3), 1)
    return 'Число должно быть положительным'


print(cubic_root(int(input('Введите положительное целое число: '))))
