# Take name of 10 students in list and reversing the names.(using for loop)

students = []

for i in range(2):
     name = input(f"enter name of student {i+1} ")
     students.append(name)

print(students)

a = []

for name in students:
    rev_names = ""
    for j in range(len(name) -1, -1, -1):
        rev_names += name[j]   
    a.append(rev_names)  

print(a)

