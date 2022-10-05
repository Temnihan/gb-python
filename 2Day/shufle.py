# реалезуйте алгоритм перемешивание
from operator import le
from random import random, shuffle, sample
import os
os.system('cls')
array1 = [i for i in range(10)]
print(array1)
array3 = sample(array1,len(array1))
# array2 = shuffle(array1)
print(array1)
