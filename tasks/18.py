def lenght_sent(sentence: str) -> int:
    """Функция считает количество символов
    во входящей строке без учета пробелов.

    :param sentence: Исходный текст (предложение).
    :return: Возвращает количество символов без учета пробелов.
    :rtype: int
    """
    return len(''.join(sentence.split()))


print('Количество символов в предложении: ',
      lenght_sent(input('Введите предложение: ')))
print(lenght_sent.__doc__)
