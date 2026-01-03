#name = input("Enter the name of a student")
math = int(input("Math = "))
physics = int(input("Physics = "))
CSE = int(input("CSE = "))
if ((math>100 or math < 0) or (physics >100 or physics <0) or (CSE >100 or CSE <0) ):
    print("Invalid mark input ")
    exit()
    
else:
    total = math + physics + CSE
    average = total/3 
    print("Total number is ", total)
    print("Average numer is ", average)

    #pass or fail
if (math < 40 or  physics < 40 or CSE < 40):
    print("Failed")
else:
    print("pass")

#Grading System 
    if ( average>=80):
        print("Grade A+ ")
    elif(average>=70 and average<=79):
        print("Grade A ")
    elif(average>=60 and average<=69):
        print("Grade A- ")
    elif(average>=50 and average<=59):
        print("Grade B ")
    elif(average>=40 and average<=49):
        print("Grade C ")
    else:
        print("Fail")





