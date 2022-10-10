# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
smpl = int(input(' enter n: '))
def simplePown(n, m = 2):
    if n == 1:
        return 1
    elif(not n % m):
        print(f'{m} ',end=' ')
        return  simplePown(n//m)
    else:
        return simplePown(n, m+1)
simplePown(smpl)