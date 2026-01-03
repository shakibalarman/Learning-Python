num = int(input("Enter a number " ))
if(num % 3 == 0 and (num % 5 == 0)):
    print("Magic Number")
elif(num % 3 == 0):
    print("Lucky number")
elif(num % 5 == 0):
    print("Cool number ")
else:
    print("Normal Number")
