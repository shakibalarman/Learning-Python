marks = {}
n = int(input(" Enter  number  of  student "))
for i in range(n):
    name = input (" Enter  student  names ")
    mark = int(input(" Enter  marks  for  students "))
    marks[name] = mark 
#total number 
total = 0 
for mark in marks.values():
    total += mark
#average 
average = total / len(marks)
#find the highest mark and top student 
highest_mark = -1
top_student = ""
for name, mark in marks.items():
    if mark > highest_mark:
        highest_mark = mark
        top_student = name 
print (" All marks is  ", marks )
print(" Total mark is  ", total)
print ("  Average mark is ", average)
print("  Highest mark is ", highest_mark)
print("  Top student is ", top_student)

