try:
    a = int(input("Enter a number for a "))
    b = int(input("Enter a number for b "))
    if a > b:
        print("The largest number is ", a)
    else:
        print("The largest number is ",b)
except ValueError:
    print ("Error: Enter numeric number only")