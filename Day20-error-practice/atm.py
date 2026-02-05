

balance = 5000

try:
    withdraw = int(input("Enter withdraw amount: "))

    if withdraw > balance:
        raise ValueError("Insufficient Balance")

    balance -= withdraw
    print("Remaining Balance:", balance)

except ValueError as e:
    print("Error:", e)
