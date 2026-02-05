

try:
    with open("report.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("Report file not found!")
