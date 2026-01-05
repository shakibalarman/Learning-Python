n = input("Write anything you want ")
numbeofdigit = 0
numberofletter = 0
numberofword = 0 
for x in n: 
    x = x.lower()
    if x>='a' and x<='z':
        numberofletter = numberofletter + 1
    elif x>='0' and x <='9':
        numbeofdigit = numbeofdigit + 1
    elif x ==' ':
        numberofword = numberofword + 1

print("The number of letter is ", numberofletter)
print("The number of digit is ", numbeofdigit )
print("The number of word is", numberofword)
 
