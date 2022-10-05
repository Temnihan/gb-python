# Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from operator import index
import os
os.system('cls')
l = (1,3,5,64,3)
my_sum = 0
for i in range(1,len(l),2):
    print(l[i])
    my_sum += l[i]
print(my_sum)