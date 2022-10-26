
def add_New(sn ,name,t,d, sep = ','):

    with open('phonebook.txt','a',encoding="utf-8") as ph:
        ph.write(sn + sep)
        ph.write(name+sep)
        ph.write(t+sep)
        ph.write(d+'\n')
def import_file(fl ):
    with open(fl,'r') as data:
        for line in data:
            tmp = line.split()
            print(f' tmp type = {type(tmp)}')
            if len(tmp)>1: # это если в строчке все данные
                add_New(tmp[0],tmp[1],tmp[2],tmp[3])
            elif len(tmp) ==1: # это если каждой сточки разные данные
                add_New(tmp[0].rstrip(),data.readline().rstrip(),
                        data.readline().rstrip(),data.readline().rstrip())
