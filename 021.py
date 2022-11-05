import math

def get_factors(x):
    sq = math.sqrt(x)
    factors = []
    more_factors = []
    half = None

    #ignore <= 1
    if(x <= 1):
        return []

    #skip even divisors for odd numbers
    if(x % 2 == 0 and x > 4):
        inc = 1
        #factors are only calculated to sqrt, add this if number is even 
#        half = x//2
    elif(x % 2 == 0):
        inc = 1
    else:
        inc = 2

    if(sq % 1 == 0):
        sq += 1

    for i in range(1, math.ceil(sq), inc):
        if(x % i == 0):
            factors.append(i)
            more_factors.append(x // i)

    for factor in reversed(more_factors):
        if(factor != x and factor != sq-1):
            factors.append(factor)

#    if(half is not None):
#        factors.append(half)

    return(factors)

def factor_sum(x):
    factors = get_factors(x)
    total = sum(factors)
    return(total)

def amicable(x):
    a = factor_sum(x)
    b = factor_sum(a)
    if(b == x and a != b):
        return True

amicable_numbers = []
max = 9999
for i in range(1, max+1):
    if(amicable(i)):
        amicable_numbers.append(i)

print(amicable_numbers)
print(sum(amicable_numbers))