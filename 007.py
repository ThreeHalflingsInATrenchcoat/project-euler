import math

primes = 10001

#checks if number is prime, returns true or false
def is_it_prime(x):

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

i = 2
prime = 1

while(prime < primes):
    i += 1
    if(is_it_prime(i)):
        prime += 1

print(i)