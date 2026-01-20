try:
    a = int (input("Enter a number "))
    b = int (input("Enter another number "))
    result = a+b 
    print("Result : ", result)
except ValueError:
    print("Error: Enter numeric number only ")