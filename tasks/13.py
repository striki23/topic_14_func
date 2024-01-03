#  Функция принимает аргументы переменной длины и выводит их значение

def output(*args: tuple) -> any:
    if not args:
        print('Ошибка: Введите что-нибудь ...')
    else:
        for arg in args:
            print(arg)


output(*input('Введите аргументы через пробел: ').split())
