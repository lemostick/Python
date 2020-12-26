my_list = [7, 5, 3, 3, 2]
numb = input('Введите число для "рейтинга": ')
numb = int(numb)
# Здесь я вдруг забил на попытки сделать из этого линейный код
# и прописал функцию, ибо её структурировать проще.
def rating(r_list, num):
	if num > max(r_list):
		r_list.insert(0, num)
	elif num in r_list:
		r_list.insert(r_list.index(num), num)
	else:
		r_list.append(num)
rating(my_list, numb)
print (my_list)

#а дальше находится первая попытка сделать линейный код

# user = input('> ')
# user = int(user)
# n = 0
# # for i in my_list:
# # 	num = int(my_list[n])
# # 	n += 1
# # 	if user >= num:
# # 		my_list.insert(num+1, user)
# # print (my_list)