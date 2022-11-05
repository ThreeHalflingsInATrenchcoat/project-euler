import math

lowest = 1
highest = 10000

#generates pentagonal numbers
def generate_pentagonal(n):
    pent = n * (3 * n - 1 ) / 2
    return int(pent)

#determines if number is pentagonal
def is_pentagonal(n):
    pent = (1 + math.sqrt(24 * n + 1)) / 6
    is_pent = pent % 1 == 0
    return is_pent

minimized = 1000000000000
min_j = 0
min_k = 0

for k in range(lowest, highest + 1):
    for j in range(lowest, k):
        j_pent = generate_pentagonal(j)
        k_pent = generate_pentagonal(k)
        pent_sum = j_pent + k_pent
        pent_diff = abs(j_pent - k_pent)
        if is_pentagonal(pent_sum) and is_pentagonal(abs(pent_diff)):
            if pent_diff < minimized:
                minimized = pent_diff
                min_j = j
                min_k = k

print(f"minimized: {minimized}\nmin_j: {min_j}\nmin_k: {min_k}")
