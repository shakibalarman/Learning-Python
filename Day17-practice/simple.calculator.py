try:
    operator = input("Enter an operator from (+ or -): ")
    
    if operator not in ["+" , "-"]:
        raise ValueError("Invalid operator ")
    a = int (input("Enter first number "))
    b = int (input("Enter second number "))
    
    if operator == '+':
        result = a + b 
    else: 
        result = a - b 
    print ("The result is ", result )
except ValueError:
    print("Error: Please Enter valid number or operator  ")
finally:
    print("End ")