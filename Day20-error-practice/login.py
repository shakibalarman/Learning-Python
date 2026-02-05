

try:
    username = input("Enter username: ")
    age = int(input("Enter age: "))

    print(f"Welcome {username}, Age: {age}")

except ValueError:
    print("Age must be a number!")
