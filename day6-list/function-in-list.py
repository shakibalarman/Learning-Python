numbers= []
for n in range(5):
    num = int (input("Enter number "))
    numbers.append(num)
def count_even(numbers):
    count = 0
    for i in numbers:
        if i %2 == 0:
            count+=1
    return count 

result = count_even(numbers)
print("Total even numbers ", result )