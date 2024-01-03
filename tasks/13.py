def output(*args: tuple) -> None:
    if not args:
        print('Ошибка: Введите что-нибудь ...')
    else:
        print(*args, sep='\n')


if __name__ == '__main__':
    # Функция принимает аргументы переменной длины и выводит их значение
    output(*input('Введите аргументы через пробел: ').split())
