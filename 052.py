import itertools
import tools.timer as timer

def generate_int_permutations(num: int) -> list:
    """generates all unique permutations of int `num`
    
    Args:
        num: a positive integer
    
    Returns:
        a set of integer permutations of `num`
    """
    perms = list(itertools.permutations(str(num)))
    
    for i in range(len(perms)):
        perm = perms[i]
        perm = int(''.join(perm))
        perms[i] = perm
    
    return set(perms)

lower = 1
upper = 999999
current = lower
target_products = 6

t = timer.Timer(verbose=True)
t.start()

while current <= upper:
    products = {current}
    for i in range(2, target_products + 1):
        products.add(current * i)

    perms = generate_int_permutations(current)

    if products.issubset(perms):
        print(sorted(products))
        break

    current += 1

t.stop()