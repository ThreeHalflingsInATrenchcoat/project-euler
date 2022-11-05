import math
from itertools import permutations
#requires string, returns true or false
def createPandigital(ln):
    arr = []
    for i in range(1, ln+1):
        arr.append(i)
    return arr

#requires positive int, checks if number is prime, returns true or false
def isPrime(x):

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

for i in reversed(range(1,10)):
    pandigital = createPandigital(i)
    pandigitals = permutations(pandigital)
    pandigitals = reversed(sorted(pandigitals))
    for p in list(pandigitals):
        pS = ''.join(map(str, p))
        if(isPrime(int(pS))):
            break
    if(isPrime(int(pS))):
        break

print(pS)