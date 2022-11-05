import math
from icecream import ic

min_ = 10
max_ = 99

def intToList(x):
    lst = [int(i) for i in str(x)]
    return(lst)

fractions = []

#loop through numerators
for num in range(min_, max_ + 1):
    #loop through denominators
    for den in range(num, max_ + 1):
        if(num == den):
            continue

        #get num and den as lists
        denL = intToList(den)
        numL = intToList(num)
        #check for overlapping numbers
        #loop through numerator digits
        for i in numL:
            #if numerator digit exists in denominator
            if i in denL:
                if(i == 0 or 0 in numL or 0 in denL):
                    continue
                rem_num = numL
                rem_den = denL
                numL.remove(i)
                denL.remove(i)
                if(num/den == rem_num[0] / rem_den[0]):
                    fractions.append([num,den])

print(fractions)

prod = [1, 1]

for fraction in fractions:
    prod[0] *= fraction[0]
    prod[1] *= fraction[1]

lcd = prod[1]/prod[0]

print(int(lcd))