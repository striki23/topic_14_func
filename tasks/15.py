def show_employee(name: str, salary) -> None:
    if salary == '':
        salary = 50000
    print(f'\nИмя: {name}\nЗарплата: {int(salary):,.0f}₽')


show_employee(input('Введите имя (обязательное поле): '),
              input('Укажите зарплату (необязательное поле): '))
