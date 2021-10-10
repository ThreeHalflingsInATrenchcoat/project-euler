import math

#technically not all the factors, but it'll do for this problem
factors = []

#number to calculate the largest prime of, not a constant so I don't have to import the library
num = 600851475143
#working number, so the original isn't lost
num_divd = num

#returns smallest factor, or -1 if prime
def smallest_factor(x):
    sq = math.floor(math.sqrt(x))

    #allows incrementing by 2 through odds only
    if(x % 2 == 0):
        return 2

    #divide working number by odds until you reach the sqrt or find a factor
    div = 3
    while(x % div != 0 and div < sq):
        div += 2

    #-1 indicates the working number is prime, otherwise return the factor
    if(div >= sq):
        return -1
    else:
        return div

#always do this at least once to populate factors list
while True:
    res = smallest_factor(num_divd)
    if(res == -1):
        factors.append(num_divd)
        break
    else:
        factors.append(res)
        num_divd = num_divd // res

print(factors)
print(factors[-1])