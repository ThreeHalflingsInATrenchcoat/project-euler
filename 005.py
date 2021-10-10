#Other than incrementing by the max at line 16, I have NO IDEA how I would even start to optimize this

max = 20

def is_it_divisible(x):
    for i in range(1,max+1):
        if(x % i != 0):
            return False
    return True

num = max
while(True):
    if(is_it_divisible(num)):
        break
    else:
        num += max

print(num)
