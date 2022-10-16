
my_text = 'Напишите программу содержающу все слова содержащие "абв" сабвва да'
my_text =  list(filter(lambda ntext: 'абв' not in ntext, my_text.split()))
my_text = " ".join(my_text)
print(my_text)