balance = 10000
try:
    amount = int(input("Enter withdrawal amount "))
    if amount<=0:
        print("Invalid amount ")
    
    elif amount > balance:
        print("Insufficient balance ")
    else:
        balance = balance - amount 
        print("Withdrawal is Succesful ")
        print ("Remaining balance ",balance )
except ValueError:
    print("Error: Enter right input ")    