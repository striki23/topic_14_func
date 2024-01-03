def printer(seq: list = ['python']) -> None:
    arg = input('Укажите аргумент(не обязательное поле):')
    if arg != '':
        seq = [arg]
    while True:
        word = input('Введите любое слово: ')
        if word == '':
            return seq
            break
        elif word in seq:
            return f'Строка {word} уже присутствует в списке на позиции {seq.index(word)}'
            break
        seq.append(word)


print(printer())
