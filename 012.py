import math

trinums = [1]

#accepts an array of triangular numbers, must start with 1, and have at least one entry
def add_trinum(x):
    return(x[-1] + len(x) + 1)

def get_factors(x):
    sq = math.ceil(math.sqrt(x))
    
    #skip even divisors for odd numbers
    if(x % 2 == 0):
        inc = 1
    else:
        inc = 2

    count = 0
    #special case for 1
    if(x == 1):
        count += 1


    for i in range(1, sq, inc):
        if(x % i == 0):
            if(i == x):
                count += 1
            else:
                count += 2
    return(count)

while(get_factors(trinums[-1]) <= 500):
    trinums.append(add_trinum(trinums))

print(trinums[-1])
print(get_factors(trinums[-1]))