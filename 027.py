from icecream import ic
import math

#checks if number is prime, returns true or false
def is_it_prime(x):
    if(x <= 0):
        return False

    sq = math.sqrt(x)

    #allows incrementing by 2 through odds only
    if(x % 2 == 0):
        return False

    #divide working number by odds until you reach the sqrt or find a factor
    div = 3
    while(x % div != 0 and div < sq):
        div += 2

    if(div > sq):
        return True
    else:
        return False

#returns result of quadratic formula
def quad(a, b, n):
    result = n**2 + a*n + b
    return result

#initialize variables
max_a = 0
max_b = 0
max_primes = 0
cycles = 0

#loop through a, b, n values
for a in range(-999,1000):
    for b in range(-1000,1001):
        # get result of first n
        n = 0
        result = quad(a, b, n)
    
        #check if result is prime, increment n until end of primes
        while(is_it_prime(result)):
            n += 1
            result = quad(a, b, n)
        if(n > max_primes):
            max_primes = n
            max_a = a
            max_b = b    

ic(max_primes)
ic(max_a)
ic(max_b)

prod = max_a * max_b
ic(prod)