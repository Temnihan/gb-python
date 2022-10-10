# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
fl2 = []
# считываем первую функцию
with open('file.txt','r') as data:
    for line in data: # read line  of text
        tmp = line.split()  # spread one line
        s = len(tmp) # count how many членов с плюсам
        fl1 = [] # здесь будет хрантяся числа функции, по индексу определим степень числа х
        for i in range(len(tmp)-1,-1,-2): # итерация входной функции с конца через 1 чтбы без плюсов
            tmpi = line.split()[i] # цифры с  хх и ** до пробела вобщем
            isnum = ''    # что не цифра
            for j in tmpi:          # every symbol
                if j.isdigit():
                    isnum += j
                else:
                    break
            fl1.append(int(isnum))
fl1.reverse() # чтобы проще складывать с другой функцие
print(fl1)
with open('file2.txt','r') as data:
    for line in data: # read line  of text
        tmp = line.split()  # spread one line
        s = len(tmp) # count how many членов с плюсам
        fl2 = [] # здесь будет хрантяся числа функции, по индексу определим степень числа х
        for i in range(len(tmp)-1,-1,-2): # итерация входной функции с конца через 1 чтбы без плюсов
            tmpi = line.split()[i] # цифры с  хх и ** до пробела вобщем
            isnum = ''    # что не цифра
            for j in tmpi:          # every symbol
                if j.isdigit():
                    isnum += j
                else:
                    break
            fl2.append(int(isnum))

fl2.reverse() # чтобы проще складывать с другой функцие
print(fl2)
itog = []
for i in range(max(len(fl1),len((fl2)))):
    tmpf1 = 0
    tmpf2 = 0
    if i < len(fl1):
        tmpf1 = fl1[i]
    if i < len(fl2):
        tmpf2 = fl2[i]
    itog.append(tmpf1+tmpf2)
print(itog)