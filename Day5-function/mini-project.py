def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def square(n):
    return n*n

def max_two(a,b):
    if a>b:
        return a
    else:
        return b
    
while True:
    print("\n---Utility Menu---")
    print("1. Check Even or Odd")
    print("2. Find square")
    print("3. Find biggest  of two number ")
    print("4. Exit ")
    choice = int(input("Enter your choice "))
    if choice == 4 :
        print("Thank You! ")
        break     
    if choice == 1:
        num = int(input("Enter  a  number "))
        if is_even(num):
            print("Even")
        else:
            print("Odd")
    elif choice == 2:
        num = int(input("Enter a number "))
        print(square(num))
    elif choice == 3:
        num1 = int(input("Enter a number "))
        num2 = int(input("Enter another number "))
        print("The largest between two number is " ,max_two(num1,num2))
    else:
        print("Invalid Choice ")
        
