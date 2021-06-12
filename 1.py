#input("Please enter maximum number")
min = 0
max = 1000
total = 0
divisor_1 = 3
divisor_2 = 5
overlap = divisor_1 * divisor_2

"""
#Brute Force
for i in range(min, max):
    if (i % divisor_1 == 0 or i % divisor_2 == 0):
        total += i
print("Brute Force")
print(total)
print("")
"""

#Find highest and lowest divisible numbers within min and max
i = min
while i % divisor_1 != 0:
    i += 1
divisor_1_min = i

i = max - 1
while i % divisor_1 != 0:
    i -= 1
divisor_1_max = i

i = min
while i % divisor_2 != 0:
    i += 1
divisor_2_min = i

i = max - 1
while i % divisor_2 != 0:
    i -= 1
divisor_2_max = i

i = min
while i % overlap != 0:
    i += 1
overlap_min = i

i = max - 1
while i % overlap != 0:
    i -= 1
overlap_max = i

#Compute totals of Divisor 1 and 2
divisor_1_count = (divisor_1_max - divisor_1_min) // divisor_1 + 1
divisor_1_total = (divisor_1_max + divisor_1_min) * divisor_1_count // 2

divisor_2_count = (divisor_2_max - divisor_2_min) // divisor_2 + 1
divisor_2_total = (divisor_2_max + divisor_2_min) * divisor_2_count // 2

#Subtract total of repeated values
overlap_count = (overlap_max - overlap_min) // overlap + 1
overlap_total = (overlap_max + overlap_min) * overlap_count // 2

#Print Results

print(divisor_1_total + divisor_2_total - overlap_total)