def calculate_average(marks):
    total = 0 
    for i in marks:
        total = total + i
    average = total/len(marks)
    return average
marks = [10,20,30,40]
result = calculate_average(marks)
print("The average is ",result)

