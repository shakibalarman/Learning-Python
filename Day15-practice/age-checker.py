try:
    age = int(input("Enter your age "))
    if age >=18:
        print("Adult ")
    else:
        print("minor")
except ValueError:
    print("Error: Enter a numeric number ")