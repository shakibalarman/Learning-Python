data = {
    "name": "Shakib",
    "age": 22,
    "country": "Bangladesh"
}

key = input("Enter a key: ")

try:
    print("Value:", data[key])
except KeyError:
    print("❌ Key not found")
