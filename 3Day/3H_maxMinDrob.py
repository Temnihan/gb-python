# Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
l = [1.1, 1.2, 3.1, 5, 10.01]
print(type(l[3]))
mx =l[0]%1
mn= l[0]%1
for i in range(1,len(l)):
    if (type(l[i]) != int):
        print('es')
        if (l[i]%1> mx):
            mx = l[i]%1
        if (l[i]%1 <mn):
            mn = l[i]%1
res = round(mx-mn,3)
print(f' mx -mn = {res}')
