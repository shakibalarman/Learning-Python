def grade_mark(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    elif mark >=40:
        return "E"
    else:
        return "F"
    
def input_students():
    students = {}
    n = int(input("Enter number of students "))
    for i in range(n):
        name = input ("Enter the name of students ")
        mark = int(input("Enter the mark for students "))
        grade = grade_mark(mark)
        students[name] = {"mark":mark,"grade":grade}
    return students 

students = input_students()
for name, info in students.items():
    info["mark"]
    info["grade"]
    print (name , info["mark"], info["grade"])
    
    