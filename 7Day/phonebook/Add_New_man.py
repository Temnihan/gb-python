
def add_New():
    man = input('имя: ')
    telef = input('number: ')
    with open('phonebook.txt','a',encoding="utf-8") as ph:
        ph.write(man+' ')
        ph.write(telef+'\n')

