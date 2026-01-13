marks  = {"Shakib": 40, "Rakib": 50, "Jisan": 50}
#printing marks 
print (marks)
#Access one student mark 
print(marks["Shakib"])
#update marks 
marks["Rakib"] = 70
print(marks)
#Add one students mark 
marks["Arman"] = 90
print(marks)
for name, mark in marks.items():
    print(name, ":" , mark)


