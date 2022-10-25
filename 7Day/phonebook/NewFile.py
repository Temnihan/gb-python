def export(name):
    ph =open('phonebook.txt','r')
    with open(name,'w') as newph:
        for line in ph:
            newph.writelines(line)
    ph.close()
