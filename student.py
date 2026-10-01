def add_student(l):
	name=input('Enter name:')
	rn=int(input('Enter roll no.:'))
	mark=float(input('Enter marks:'))
	clas=input('Enter class:')
	sec=input('Enter section:')
	l.append([name, rn, mark, clas, sec])
	return "Succssesfully added!"
def display_student(l):
	for i in l:
		print(i)
def search_student(l):
	rn=int(input('Enter roll no.:'))
	for i in l:
		if rn==l[1]:
			print(i)

	
