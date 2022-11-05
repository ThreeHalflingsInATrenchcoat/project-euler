from math import factorial
from icecream import ic

min = 3
max = 2540160 #9!*7

sums = []

def intToList(x):
    lst = [int(i) for i in str(x)]
    return(lst)



for num in range(min, max + 1):
    flist = intToList(num)
    sum_ = 0
    for f in flist:
        sum_ += factorial(f)
        if(sum_ == num):
            sums.append(sum_)

print(sums)
print(sum(sums))