# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
import itertools
import tools.numbers as numbers

# boundaries for problem
lower = 1000
upper = 9999

#generate initial prime, -1 because READ THE FUNCTION DESCRIPTION
primes = [numbers.next_prime(lower - 1)]

#this will always generate one too many primes
while primes[-1] < upper + 1:
    primes.append(numbers.next_prime(primes[-1]))
#So remove the extra prime. This is the lazy way to do this, but it works and is not problematic given the boundaries of the problem.
primes.pop()

primes_groups = []

#convert primes to 
for prime in primes:
    #convert `prime` int to str (iterable), create permutations(list of tuples) 
    prime_perms = list(itertools.permutations(str(prime)))
    for i in range(len(prime_perms)):
        #convert tuples to strings, then back to ints... could be done through math, but this was faster to type and what I thought of first
        prime_perms[i] = int(''.join(prime_perms[i]))
    
    primes_groups.append(prime_perms)

#this was just to verify that the loop wasn't wonky
print(len(primes))
print(len(primes_groups))


# NEXT TIME... ON PROJECT EULER
# Continue the function from lines 23-28. Rather than making a list of all of the permutations of ALL of the primes,
# iterate through the prime_perms lists after they are created, and remove any permutations that are NOT found in `primes`,
# then remove any primes from `primes` that are listed in prime_perms
# I'll be left with groups of primes that are permutations of each other