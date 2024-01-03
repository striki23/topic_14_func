def external(a: int, b: int) -> int:
    def inner() -> int:
        total = a + b
        return total

    return inner() + 10


if __name__ == '__main__':
    print(external(
        int(input('Введите первое число: ')),
        int(input('Введите второе число: '))
    ))
