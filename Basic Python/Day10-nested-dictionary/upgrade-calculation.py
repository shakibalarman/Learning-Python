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
        students[name] = {"mark" : mark, "grade" : grade}
    return students

def calculate_total(students):
    total = 0
    for name, info in students.items():
        total+=info["mark"]
    return total

def calculate_average(students):
    total = calculate_total(students)
    average = total / len(students)
    return average
def find_top_student(students):
    highest_mark = -1
    top_student = ""
    for name, info in students.items():
        if info["mark"] > highest_mark:
            highest_mark = info["mark"]
            top_student = name 
    return highest_mark, top_student


students = input_students()

total = calculate_total(students)
average = calculate_average(students)
best = find_top_student(students)
print("Total:", total)
print("Average:", average)
print (best)