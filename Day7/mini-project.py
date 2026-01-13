def calculate_total_mark(marks):
    total = 0
    for i in marks:
        total = total + i 
    return total
def calculate_average(marks):
    total = 0 
    for i in marks:
        total = total + i
    average = total/len(marks)
    return average
def highest_mark(marks):
    highest_number = marks[0]
    for n in marks:
        if n > highest_number:
            highest_number = n
    return highest_number
marks = []
for i in range(5):
    num = int(input("Enter the marks for every student "))
    marks.append(num)
result1  = calculate_total_mark(marks)
result2 = calculate_average(marks)
result3 = highest_mark(marks)
print("The total is ",result1)
print("The average is ", result2)
print("The highest number is ",result3)

