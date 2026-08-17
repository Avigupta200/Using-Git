def reverse_list(students):
    reversed_students = []

    for i in range(len(students) - 1, -1, -1):
        reversed_students.append(students[i])

    return reversed_students


def reverse_names(students):
    reversed_names = []

    for student in students:
        name = student.name
        reversed_name = ""

        for i in range(len(student.name) - 1, -1, -1):
            reversed_name += student.name[i]

        reversed_names.append(reversed_name)

    return reversed_names