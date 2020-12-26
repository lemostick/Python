income = int(input('Введите месячную выручку вашего предприятия: '))
outcome = int(input('Введите месячные расходы вашего предприятия: '))
if (income > outcome):
	print ('Ваше предприятие работает в прибыль, поздравляем!')
	result = income - outcome
	print ('Ваша месячная выручка составляет: '+ str(result))
	plus = True
elif (outcome > income):
	print ('Ваше предприятие работает в убыток, советую сделать что-то с этим.')
	result = income - outcome
	print ('Ваш месячный убыток составляет: '+ str(result))
elif (income == outcome):
	print ('Ваше предприятие работает в ноль. Не хорошо, но и не плохо.')
else:
	print ('Произошла ошибка.')

if (plus == True):
	workers = input('Введите количество ваших сотрудников для расчёта прибыли на одного работника: ')
	incperworker = int(result)/int(workers)
	print ('Ваша прибыль на одного сотрудника: ' + str(incperworker))
else:
	print ('Программа расчёта завершена.')

