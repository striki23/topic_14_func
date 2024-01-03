# Функция прининимает два целых чисоа и возвращает их сумму и разность
def math_oper(a: int, b: int) -> int:
    s = a + b
    d = a - b
    return s, d


num1 = int(input('Введите первое целое число: '))
num2 = int(input('Введите второе целое число: '))
print(f'\nsumma = {(math_oper(num1, num2))[0]}'
      f'\ndifference = {(math_oper(num1, num2))[1]}')
