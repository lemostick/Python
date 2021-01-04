def div(*args):
	try:
		arg1 = int(input("Введите делимое число: "))
		arg2 = int(input("Введите делитель: "))
		res = arg1 / arg2
	except ValueError:
		return 'Числовая ошибка.'
	except ZeroDivisionError:
		return "Ошибка. На ноль делить нельзя."
	return res
print (div())