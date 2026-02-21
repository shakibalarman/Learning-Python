password = input("Enter password: ")

if len(password) < 6:
    print("❌ Password  too short (minimum  6  characters)")
else:
    print("✅ Password is valid")
