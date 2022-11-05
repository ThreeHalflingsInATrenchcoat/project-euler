import math

max = 999999

primes = []
circ_primes = []

#checks if number is prime, returns true or false
def is_it_prime(x):

    sq = math.sqrt(x)

    #special case for 2
    if(x == 2):
        return True

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

#requires an integer, returns a list of integer rotations, including the integer itself
def int_rotations(x):
    rots = []
    for i in range(len(str(x))):
        rot = int(str(x)[i:] + str(x)[:i])
        rots.append(rot)
    return rots

#calculate all primes below or equal to max and store in primes list
for num in range(2, max+1):
    if(is_it_prime(num)):
        primes.append(num)

#loop through primes and check if circular, not optimized
for prime in primes:
    rots = int_rotations(prime)
    if(all(is_it_prime(rot) for rot in rots)):
        circ_primes.append(prime)

print(circ_primes)
print(len(circ_primes))