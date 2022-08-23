income = int(input('Введите прибыль: '))
outgoing = int(input('Введите издержки: '))
print('Финансовый результат:')
if income > outgoing:
    print('прибыль')
elif income == outgoing:
    print('вышла в ноль')
else:
    print('убыток')