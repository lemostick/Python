from itertools import count
from math import factorial

def idontknow():
	for el in count(1):
		yield factorial(el)
num = input ('Введите число для получения факториала: ')
gen = idontknow()
x = 0
for i in gen:
	if x < int(num):
		x += 1
	else:
		break
	print (i)