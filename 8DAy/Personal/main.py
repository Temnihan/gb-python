import Add_New_man as a
import Show_men as sh
import export as nf
import os.path
import os
def show_menu():
    print('\n'+'┌'+'─'*30+'┐')   #┌───┬───┬───┐
    print('│ ВЫБЕРИ ДЕЙСТВИЕ: ')
    print('│'+'─'*30)
    print("│'f' = find employer")
    print("│'a'- добавить сотрудника")
    print("│'8' = export cvs")
    print("│'s' выести на экран всех сотрудников")
    print("│'i' - import file")
    print("│'ee' = export в текстовом файле одной строкой")
    print("│'e' = export file .txt  формат вывода построчно")
    return input('выбери действие ')

choise = show_menu()

if choise == 'a':
    sn = input('фамилия: ')
    name = input('имя: ')

    t = input('number: ')

    d = input('status?: ')
    sep = ','
    a.add_New(sn,name,t,d,sep)
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
elif choise == '8':
    file = input('название файла?')+'.csv'
    nf.export_csv(file)
    print('done')
elif choise == '2':
    file = input('кого выбрать?')
    sh.find_empl(file)
    print('done')
