import math
from icecream import ic

num_of_truncatable_primes = 11
truncatable_primes = []

#checks if number is prime, returns true or false
def is_it_prime(x):

    sq = math.sqrt(x)
    if(x == 1):
        return False
    
    #allows incrementing by 2 through odds only
    if(x % 2 == 0):
        if(x == 2):
            return True
        else:
            return False

    #divide working number by odds until you reach the sqrt or find a factor
    div = 3
    while(x % div != 0 and div < sq):
        div += 2

    if(div > sq):
        return True
    else:
        return False

#requires int, returns true or false
def is_it_a_truncatable_prime(x):
    #check if number is prime
    if(is_it_prime(x) == False):
        return False

    #remove digits from left
    for i in range(1,len(str(x))):
        if(not is_it_prime(x % (10**(len(str(x))-i)))):
            #trunc = x % (10**(len(str(x))-i))
            #print(trunc)
            return False

    #remove digits from right
    for i in range(1,len(str(x))):
        if(not is_it_prime((x - x % (10**i)) // 10**i)):
            #trunc = (x - x % (10**i)) // 10**i
            #print(trunc)
            #ic(x)
            return False

    return True

num = 11
while(len(truncatable_primes) < 11):
    if(is_it_a_truncatable_prime(num)):
        truncatable_primes.append(num)

    num += 1

print(truncatable_primes)

print(sum(truncatable_primes))