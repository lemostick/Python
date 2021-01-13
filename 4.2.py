import math
import random
def bignumber():
	mylist = []
	i = 0
	try:
		lenght = int(input ('Введите длину списка, для его генерации:\n'))
		while i < lenght:
			mylist.append(random.randint(0, 1000))
			i += 1	
	except ValueError:
		return print('Ошибка: введённое - не число.')
	mynewlist = [el for num, el in enumerate(mylist) if mylist[num - 1] < mylist[num]]
	print (f'{mylist} - исходный список') 
	print (f'{mynewlist} - новый спиоск') 
bignumber()