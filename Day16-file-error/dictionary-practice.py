marks = {}
n = int(input("Enter number of students "))
try:
    for i in range(n):
        name = input("Enter name for student ")
        mark = int(input("Enter marks for student "))
        marks[name] = mark 
    for name,mark in marks.items():
        print( name, ":", mark )
except(ValueError, KeyError):
    print("Error: Enter correct key")
        