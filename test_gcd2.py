# import timeit and random
# test program for demonstration of measuring performance
import timeit
import random

#generate two random even numbers to use to find gcd
x = random.randint(1, 50) * 2
y = random.randint(1, 50) * 2

# print random numbers
print("Number 1: ", x)
print("Number 2: ", y)

#def function gcd with parameters x and y
def gcd(x, y):
    # if y = 0 return x because 0 doesn't have a divisor
    # otherwise return the GCD of y and the remainder of x / y
    
    if (y == 0):
        return x
    else:
        return gcd(y,x % y)
print("GCD is: ", gcd(x, y))
# create the timeit object pointing to file and function names as well as globals 
t=timeit.Timer("gcd2.gcd(x, y)","import gcd2", globals = globals())

# This is a convenience function that calls the timeit() repeatedly, returning a list of results.
# The first argument specifies how many times to call timeit().
# The second argument specifies the number executions of the main statement

# timeit will make 5 passes and each pass will call the function 1000 times ( timing is the total of 1000 calls )

print("calling timeit for 5 passes, each pass is 1000 calls timed cumulatively") 

results=t.repeat(5,1000)

for i, item in enumerate(results):
    print(i, "\t", item)

print("same example, but using range to show how the number arg effects cpu usage ")

#show the effect of running more passes using range
for i in range(250000,1000001,250000):

    #show user what the number input does performance wise
    print("timeit number value is = ", i)

    # timeit will make 5 passes and each pass will be the value of "i" calls
    results=t.repeat(5,i)

    for i, item in enumerate(results):
        print(i, "\t", item)
