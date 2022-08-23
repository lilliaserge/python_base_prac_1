x = int(input('Введите целое положительное число: '))
max_num = 0
while x != 0:
    max_num = max(max_num, x % 10)
    x //= 10
print(max_num)