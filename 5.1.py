file = open('1.txt', 'w')
line = input('Введите текст \n')
while line:
	file.writelines(f'{line}\n')
	line = input('Введите текст \n')
	if not line:
		break
file.close()
file = open('1.txt', 'r')
content = file.readlines()
print(content)
file.close()