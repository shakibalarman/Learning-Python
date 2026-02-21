numbers = []
try:
    n = int(input("Enter how many value you want "))
    for i in range(n):
        number = int(input("Enter the value "))
        numbers.append(number)
    print("The list is ",numbers)
    print("The length of number is",len(numbers))
except TypeError:
    print(" Error: ")
except Exception:
    print("Unexpected  Error ")
print("The program is end ")
    