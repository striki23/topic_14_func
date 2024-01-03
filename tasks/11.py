def calculate(a: int, b: int) -> int:
    if (comp := a * b) <= 1000:
        return comp
    return a + b


if __name__ == '__main__':
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    print(calculate(num_1, num_2))
    # функция принимает два целых числа и возвращает их произведение,
    # только если произведение <= 1000, иначе возвращает их сумму
