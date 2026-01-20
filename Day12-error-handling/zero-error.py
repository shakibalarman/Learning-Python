try:
    a = int(input("Enter a number "))
    b = int (input("Enter another number "))
    result = a / b 
    print("The division is ", result)
    
except ZeroDivisionError:
    print ("Error: you cannot divided by zero ")
except ValueError:
    print("Error: Enter only numeric number ")