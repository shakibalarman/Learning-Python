try:
    n = int(input("Enter a number "))
except ValueError:
    print("Error: Enter the correct value only ")
else:
    print("You entered: ", n )
    print("Square is ", n*n)