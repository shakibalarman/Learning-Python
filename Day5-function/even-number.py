def is_even(a):
        if a % 2 ==  0:
            return True
        else:
            return False

        
for i in range(1 , 19):
    if is_even(i):
        print(i)
