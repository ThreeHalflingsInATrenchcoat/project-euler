import math

lower = 1
upper = 10

powerful_digits = []

for multiplier in range(lower, upper):
    power = 1
    while True:
        result = int(math.pow(multiplier, power))
        if len(str(result)) == power:
            powerful_digits.append((f'{multiplier}^{power}', result))
            power += 1
        else:
            break

print(powerful_digits)
print(len(powerful_digits))