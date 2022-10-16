# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import  random

# Защита от дурака чтбы была только цифра
def isNumber(ostat):
    n = (input('жду.. '))
    while not n.isdigit():
        n = (input('вводи правильно : '))
    n = int(n)
    # защита от выпада диапазона цифр
    if   n > ostat or n < 1:
        print(f'не менее 1 и не более {ostat}')
        return isNumber(ostat)
    return n

# candy = 10 # колво конфте
candy = int(input('how myny candy?: '))
# ostatok = 3
ostatok = int(input('how many tryes?: '))
player1 = input('как тебя зовут 1? ')
player2 = input('как тебя зовту 2? ')
players = [player1,player2]
countMove = random.randint(0, 1) # счетчик кол во ходов и Жеребьевка
isRobot = (input('хочешь с роботом играть? нажми 1 '))
if isRobot =="1":
    isRobot = True
else:
    isRobot =False

while candy > 0:
    print(f' Всего {candy} конфет')
    if ostatok >candy:
        ostatok = candy
    if isRobot:
        if countMove % len(players) ==1:
            if candy <= ostatok:
                takes = candy
            else:
                takes = (candy) %(ostatok+1)
                if takes ==0:
                    takes = 1
            print(f' {player2} взял {takes} контфет ')
        else:
            print(f'{players[countMove % len(players)]} возьми  конфету от 1 до {ostatok} ')
            takes = isNumber(ostatok)  # сколько взял конфет
    else:
    # {players[countMove % len(players)]} - это для того чтобы чередовать игроков
        print(f'{players[countMove % len(players)]} возьми  конфету от 1 до {ostatok} ')
        takes = isNumber(ostatok)  # сколько взял конфет
    candy -=takes
    # print(candy)
    countMove += 1
print(f' The winner is {players[(countMove-1)%len(players)]}')