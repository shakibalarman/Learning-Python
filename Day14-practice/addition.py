try:
    a = int (input("Enter a number "))
    b = int (input("Enter another number "))
    result = a + b 
    print ("sum = ", result )
except ValueError:
    print("Error: Enter a numeric number ")
    