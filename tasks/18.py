def lenght_sent(sentence: str) -> int:
    """
    Функция считает количество символов
    во входящей строке без учета пробелов

    :param sentence: исходный текст (предложение)
    :return: возвращает количество символов без учета пробелов
    """
    return len(''.join(sentence.split()))


print('Количество символов в предложении: ',
      lenght_sent(input('Введите предложение: ')))
print(lenght_sent.__doc__)
