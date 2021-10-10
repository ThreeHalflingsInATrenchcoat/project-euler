import math
from icecream import ic

#must be a positive odd integer
size = 1001

"""
#solution 1: math!

#Find middle of block
mid = (size+1) / 2

#ul to br
ulbr = 0
ulbr_part = 1

#bl to tr
blur = 0
blur_part = 1

for sq in range(0, size):
    #calculate next ulbr block and add to ulbr
    ulbr_part += 2 * sq
    ulbr += ulbr_part

    #same with blur
    blur_part += 4 * math.ceil(sq/2)
    blur += blur_part

    print(sq, ulbr_part, blur_part)

#combined sum, minus 1 for overlapping mid
print(ulbr + blur - 1)
"""


#solution 2, easy math!
num = 1
total = 1

circles = (size - 1) // 2
for i in range(0,circles * 4):
    difference = ((i // 4) + 1) * 2
    num += difference
    total += num

ic(total)