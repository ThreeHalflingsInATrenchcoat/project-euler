# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
# Total execution time was 91 seconds. This is not optimal.


import tools.numbers as numbers
import tools.timer as timer

#create an array of primes because these are computationally expensive
primes = [2]
consecutive_numbers = []
test_num = 1
num_of_factors = 4

t = timer.Timer(verbose=True)

t.start()


while len(consecutive_numbers) < num_of_factors:

    # if test_num % 10000 == 0:
    #     print(test_num)

    if primes[-1] < test_num:
        primes.append(numbers.next_prime(primes[-1]))

    factors = numbers.find_factors(test_num)

    prime_factors = []

    for factor in factors:
        if factor in primes:
            prime_factors.append(factor)

    if len(prime_factors) >= num_of_factors:
        consecutive_numbers.append((test_num, prime_factors))
    else:
        consecutive_numbers = []

    test_num += 1

t.stop()

for i in (consecutive_numbers):
    print(f'{i[0]}:\t{i[1]}')

print()

print(consecutive_numbers[0][0])
# print(consecutive_numbers)
