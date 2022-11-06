import math

def is_it_prime(x: int) -> bool:
    #validate input
    if not isinstance(x, int):
        raise ValueError

    if x < 2:
        return False

    sq = math.sqrt(x)

    #allows incrementing by 2 through odds only
    if(x % 2 == 0):
        return False

    #divide working number by odds until you reach the sqrt or find a factor
    div = 3
    while(x % div != 0 and div < sq):
        div += 2

    if(div > sq):
        return True
    else:
        return False


def next_prime(x: int) -> int:
    """input an integer, returns the next prime number, NOT including the entered number."""
    #validate input
    if not isinstance(x, int):
        raise ValueError

    y = x + 1

    while(is_it_prime(y) == False):
        y += 1
    
    return y


def append_prime(primes_list: list) -> None:
    prime = primes_list[-1]
    next_prime = numbers.next_prime(prime)
    primes_list.append(next_prime)


def is_it_composite(x: int) -> bool:
    #validate input
    if not isinstance(x, int):
        raise ValueError

    #4 is the smallest composite number
    if x < 4:
        return False

    #handle all even numbers at once
    if x % 2 == 0:
        return True

    #square root provides a logical stopping point
    sq = math.sqrt(x)

    #divide working number by odds until you reach the sqrt or find a factor, start with 3 because 2, and therefore all even numbers, have been ruled out
    divisor = 3
    while(x % divisor != 0 and divisor < sq):
        divisor += 2

    if(divisor > sq):
        return False
    else:
        return True


def next_composite(x: int) -> bool:
    if not isinstance(x, int):
        raise ValueError

    y = x + 1

    while not is_it_composite(y):
        y += 1

    return y


def find_factors(x: int) -> list:
    """returns a list of factors for int x"""
    if not isinstance(x, int) or x < 1:
        raise ValueError

    #upper boundary for factor
    sq = math.sqrt(float(x))

    factors = set()

    for i in range(1, int(sq + 1)):
        if x % i == 0:
            factors.add(i)
            factors.add(int(x / i))

    return factors
    
if __name__ == '__main__':
    for i in range(1,10):
        print(f'{i}: {find_factors(i)}')