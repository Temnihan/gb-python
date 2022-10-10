# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randrange
st = int(input(' stepen: '))
with open('file2.txt','a') as data:

    while st != 0:
        k = randrange(4)
        if k !=0:
            data.write(f' {k}x**{st} + ')
            print(f' {k}x**{st} + ', end= '')
        st -= 1
    data.write(str(randrange(101))+'\n')
print(randrange(101))
