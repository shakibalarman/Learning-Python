def max_of_three(a,b,c):
    if a>b and a>c:
        return a 
    elif b>c:
        return b
    else:
        return c
x = max_of_three(10,20,30)
print(x)