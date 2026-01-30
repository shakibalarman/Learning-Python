try:
    name = input("Enter your name: ").strip()

    if name == "":
        raise ValueError("Name cannot be empty!")

    print("Uppercase Name:", name.upper())

except ValueError as e:
    print("Error:", e)
