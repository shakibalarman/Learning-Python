numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index (0-4): "))

    print("Value:", numbers[index])

except IndexError:
    print("Error: Index out of range!")

except ValueError:
    print("Error: Please enter a valid integer!")
