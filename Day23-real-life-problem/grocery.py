try:
    item1 = float(input("Enter price of item 1: "))
    item2 = float(input("Enter price of item 2: "))
    item3 = float(input("Enter price of item 3: "))

    total = item1 + item2 + item3
    tax = total * 0.05
    final_amount = total + tax

    print("Total:", total)
    print("Tax (5%):", tax)
    print("Final Amount:", final_amount)

except ValueError:
    print("❌ Invalid price input")
