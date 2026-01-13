sum=0
i = 2
while i<=20:
    sum = sum + i
    i+=2
    if i % 2 == 0:
        print("Even",i)
        
print("The sum of even number is ",sum)    