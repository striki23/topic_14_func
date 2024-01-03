def math_oper(a: int, b: int) -> tuple[int, int]:
    return a + b, a - b


if __name__ == '__main__':
    # Функция прининимает два целых чисоа и возвращает их сумму и разность
    num1 = int(input('Введите первое целое число: '))
    num2 = int(input('Введите второе целое число: '))
    summa, difference = math_oper(num1, num2)

    print(f'{summa = }\n{difference = }')
