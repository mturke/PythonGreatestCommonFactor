import timeit

# timeit object with  ints 8 and 12 passed through function with globals included 
t = timeit.Timer("gcd1.gcd(70,60)","import gcd1")


print("calling timeit for 5 passes, each pass is 1000 calls timed cumulatively") 

# timeit makes 5 passes and each calls gcd function 1000 times
results = t.repeat(5,1000)

for i, item in enumerate(results):
    print(i, "\t", item)

# timeit using range to run more passes 
for i in range(25000,100001,25000):

    # show user what the number input does performance wise
    print("timeit number value is = ", i)

    # timeit makes 5 passes and each is value of calling i
    results=t.repeat(5,i)

    for i, item in enumerate(results):
        print(i, "\t", item)
