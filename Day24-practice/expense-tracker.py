expense = {}
try:
    count = int(input("How many expense do you want to enter  "))
    for i in range(count):
        name = input("Enter expense name ")
        amount = float(input("Enter expense amount "))
        expense[name] = amount 
    total = sum(expense.values()) 
    print("\n--- Expense Summary ---")
    for name, amount in expense.items():
        print(f"{name}: {amount}")

    print("Total Expense:", total)

    highest = max(expense, key= expense.get)
    print("Highest Expense:", highest, "-", expense[highest])

except ValueError:
    print("❌ Invalid number entered")       
    