try:
    units = float(input("Enter electricity units used: "))

    if units < 0:
        print("❌ Invalid units")
    elif units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 8
    else:
        bill = (100 * 5) + (100 * 8) + (units - 200) * 10

    print("Total Bill:", bill)

except ValueError:
    print("❌ Invalid input")
