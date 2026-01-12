def second_largest(numbers):
    if numbers[0]>numbers[1]:
        largest = numbers[0]
        second_largest = numbers[1]
    else:
        largest = numbers[1]
        second_largest = numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i]>largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i]>second_largest and numbers[i]!=largest:
            second_largest = numbers[i]
    return second_largest
number = [10,20,30,40,50]
result = second_largest(number)
print ("The second largest number is ", result)
