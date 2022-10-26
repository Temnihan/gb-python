import Add_New_man as a
import Show_men as sh
import export as nf
import os.path
import os
print(' выбери дейстие: ')
print("'s'- добавить новую запись")
print("'sh' показать файлы")
print("'i' - import file")
print("'ee' = export onelinefile")
print("'e' = export file")

choise = input('выбери действие ')
if choise == 's':
    sn = input('фамилия'),
    name = input('имя: '),
    t = input('number: '),
    d = input('описание'),
    sep = ','
    a.add_New(sn,name,sn,d,sep)
elif choise == 'sh':
    sh.show()
elif choise == 'ee':
    file = input('name? ')+'.txt'
    nf.export1(file)
    print('done')
elif choise == 'e':
    file = input('name? ')+'.txt'
    nf.export2(file)
    print('done')
elif choise == 'i':
    # file = os.system(r"explorer.exe D:\удалить\gb\Python\7Day\phonebook")
    file = input('какйо файл импортировать? ')+'.txt'
    while not os.path.isfile(file):
        print("такого файла не сущетсвует")
        file = input('какйо файл импортировать? ')+'.txt'
    a.import_file(file)
    print(f'сделанно из файла {file} в файл phonebook.txt')
