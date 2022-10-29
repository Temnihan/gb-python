import os
os.system('cls')
def show():
    with open('phonebook.txt','r',encoding='utf-8') as ph:
        for line in ph:
            print(line,end='')


def find_empl(name):
    res = []
    with open('phonebook.txt', 'r', encoding='utf-8') as ph:
        for line in ph:
            word = line.rstrip().split(',')
            for item in word:
                if name == item:
                    res.append(line.strip())
    print('-'*10)
    print('\n'.join(res))
    print('-'*10)



