def input_students():
    students = { }
    n = int(input("Enter number of students"))
    for i in range(n):
        name = input("Enter students name ")
        mark = int (input("Enter the marks "))
        students[name] = mark
    return students
def grade_mark(mark):
    if mark >=80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    else:
        return 'F'
students = input_students()
for name , mark in students.items():
    grade = grade_mark(mark)
    print(name, mark, grade)