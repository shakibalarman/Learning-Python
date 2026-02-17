try:
    marks = float(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("❌ Invalid marks")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: F")

except ValueError:
    print("❌ Invalid input")
