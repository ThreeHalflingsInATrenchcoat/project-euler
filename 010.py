import math

#checks if number is prime, returns true or false, does not work for 1 or 2 because I already know that, and extra cycles
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

#not doing math on 2, i know it's prime
sum = 2

for i in range(3, 2000000, 2):
    if(is_it_prime(i)):
        print(i)
        sum += i

print(sum)