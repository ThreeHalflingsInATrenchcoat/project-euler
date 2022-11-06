# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?
import tools.numbers as numbers
import tools.timer as timer

upper = 1000000

t = timer.Timer(verbose=True)
t.start()

primes = [2]
while primes[-1] < upper:
    primes.append(numbers.next_prime(primes[-1]))
primes.pop()

#print(f'all primes: {primes}')

consecutive_primes = []

total = 0
max_possible_consecutive_primes = 0

#create max limit for consecutive length
for prime in primes:
    if total + prime < primes[-1]:
        consecutive_primes.append(prime)
        max_possible_consecutive_primes += 1
        total += prime
    else:
        break
#print(f'consecutive_primes: {consecutive_primes}')
print(f'max length: {max_possible_consecutive_primes}')
print(f'sum: {sum(consecutive_primes)}')
print()

max_consecutive_primes = 0
done = False

#number of consequtive primes to search for
for i in reversed(range(max_possible_consecutive_primes + 1)):
    print(i)
    t.lap()
    #starting position, iterating up to primes[-j]
    for j in reversed(range(len(primes)-i)):
        top = primes[j+i]
        total = sum(primes[j:j+i])
        consecutive_primes = primes[j:j+i]
        if total > primes[-1]:
            continue
        elif total in primes:
            print(total, consecutive_primes)
            done = True
            break
    if done:
        break


#print(f'top; {top}')
#print(f'consecutive primes: {consecutive_primes}')

# for i in range(1, len(primes)):
#     target_sum = primes[i]
#     for j in range(i):
#         total = 0
#         num_consecutive_primes = 0
#         while total < target_sum:
#             total += primes[j + num_consecutive_primes]
#             num_consecutive_primes += 1
        
#         if total == target_sum and num_consecutive_primes > max_consecutive_primes:
#             max_consecutive_primes = num_consecutive_primes
#             consecutive_primes = primes[j:j+num_consecutive_primes]

# print(f'{consecutive_primes} : {max_consecutive_primes} : {sum(consecutive_primes)}')

t.stop()

#This code works for under 100 and under 1000, but gets really, really slow starting at 100000
# this took about a minute, and was exponentially longer than the run for 10000, less than a second
#it should be rewritten to search for the sums of the largest possible sequence of primes
#incrementing down until the solution is found