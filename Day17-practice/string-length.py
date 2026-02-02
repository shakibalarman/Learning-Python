try:
    name = input("Enter your name ")
    if name == "":
        print("You didn't enter a any text")
        
    print("The length is ",len(name))

except TypeError:
    print("Error: Enter the input correctly")
finally:
    print("program end ")