import student
student_details=[['Arun', 26, 91, 12, 'c'],['Sana', 13, 89, 11, 'a']]
print('''Menu: 1)Add a student
		2)Display student details
		3)Search for a student''')
ch=int(input('Enter your choice(1,2,3):'))
if ch==1:
	print(student.add_student(student_details))
elif ch==2:
	student.display_student(student_details)
elif ch==3:
	student.search_student(student_details)
else:
	print('Invalid choice.')
	
