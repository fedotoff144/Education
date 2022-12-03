# Task 4

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def Binar(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b


n = int(input('Enter N: '))
print(Binar(n))