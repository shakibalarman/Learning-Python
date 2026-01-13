def max_of_three(a,b,c):
    if a>b and a>c:
        return a 
    elif b>c:
        return b
    else:
        return c
x = max_of_three(10,20,30)
print(x)

while True:
    print("\n---Utiliti Menu---")
    print("1. Check Even or Odd")
    print("2. Find square")
    print("3. Find largest of two number ")
    print("4. Exit ")
    choice = int(input("Enter your choice "))
    if choice == 4 :
        print("Thank You! ")
        break 