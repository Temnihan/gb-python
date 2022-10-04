# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример
# - 6782 -> 23
# - 0,56 -> 11
import os
os.system('cls')


def sumelements(num):
    checkinput = True
    try:
        n = float(num)
        return n
    except ValueError:
        print('Try again: ')
    while checkinput:
        try:
            n1 = float(input(' enter n: '))
            checkinput = False
        except ValueError:
            print('Try again: ')
    return n1


n = input('enter n: ')
res = str(sumelements(n))
sum = 0
for i in res:
    if i !='.':
        sum += int(i)
print(sum)
