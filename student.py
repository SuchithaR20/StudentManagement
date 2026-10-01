def add_student(l):
	name=input('Enter name:')
	rn=int(input('Enter roll no.:'))
	mark=float(input('Enter marks:'))
	clas=input('Enter class:')
	sec=input('Enter section:')
	l.append([name, rn, mark, clas, sec])
	return "Successfully added!"
def display_student(l):
	for i in l:
		print(i)
def search_student(l):
	rn=int(input('Enter roll no.:'))
	for i in l:
		if rn==i[1]:
			print(i)
			break
	else:
		print('No such student.')
def delete_student(l):
	rn=int(input('Enter roll no.:'))
	for i in l:
		if rn==i[1]:
			l.remove(i)
	return "Successfully deleted."
def update_student(l):
	rn=int(input('Enter the roll no. of the student whose details you wish to update:'))
	for i in l:
		if rn==i[1]:
			n=input('Enter name:')
			rn=int(input('Enter roll no.:'))
			mark=float(input('Enter marks:'))
			clas=input('Enter class:')
			sec=input('Enter section:')
			i[0]=n
			i[1]=rn
			i[2]=mark
			i[3]=clas
			i[4]=sec
			print('Successfully updated!')
			break
	else:
		print('No such student.')
		

	
