try:
    with open("data.txt","r") as file:
        file.write("Hello, this is written safely.\n")
        file.write("python file error handling works. ")
except PermissionError:
    print("Error: You don't have permission to write this file.")
except FileNotFoundError:
    print("Error: Invalid file path")
else:
    print("file written successfully ")
finally:
    print("Programm end ")