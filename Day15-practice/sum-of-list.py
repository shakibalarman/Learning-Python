try:
    numbers = []
    total = 0
    n = int(input("Enter the range "))
    for i in range(n):
        number = int(input("Enter the value "))
        numbers.append(number)
        total = total + number
    print("The sum is ",total)
except ValueError:
    print("Error: Enter numeric value only ")
        