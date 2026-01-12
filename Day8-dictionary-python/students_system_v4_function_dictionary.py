def input_students():
    students = {}
    n = int(input("Enter number of students "))
    for i in range(n):
        name = input("Enter students name ")
        mark = int(input("Enter the marks for student "))
        students [name] = mark 
    return students 

def calculate_total(students):
    total = 0 
    for mark in students.values():
        
        total += mark 
    return total
def calculate_average(students):
    total = calculate_total(students)
    average = total / len(students)
    return average 

def find_top_student(students):
    highest_mark = -1
    top_student = ""

    for name, mark in students.items():
        if mark > highest_mark:
            highest_mark = mark
            top_student = name

    return top_student, highest_mark

students = input_students()

total = calculate_total(students)
average = calculate_average(students)
top_student, highest_mark = find_top_student(students)
print("\n--- Student Result Summary ---")
print("All Student:", students)
print("Total Marks:", total)
print("Average Marks:", average)
print("Top Student:", top_student)
print("Highest Mark:", highest_mark)


