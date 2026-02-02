number = []
try:
    n = int(input("how many value "))
    for i in range(n):
        value = int(input("Enter value "))
        number.append(value)
    print("The list is ", number )
except  Exception as e:
    print("Error: You entered wrong value ")
finally: 
    print ("program end")