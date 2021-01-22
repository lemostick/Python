import codecs
file = codecs.open( "6.txt", "r", "utf-8" )
data = file.read()
file .close()

subj = {}
with open('6.txt', 'r') as init_f:
	for line in init_f:
		subject, lecture, practice, lab = line.split()
		subj[subject] = int(lecture) + int(practice) + int(lab)
	print(f'Общее количество часов по предмету - \n {subj}')