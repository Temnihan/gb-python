import Add_New_man as a
import Show_men as sh
import NewFile as nf

print(' выбери дейстие: ')
print("'s'- добавить новую запись")
print("'sh' показать файлы")
print("'i' - import file")
print("'e' = export file")

choise = input('выбери действие ')
if choise == 's':
    a.add_New()
elif choise == 'sh':
    sh.show()
elif choise == 'e':
    nf.export(input('введите имя и расширение'))