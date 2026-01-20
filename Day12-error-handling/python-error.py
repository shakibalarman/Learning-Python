try:
    n = int (input("Enter a number "))
    print("The square is  ", n*n)
except ValueError:
    print ("Error: enter a numeric value ")