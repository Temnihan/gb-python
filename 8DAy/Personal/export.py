
def export1(name):
    ph =open('phonebook.txt','r')
    with open(name,'w') as newph:
        for line in ph:
            newph.writelines(line)
    ph.close()

def export2(name):
    ph =open('phonebook.txt','r')
    with open(name,'w') as newph:
        for line in ph:
            nline = line.split(',')
            for i in (nline):
                newph.writelines(i+'\n')
            # newph.writelines(line)
    ph.close()
def create_head(data):
    with open(data,'w', encoding= 'utf-8') as fl:
        fl.write('Фамилия,Имя,Дожность,Статус \n')

def export_csv(name):
    ph = open('phonebook.txt','r')
    with open(name,'a') as newph:
        create_head(name)
        for line in ph:
            newph.writelines(line)
    ph.close()
