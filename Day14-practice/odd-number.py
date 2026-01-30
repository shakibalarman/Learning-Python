

try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

except ValueError:
    print("Error: Please enter a valid integer!")
