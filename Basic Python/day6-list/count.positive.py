def count_positive(number):
    count = 0
    
    for n in number:
        if n > 0:
            count+=1
    return count  
numbers=[]
for i in range(6):
    num = int(input("Enter a number "))
    numbers.append(num)
     
result = count_positive(numbers)
print("Total positive number is ",result)
