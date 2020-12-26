# print ('Введите через ", " числа для создания списка')
# glist = input ('> ')
# print (glist)
# print (glist.split(', '))

# j = 0
# for i in range(int(len(glist)/2)):
#   glist[j], glist[j+1] = glist[j+1], glist[j]
#   j += 2


userlength = int(input('Введите количество элементов списка: '))
glist = []
i = 0
n = 0
while i < userlength:
    my_list.append(input('Введите следующее значение списка: '))
    i += 1

for test in range(int(len(glist)/2)):
        glist[n], glist[n + 1] = glist [n + 1], glist[n]
        n += 2
print(glist)







# for i in glist.count():
# 	n = 0
# 	glist[n], glist[n+1] = glist[n+1], glist[n]
# 	n += 2
# 	print (i)

# A = [ 'ж', 4, 5, 7]
# A[0], A[1] = A[1], A[0]
# print (A)