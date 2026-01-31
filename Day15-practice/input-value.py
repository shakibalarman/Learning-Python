user_input = input("Enter a number ")
try:
    number = int (user_input)
    print("The number is ",number )
except ValueError:
    print("Error: Enter a nemuric number ")