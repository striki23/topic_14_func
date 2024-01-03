def sum_nums(num1: int, num2: int) -> None:
    print(num1 + num2)


if __name__ == '__main__':
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))

    my_func = sum_nums
    print('\nРезультат первой функции:', end=' ')
    sum_nums(a, b)

    print('Результат функции с новым именем:', end=' ')
    my_func(a, b)
