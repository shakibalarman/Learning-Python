

data = {"temp": 32}

try:
    print("Temperature:", data["humidity"])

except KeyError:
    print("Humidity data not available!")
