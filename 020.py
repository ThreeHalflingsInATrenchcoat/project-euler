import math
#easy way
print(sum([int(d) for d in str(math.factorial(100))]))

#slightly less easy way
factorial = 1
for i in range(1,101):
    factorial = factorial * i
print(sum([int(d) for d in str(factorial)]))