expenses = {}

try:
    count = int(input("How many expenses do you want to enter? "))

    for i in range(count):
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses[name] = amount

    total = sum(expenses.values())

    print("\n--- Expense Summary ---")
    for name, amount in  expenses.items():
        print(f"{name}: {amount}")

    print("Total Expense:", total)

    highest = max(expenses, key=expenses.get)
    print("Highest Expense:", highest, "-", expenses[highest])

except ValueError:
    print("❌ Invalid number entered")
