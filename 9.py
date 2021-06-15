import math
result = 1000

#loop through a
for a in range(1, 1000):
    #loop through b
    for b in range(a+1,1000):
        c = math.sqrt(a**2+b**2)
        #check if a + b + c is 1000
        sum = a + b + c
        if(sum >= result):
            break
    if(sum == result):
        break

#Check if solution has been found
if(sum == 1000):
    print(a * b * c)
else:
    print("No solution found")