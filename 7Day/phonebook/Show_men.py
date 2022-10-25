import os
os.system('cls')
def show():
    with open('phonebook.txt','r') as ph:
        print(*ph)
