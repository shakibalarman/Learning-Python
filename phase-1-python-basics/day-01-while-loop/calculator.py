while True:
    print("Calculator menu ")
    print("1. Add")
    print("2. Subtruction ")
    print("3. Multiply ")
    print("4. Division ")
    print("5. exit ")
    choice = int(input("Which calculation you  want to run "))
    if choice == 5 :
        print("Thank you ")
        break
    num1= int(input("Enter a number "))
    num2 = int(input("Enter another number "))
    if choice == 1:
        print("Result: ",num1+num2)
    elif choice == 2:
        print("Result ", num1 - num2)
    elif choice ==3:
        print("Result ",num1*num2)
    elif choice == 4:
        if num2 == 0:
            print("Invalid ")
        else:
            print("Result ",num1/num2 )
