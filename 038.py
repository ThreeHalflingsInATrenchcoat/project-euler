#requires positive int
def isPandigital(x):
    ordered = ''.join(sorted(str(x)))
    if(ordered == '123456789'):
        return True
    else:
        return False 

def incremental_multiply(num):
    strng = ''
    mult = 1
    while len(strng) < 9:
        strng = strng + str(num * mult)
        mult = mult + 1
    return(strng)

res = incremental_multiply(1)
print(res)
print(isPandigital(res))

max_pandigital = 0
for num in range(1, 10000):
    prod = incremental_multiply(num)
    if(len(prod) == 9 and isPandigital(prod) and int(prod) > max_pandigital):
        max_pandigital = int(prod)
        print(str(num) + ": " + str(prod))

print(max_pandigital)