# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

import tools.timer as timer
import itertools
import tools.numbers as numbers

# boundaries for problem
lower = 1000
upper = 9999

t = timer.Timer(verbose=True)
t.start()

#generate initial prime, -1 because READ THE FUNCTION DESCRIPTION
primes = [numbers.next_prime(lower - 1)]

#this will always generate one too many primes
while primes[-1] < upper + 1:
    primes.append(numbers.next_prime(primes[-1]))
#So remove the extra prime. This is the lazy way to do this, but it works and is not problematic given the boundaries of the problem.
primes.pop()

primes_groups = []

while len(primes) > 0:    
    #grab a prime
    prime = primes[-1]
    #create prime permutations
    prime_perms = list(itertools.permutations(str(prime)))
    #convert permutations back to ints
    for i in range(len(prime_perms)):
        prime_perms[i] = int(''.join(prime_perms[i]))

    primes_group = []

    #find primes that match permutations and add to group
    for prime_perm in prime_perms:
        if prime_perm in primes:
            primes_group.append(primes.pop(primes.index(prime_perm)))

    #add group only if it contains the minimum necessary number of primes
    if len(prime_perms) >= 3:
        primes_groups.append(primes_group)

#sort groups for easy mathing
for primes_group in primes_groups:
    primes_group.sort()

for primes_group in primes_groups:
    for i in range(len(primes_group)-2):
        first = primes_group[i]
        for j in range(i + 1, len(primes_group)-1):
            second = primes_group[j]
            diff = second - first
            third = second + diff
            if third in primes_group:
                print(first, second, third, sep=', ')

t.stop()