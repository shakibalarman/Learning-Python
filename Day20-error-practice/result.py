

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

except ValueError as e:
    print("Error:", e)
