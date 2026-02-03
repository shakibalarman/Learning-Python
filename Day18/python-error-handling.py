try:
    
    file = open("data.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not exist. ")
finally:
    print("Program End ")