def show_employee(name: str, salary: int = 50_000) -> None:
    print(f'\nИмя: {name}'
          f'\nЗарплата: {int(salary):,.0f}₽')


if __name__ == '__main__':
    name: str = input('Введите имя (обязательное поле): ')
    salary: str = input('Укажите зарплату (необязательное поле): ')

    if not salary:
        show_employee(name)
    else:
        show_employee(name, int(salary))
