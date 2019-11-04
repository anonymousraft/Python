#pizza calculator 1.5 pizza should be given to every student

students = input('How many students are present today ')
student_int = int(students)
pizza_count = student_int/1.5
student_str = str(student_int)
print('You will need '+ str(pizza_count) + ' pizzas for '  + student_str + ' Students')
