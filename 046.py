# I like to create useful functions, put them in a tools folder, then call them as though they were modules
# Don't judge me
import tools.numbers as numbers
import tools.timer as timer
import math

#9 is the smallest odd composite number
composite_number = 9
primes = [2]
twice_squares = [2]

def append_prime(primes_list: list) -> None:
    prime = primes_list[-1]
    next_prime = numbers.next_prime(prime)
    primes_list.append(next_prime)


def append_twice_square(squares_list: list) -> None:
    square_x2 = squares_list[-1]
    square = square_x2 / 2
    square_root = math.sqrt(square)
    next_square_root = square_root + 1
    next_square = math.pow(next_square_root, 2)
    squares_list.append(int(next_square * 2))


def test_goldbach(x: int) -> bool:
    """returns True if his conjecture works, False if it does not"""
    # -2 because that's the smallest possible prime
    while primes[-1] < x - 2:
        append_prime(primes)
    
    # -2 because that's the smallest possible twice_square
    while twice_squares[-1] < x - 2:
        append_twice_square(twice_squares)
    
    # print(primes)
    # print(twice_squares)

    for prime in primes:
        for twice_square in twice_squares:
            if x == prime + twice_square:
                return True
            # elif x < prime + twice_square:
            #     break
    
    #all options have run out
    return False

t = timer.Timer()

t.start()

while test_goldbach(composite_number) or composite_number % 2 == 0:
    composite_number = numbers.next_composite(composite_number)

print(composite_number)

t.stop()
t.report()