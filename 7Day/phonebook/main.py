
print(' выбери дейстие: ')
print("'s'- добавить новую запись")
print("'sh' показать файлы")
print("'i' - import file")
print("'e' = export file")

choise = input('выбери действие ')
if choise == 's':
    import Add_New_man as a
    a.add_New()
elif choise == 'sh':
    import Show_men as sh
    sh.show()
elif choise == 'e':
    import NewFile as nf
    nf.export(input('введите имя и расширение'))