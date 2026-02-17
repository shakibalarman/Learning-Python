try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    sum = a+b
    print("The summation is ", sum )
    sub = a - b
    print("The substruction is ", sub )
    multiplication = a*b
    print("The multiplication is ", multiplication)
    division = a/b
    print ("The division is ", division )
except ZeroDivisionError:
    print("Error: you cant divide by zero")
except ValueError:
    print("Error: Pls enter a numeric degit ")