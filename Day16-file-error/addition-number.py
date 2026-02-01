try:
    a = int(input("Enter a number "))
    b = int(input("Enter another number "))
    result = a * b
    print("The multiplication is ", result)
except ValueError:
    print("Error: input numeric value only")