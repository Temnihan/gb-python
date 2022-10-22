from random import randint
from functools import reduce
sumrez= 0
# for i in range(randint(4,10)):
#     masobr.append(randint(0,10))
masobr = [randint(0, 10) for i in range(randint(4, 10))]

sumrez = [sumrez + masobr[i] for i in range(1,len(masobr),2) ]
# for i in range(1,len(masobr),2):
#     sumrez+=masobr[i]
sumrez = reduce(lambda a,b: a + b, [masobr[i] for i in range(1,len(masobr),2)])

print(masobr,"->",sumrez)

