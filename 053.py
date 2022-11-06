import math

def combinatorics(x: int, y: int) -> int:
    """returns number of possible combinations of x selections from y objects
    
    Args:
        x: total objects in set
        y: number of objects to be selected
    """
    numerator = math.factorial(x)
    denominator = math.factorial(y) * math.factorial(x - y)
    return int(numerator / denominator)

print(combinatorics(5, 3))

million_count = 0

for x in range(1, 101):
    for y in range(1, x + 1):
        combinations = combinatorics(x, y)
        if combinations > 1000000:
            million_count += 1

print(million_count)