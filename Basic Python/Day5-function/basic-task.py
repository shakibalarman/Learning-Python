def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
x = is_even(7)
print(x)

def square(n):
    return n*n
x= square(4)
print(x)

def max_two(a,b):
    if a>b:
        return a
    else:
        return b
x = max_two(10,20)
print("The largest number is ", x)