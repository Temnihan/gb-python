# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import os
os.system('cls')
n = input('enter number: ')
while not n.isdigit():
    n = input('try again')
n = int(n)
s = 1
for i in range(1,n+1):
    print(i*s,end = ', ')
    s*=i
