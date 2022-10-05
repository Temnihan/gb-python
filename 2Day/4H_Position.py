# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
import os
os.system('cls')
n = input('enter number: ')
while not n.isdigit():
    n = input('try again')
n = int(n)
res = []
res.append(0)
for i in range(-n,n+1):
    res.append(i)
print(res)
s = 1

path = 'file.txt'
data = open(path, 'r')
for line in data:
    line = line.rstrip('\n')
    if line.isdigit():
        line = int(line)
        s*= res[line]

data.close()
print(s)
