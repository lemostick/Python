
firsttry = input('Введите результат первого дня в км: ')
neededres = input('Введите желаемый результат в км: ')
day = 1
while int(firsttry)<int(neededres):
	firsttry = float(firsttry)*1.1
	print (str(day) + '-й день: '+ str(firsttry))
	day += 1
print ('На ' + str(day) + '-й день, спортсмен достиг результата не менее ' + str(neededres) + ' км.')

