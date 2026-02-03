try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found ")
finally:
    print("program end")