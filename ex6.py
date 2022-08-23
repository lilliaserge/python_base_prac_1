income = int(input('Введите прибыль: '))
outgoing = int(input('Введите издержки: '))
print('Финансовый результат:')
if income > outgoing:
    efficiency = 1 - outgoing / income
    print('прибыль')
    print(f'Рентабельность = {efficiency}')
    staff = int(input('Введите количество сотрудников: '))
    profit_per_worker = (income - outgoing) / staff
    print(f'Прибыль на сотрудника = {profit_per_worker}')
elif income == outgoing:
    print('вышла в ноль')
else:
    print('убыток')