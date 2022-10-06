# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibon(n):
    if n in (1, 2):
        return 1
    return fibon(n -1) +fibon(n - 2)
num = int(input())
# fibon(num)
fib = []
for i in range(1,num+1):
    # print(fibon(i), end = ' ')
    fib.append(fibon(i))
print(fib)
nefib = []

def nefibon(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nefibon(n-2) -nefibon(n-1)

for i in range(num+1):
    fib.insert(0,nefibon(i))
    # nefib.append(nefibon(i))
# print(nefib)
print(fib)