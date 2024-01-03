
def external(a: int, b: int) -> int:
    def inner() -> int:
        total = a + b
        return total
    return inner() + 10


print(external(int(input('Введите первое число: ')),
      int(input('Введите второе число: '))))
