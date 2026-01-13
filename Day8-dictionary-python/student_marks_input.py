marks = {}
n = int (input("Enter number of students "))
for i in range (n):
    name = input("Enter the students name ")
    mark = int(input("Enter marks for student: "))
    marks[name] = mark 

for name, mark in marks.items():
    print(name , ":", mark )