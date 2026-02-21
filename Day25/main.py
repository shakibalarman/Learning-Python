students = {}
try:
    count = int(input("Enter how many student "))
    for i in range(count):
        name = input("Enter the name of student ")
        mark = int(input("Enter the marks for student "))
        students[name] = mark 
    print(students)
except ValueError:
    print("Error: your input is wrong ")