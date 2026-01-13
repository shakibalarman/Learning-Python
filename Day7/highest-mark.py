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
result = highest_mark(marks)
print("The highest number is ",result)

