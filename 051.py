# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

from math import pow
from tools.numbers import next_prime
from tools.timer import Timer
from itertools import permutations

def create_replacement_pattern(num_length: int) -> list:
    """creates replacement patterns to replace all variations of num_length-1 characters in a string
    1 indicates the character should be replaced
    0 indicates the character should not be replaced
    
    Args:
        num_length: the length of the pattern you are generating

    Returns:
        a list of tuple patterns
    """
    patterns = []
    for i in range(1, num_length):
        template = [1] * i + [0] * (num_length - i)
        perms = list(set(permutations(template)))
        patterns += perms
    
    return patterns

def update_primes_list(primes_list, length: int) -> list:
    
    plist = primes_list
    """extends a list of primes up to `length` digits

    Args:
        primes_list: a list of consecutive primes in ascending order -- THIS IS NOT VALIDATED
    
    Returns:
        `primes_list` with all further consecutive primes up to and including `length` digits

    Raises:
        None, because this is Project Euler and I'll probably never use this function again
    """
    upper_limit = pow(10, length)
    while plist[-1] < upper_limit:
        prime = next_prime(plist[-1])
        plist.append(prime)

    plist.pop()

    return plist

def replace_digit(num: int, place: int, replacement: int) -> int:
    """replaces digit in `num` at `place` with `replacement_digit`
    
    Args:
        num: number to have a digit replaced
        place: the place of the digit to be replaced (starting from zero, left to right)
        replacement_digit: the new digit to put in its place

    Returns:
        the modified `num` 
    """
    digits = len(str(num))
    up = num - num % pow(10, digits - place)
    down = num % pow(10, digits - 1 - place)
    mid = replacement * pow(10, digits - 1 - place)
    total = int(up + mid + down)

    return total

def pattern_replace(num: int, pattern: tuple, replacement: int) -> int:
    """replaces digits in `num` with `replacement` according to `pattern`
    
    Args:
        num: the number to have digits replaced
        pattern: a tuple of 1s and 0s, 1 indicates replace the number, 0 indicates do nothing
        replacement: the digit to be inserted

    Returns:
        an int with the specified digits replaced
    """

    working_num = num
    digits = len(str(num))

    for i in range(digits):
        if pattern[i] == 1:
            working_num = replace_digit(working_num, i, replacement)

    return working_num

t = Timer(verbose=True)
t.start()

#upper and lower boundaries for testing
lower = 10
#upper = 56010

#get first prime starting at lower boundary
primes_list = [next_prime(lower-1)]
primes_list = update_primes_list(primes_list, len(str(primes_list[-1])))
#for faster searching
primes_set = set(primes_list)
current_prime = primes_list[0]

replacement_patterns = {}

max_variations = 0

while max_variations < 8:
    #create another variable so I can math with it
    num_digits = len(str(current_prime))

    #get replacement patterns, create and store them if they don't yet exist
    if num_digits not in replacement_patterns:
        replacement_patterns[num_digits] = create_replacement_pattern(num_digits)
    patterns = replacement_patterns[num_digits]

    #check enough primes have been created
    max_generated_prime = primes_list[-1]
    if len(str(max_generated_prime)) < num_digits:
        primes_list = update_primes_list(primes_list, num_digits)
        primes_set = set(primes_list)

#    print(f'{current_prime}: {replacement_patterns[num_digits]}')

    max_family_size = 0
    prime_family = []

    for pattern in patterns:
        variations = []
        for replacement_digit in range(10):
            if pattern[0] == 1 and replacement_digit == 0:
                continue
            variation = pattern_replace(current_prime, pattern, replacement_digit)
            if variation in primes_set:
                variations.append(variation)

        total_variations = len(variations)

        if total_variations > max_variations:
            max_variations = total_variations
            print(f'prime: {current_prime}')
            print(f'pattern: {pattern}')
            print(f'variations: {total_variations} - {variations}')
            print()
            t.lap()
            print()

    #create next prime and continue
    current_prime = next_prime(current_prime)

t.stop()