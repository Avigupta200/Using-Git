from student import Student
from reversing import reverse_list, reverse_names


def main():
    students = []

    for i in range(2):
        name = input(f"Enter name of student {i + 1}: ")
        students.append(Student(name))

    print("Original students:")

    for student in students:
        print(student.name)

    reversed_students = reverse_list(students)

    print("\nReversed list:")

    for student in reversed_students:
        print(student.name)

    reversed_names = reverse_names(students)

    print("\nReversed names:")

    for name in reversed_names:
        print(name)


if __name__ == "__main__":
    main()