import timeit
import statistics

"""
def maxNum(lst):
    print(lst)
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0],maxNum(lst[1:]))

lst = [2,44,61,8,22,12,34]
print(maxNum(lst))
"""

def main():
    lst = [2,44,61,8,22,15,37]
    print("List: ",lst)
    print("Finding max number in list:", maxNum(lst))

   
def maxNum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0],maxNum(lst[1:]))

print("Run times: ")
t1 = timeit.repeat(repeat = 5, number = 1000000)
print(t1)
avg = statistics.mean(t1)
print("Average run time is: ", avg)

main()













