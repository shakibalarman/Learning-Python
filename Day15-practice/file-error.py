filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")

except Exception as e:
    print("Unexpected error:", e)
