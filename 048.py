import tools.timer as timer
import math

upper = 1000
digits = 10

t = timer.Timer(verbose=True)

t.start()

def last_digits_of_power(num: int, power: int, digits: int) -> int:

    div = math.pow(10, digits)

    total = num

    for i in range(power - 1):
        total *= num
        total %= div

    return total

total = 0

for i in range(1, upper + 1):
    total += last_digits_of_power(i, i, digits)

t.stop()

print(int(total % math.pow(10, digits)))
