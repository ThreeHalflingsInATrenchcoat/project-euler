from decimal import *
import tools.timer as timer
import math

def sum_digits(x: int):
    """returns sum of digits in int or decimal `x`"""
    total = 0

    while x > 0:
        total += x % 10
        x //= 10

    return total


def precise_pow(number, power):
    """does power calculation on Decimal type numbers, returns a decimal, bound by getcontext().prec, so set that first
    
    Args:
        number: the number to be multiplied
        power: the power to raise it to, int type

    Returns:
        a Decimal type number
    """
    number = Decimal(number)

    if power == 0:
        return Decimal(1)
    else:
        total = number
        for i in range(1, power):
            total *= number

    return total


lower = 1
upper = 100

max_length = len(str(Decimal(math.pow(100,100))))
getcontext().prec = max_length + 2

max_number = 0
max_digit_sum = 0
max_digit_sum_multipliers = ()

t = timer.Timer(verbose=True)
t.start()

for a in range(lower, upper + 1):
    for b in range(lower, upper + 1):
        prod = precise_pow(a,b)
        digit_sum = sum_digits(prod)
        # print(f'{a}^{b}: {prod}')
        # print(f'digit_sum: {digit_sum}')
        # print()

        if digit_sum > max_digit_sum:
            max_number = prod
            max_digit_sum = digit_sum
            max_digit_sum_multipliers = (a, b)

t.stop()

print(f'max_digit_sum: {max_digit_sum}, {max_digit_sum_multipliers}')
print(max_number)

print()