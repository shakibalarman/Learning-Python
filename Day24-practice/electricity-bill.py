try:
    unit = int (input("Enter how many unit you consumed "))
    if unit < 0:
        print("invalid unit ")
        
    elif unit <= 100:
        bill = unit * 5
    elif unit <= 200:
        bill = (100*5)+(unit - 100)*8
    else:
        bill = (100*5) + (100*8)+(unit - 200)*10
        
    print("Total bill: ",bill)
except ValueError:
    print("Invalid input ")