
my_tuple = ("apple", "banana", "cherry", "mango", "orange")

try:
    
    index = int(input("Enter an index number: "))

   
    print("Value at index", index, "is:", my_tuple[index])

except ValueError:
    print("Error: Please enter a valid integer number.")

except IndexError:
    print("Error: Index is out of range.")

except Exception as e:
    print("Unexpected error:", e)
