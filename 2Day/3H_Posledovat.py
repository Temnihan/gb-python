# Задайте список из п чисел, заполненный по формуле (1 + 1/п) ** п и выведите на экран их сумму.
# Для п = 6: [2, 2,2, 2,2, 3] ->13"""

import os
os.system('cls')
n = input('enter number: ')
while not n.isdigit():
    n = input('try again')
n = int(n)
s = 0
for i in range(1,n+1):
    tmp = round((1 + 1/i)**i)
    print(tmp, end=', ')
    s+=tmp
print()
print(s)