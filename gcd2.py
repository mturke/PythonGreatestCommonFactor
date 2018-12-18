
# define gcd function with 2 parameters, x and y
def gcd(x, y):
    # if y = 0 return x because 0 doesn't have a divisor
    # otherwise return the GCD of y and the remainder of x / y
    
    if (y == 0):
        return x
    else:
        return gcd(y,x % y)


print("A simple program to demonstrate using timeit")
