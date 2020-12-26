user = input('Введите слова, разделённые пробелом: ')
user = user.split(' ')
flist = user
print (flist)
print (len(flist[0]))
m = 0
n = 0
for i in flist:
	if (len(flist[m]))>=10:
		print ('№' + str(m+1) + ': ' + str(i[:10]))
		m += 1
	else:
		print ('№' + str(m+1) + ': ' + str(flist[m]))
		m += 1