import time
import math
from types import TracebackType

start_time = time.time()

p_max = 1000

triangles = set()

for a in range(1, p_max):
    #print(a)
    for b in range(1, p_max):
        #print(b)
        c = math.sqrt(a * a + b * b)
        p = a + b + c
        if(p > p_max):
            break
        if(c % 1 == 0):
            c = int(c)
            p = int(p)
            srtd = sorted([a, b, c, p])
            triangles.add(tuple(srtd))

perimeters = {}
for triangle in triangles:
    perimeters[triangle[3]] = perimeters.get(triangle[3], 0) + 1
    
p_common = max(perimeters, key=perimeters.get)

print(p_common, perimeters[p_common])

print("time: ", time.time() - start_time)