num1 = int(input("Enter a number "))
num2 = int(input("Enter another  number ")) 
operator = input("Enter an operator(+,-,*,/): ")
if operator=="+":
    print("The summation is ",num1+num2)
elif operator == "-":
    print("The substraction is ",num1-num2)
elif operator =="*":   
    print("The multiplicatio is ",num1*num2)
elif operator =="/":
    if num2 != 0:
     print("The division is ",num1/num2) 
    else:
        print("Error: do not made division by zero!")
 
else: 
    print("invalid operator")    
