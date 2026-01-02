import cmath

a = int(input('Write a value for a: '))
if a == 0:
    print("Please enter more than 0 ")
b = int(input('Write a value for b: '))
c = int(input('Write a value for c: '))


d = b**2 - 4 * a * c 
# solving the problem 
solve1 = (-b-cmath.sqrt(d))/(2*a)
solve2 = (-b+cmath.sqrt(d))/(2*a)
print("The solution are {0} and {1}".format(solve1,solve2 ))