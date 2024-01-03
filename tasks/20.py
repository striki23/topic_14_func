def printer(seq: str) -> None:
    if not seq:
        words: list[str, ...] = ['python']
    else:
        words: list[str, ...] = [seq]

    while word := input('Введите любое слово: '):
        if word in words:
            print(f'Строка {word} уже присутствует в '
                  f'списке на позиции {words.index(word)}')
            break
        words.append(word)
    else:
        print(words)


if __name__ == '__main__':
    arg = input('Укажите аргумент(не обязательное поле): ')
    printer(arg)

"""
Orange
kiwi
django
flask
python
django
"""
