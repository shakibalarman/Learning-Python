# File: all_errors.py

try:
    num = int(input("Enter a number: "))
    result = 100 / num

    my_list = [1, 2, 3]
    print(my_list[5])

except ValueError:
    print("Please enter a number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

except IndexError:
    print("List index error!")

except Exception as e:
    print("Unknown error:", e)

else:
    print("Program ran successfully!")

finally:
    print("Program finished.")
