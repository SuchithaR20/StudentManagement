import student
print('Welcome to Student Management System!')
student_details=[['Arun', 26, 91, 12, 'c'],['Sana', 13, 89, 11, 'a']]
x='y'
while x=='y' or x=='Y':
	print('''Menu: 1)Add a student
		2)Display student details
		3)Search for a student
		4)Delete a student''')
	ch=int(input('Enter your choice(1,2,3,4):'))
	if ch==1:
		print(student.add_student(student_details))
	elif ch==2:
		student.display_student(student_details)
	elif ch==3:
		student.search_student(student_details)
	elif ch==4:
		print(student.delete_student(student_details))
	else:
		print('Invalid choice.')
	x=input('Do you wish to choose again?(y/n):')

