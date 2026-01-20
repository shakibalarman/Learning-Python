try:
    a = int (input("Enter a number "))
    b = int(input("Enter another number "))
    operator = input ("Enter operator(+,-,*,/): ")
    if operator == "+":
        result = a+b 
    elif operator == "-":
        result = a - b 
    elif operator == "*":
        result = a * b 
    elif operator == "/":
        result = a/b
    else: 
        raise ValueError("invalid operator")
except ValueError:
    print("Error: Enter numeric value only  ")
except ZeroDivisionError:
    print("Error: You can't devide by zero ")
else:
    print("result: ", result)
finally:
    print("Calculator program finished ")