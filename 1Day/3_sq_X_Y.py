# Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).
sq = int(input('enter sq '))
if (sq == 1):
    print('x > 0,  y > 0')
elif (sq == 2):
    print(' x < 0, y > 0')
elif(sq == 3):
    print('x < 0, and y < 0')
elif (sq == 4):
    print(' x > 0 and y < 0')
else:
    print(' not correct')
