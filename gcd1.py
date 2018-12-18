# assign values to vars x and y
x = 70
y = 60

# define function gcd with 2 parameters, x and y 
def gcd(x, y):
    # while y doesnt equal 0
    # x = y and y equals remainder of x divided by y
    # if smaller of two ints divides evenly the smaller number is returned
    # otherwise return remainder using modulus of larger int divided by smaller in x

    while y != 0:
        x, y = y, x % y
    return x
# print the value of x, y
# print GCD by calling gcd with x and y passed through
print("A simple program to demonstrate using timeit")
print("Number 1: ", x)
print("Number 2: ", y)
print("GCD is: ", gcd(x, y))

