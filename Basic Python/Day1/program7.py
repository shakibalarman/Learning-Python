mark = int(input("Enter you mark"))
print("Your total mark is :")
if mark>90:
    print("Grade A")
elif (mark >80 and (mark<90)):
    print ("Grade B")
elif (mark>=70 and (mark <=79)):
    print("Grade C")
elif (mark>=60 and (mark<=69)):
    print("Grade D")
elif (mark>=50 and (mark<=59)):
    print ("Grade E")
else:
    print("fail")               