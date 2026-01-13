def greater_than_x(numbers,x):
    count = 0
    for n in numbers:
        if n > x:
            count+= 1
    return count 
number = []
x = 10
for i in range (5):
    num = int(input("Enter the number "))
    number.append(num)

result = greater_than_x(number,x)
print(result)

            