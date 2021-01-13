import math
import random
def createlist():
	mylist = []
	i = 0
	try:
		lenght = int(input ('Введите длину списка, для его генерации:\n'))
		while i < lenght:
			mylist.append(random.randint(0, 20))
			i += 1	
	except ValueError:
		return print('Ошибка: введённое - не число.')
	mynewlist = [el for el in mylist if mylist.count(el) == 1]
	print (f'{mylist} - сгенерированый список из {lenght} номеров:')
	print (f'{mynewlist} - верхний список без повторяющихся номеров')
	
createlist()