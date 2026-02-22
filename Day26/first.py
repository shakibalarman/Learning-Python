try:
    a = int(input("Enter a number "))
    b = int(input("Enter another number "))
    result = a + b 
    print("The summation is ",result)
except ValueError:
    print("Error: enterf the  numeric value only ")