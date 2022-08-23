a = int(input('Введите, сколько км пробежал спортсмен в 1й день: '))
b = int(input('Введите требуемую дистанцию: '))
ran = a
day = 1
while ran < b:
    ran *= 1.1
    day += 1
print(day)