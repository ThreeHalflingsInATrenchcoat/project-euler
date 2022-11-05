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

#returns true if number is abundant
def is_abundant(x):
    factors = get_factors(x)
    factor_sum = sum(factors)
    if(factor_sum > x):
        return True
    else:
        return False

#returns true if number is the sum of two abundant numbers
def sum_of_abundant(x,nums):
    for i in range(0,len(nums)):
        if(nums[i] > x):
            return False
        else:
            for j in range(i, len(nums)):
                if(i + j == x):
                    return True

abundant_numbers = []

for number in range(1, 28123):
    if(is_abundant(number)):
        abundant_numbers.append(number)

sums = [0] * 28124

for i in range(0, len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        sumof2abundantnums = abundant_numbers[i] + abundant_numbers[j]
        if(sumof2abundantnums <= 28123 and sums[sumof2abundantnums] == 0):
            sums[sumof2abundantnums] = sumof2abundantnums

total = 0

for i in range(1,len(sums)):
    if sums[i] == 0:
        total += i

print(total)