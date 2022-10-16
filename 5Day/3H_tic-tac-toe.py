# Создайте программу для игры в ""Крестики-нолики"".
import os, random
os.system('cls')

# Защита от дурака чтбы была только цифра
def isNumber(arr):

    n = (input('жду.. '))
    while not n.isdigit():
        n = (input('вводи правильно : '))
    n = int(n)
    # защита от выпада диапазона цифр
    if   n > 9 or n < 1:
        print(f'не менее 1 и не более 9')
        return isNumber(arr)
    # защита от повторения цифр
    if n not in arr:
        print('уже поставлен знак')
        return isNumber(arr)

    return n
# тоже самое только для робота
def isNumberRobot(arr):
    n = ""
    n = checkWin(2,0) #  если есть свои  2 то добавим 1
    if n == "":
        n = checkWin(0,2) # если есть 2 противника то мешаем
    if n == "":
        n = checkWin(1,0)
    if n == "":
        if type(field[4]) == int:
            n = 5
    if n == "":
        if type(field[0]) == int:
            n =1
    if n == "":
        n = int(random.randint(1,10))
    if n not in arr:
        return (isNumberRobot(arr))
    return n

# содережит ли своих 2 нолика
def checkWin(sum_O,sum_X):
    for line in victories:
        o = 0
        x = 0
        tmp = 0
        for i in range(0,3):
            if field[line[i]] == "O":
                o += 1
            elif field[line[i]] == "X":
                x += 1
            else: tmp = field[line[i]]

        if o == sum_O and x == sum_X:
            return tmp
    return ""


field = [i for i in range(1,10)] # заполнеие поле цифрами, для выбора клетки
 # проверка выиграл ли игрок

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def checkisWin1(mark_this):
    win = 'Нет победителя'
    for i in victories:
        if field[i[0]] == mark_this and field[i[1]] == mark_this  and field[i[2]] == mark_this:
            win = players[whose_move]
    return  win
player1 = input('what is you name player 1? ')
player2 = input('what is you name player 2? ')
players = [player1,player2]
countMove = random.randint(0, 1)
isRobot = (input('хочешь с роботом играть? нажми  "1" '))
if isRobot =="1":
    isRobot = True
else:
    isRobot =False



def showField(arr):  # заполнение поля
    print('_________')
    next_line = len(arr)**0.5 # это вдруг поле будет не 3 на 3 а больше
    for i in range(len(arr)):
        print(arr[i],end=' |')
        if i<=9:
            print(' ',end = '')
        if not (i+1) % next_line: # переход на след линию
            print()
    print('---------')
showField(field)

winner  = 'Нет победителя'
The_end = False
while not The_end:
    # проверка на выход из игры
    whose_move =countMove % len(players)

    if whose_move:
        mark ='O'
    else:
        mark = 'X'
    if isRobot: # если выбрали с роботом играть
        if whose_move: #  если ход  робота
            n = isNumberRobot(field)
            print(f' "р{players[whose_move]}" поставил "{mark}" на ячейку = {n}')
        else:
            print(f' "{players[whose_move]}" выбери клетку куда поставить крестик цифрами от 1 до 9: ')
            n = isNumber(field) # chreck number
    else:
        print(f' "{players[whose_move]}" выбери клетку куда поставить крестик цифрами от 1 до 9: ')
        n = isNumber(field) # chreck number
    field[n-1] = mark
    winner = checkisWin1(mark)
    showField(field)
    countMove += 1 # чередование 0 и 1 для следуещго игрока
    for i in field:
        if type(i) == int:
            The_end = False
            break
        else:
            The_end =True
    if winner !='Нет победителя':
        break
print(f'the winner is "{winner}"')
