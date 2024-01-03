def sum_nums(num1: int, num2: int) -> int:
    return num1 + num2


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

my_func = sum_nums
print('\nРезультат первой функции:', sum_nums(a, b))
print('Результат функции с новым именем:', my_func(a, b))

# почему функция должна возвращать None?