balance = 10000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("✅ Withdrawal successful")
        print("Remaining balance:", balance)

except ValueError:
    print("Please enter a valid number")
