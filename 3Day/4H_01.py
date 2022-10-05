# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import os
import re
os.system('cls')
num = input(' enter number: ')
while not num.isdigit():
    num = input('try again: ')
num = int(num)

res = []
while num > 0:
    # print(num % 2, end='')
    res.append(num % 2)
    num //=2

for i in range(-1,-len(res)-1, -1):
    print(res[i],end= '')

print()
