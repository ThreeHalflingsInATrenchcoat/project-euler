from itertools import permutations

weird_nums = []

primes = [2, 3, 5, 7, 11, 13, 17]
numbers = [0,1,2,3,4,5,6,7,8,9]
perms = permutations(numbers)

#perm = (1,4,0,6,3,5,7,2,8,9)

for perm in list(perms):
    for d in range(1,8):
        #print(d)
        if((100 * perm[d] + 10 * perm[d+1] + perm[d+2]) % primes[d-1] != 0):
            break
        elif(d==7):
            weird_nums.append(perm)
        
total = 0
for weird in weird_nums:
    total += int(''.join(str(d) for d in weird))
    #print(total)

print(total)