# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
l = [2, 3, 4, 5, 6]
k = -1
for i in range((len(l)+1)//2):
    print(l[i]*l[k])
    k-=1