# функция принимает два целых числа и возвращает их произведение,
# только если произведение <= 1000, иначе возвращает их сумму

def calculate(a: int, b: int) -> int:
    if (comp := a * b) <= 1000:
        return comp
    else:
        return a + b


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print(calculate(num1, num2))
