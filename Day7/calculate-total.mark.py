def calculate_total_mark(marks):
    total = 0
    for i in marks:
        total = total + i 
    return total

marks = []
for i in range(5):
    num = int(input("Enter students mark "))
    marks.append(num)
x = calculate_total_mark(marks)
print("The total marks is  ", x)
