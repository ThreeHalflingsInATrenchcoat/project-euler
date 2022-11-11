import tools.numbers as numbers
import tools.timer as timer

t = timer.Timer(verbose=True)
t.start()

number_of_circles = 3 #does not include center point

total_numbers = 1
primes = 0
number = 1
increment = 0

while True:
    increment += 2
    total_numbers = increment * 2 + 1

    for i in range(1,5):
        number += increment
        if numbers.is_it_prime(number):
            primes += 1

    if primes / total_numbers < .1:
        break

side_length = increment + 1

print(f'{side_length} - {round(primes/total_numbers, 2)} - {primes}/{total_numbers}')

t.stop()