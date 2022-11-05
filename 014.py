start = 13

def next_collatz(x):
    if(x % 2 == 0):
        return x//2
    else:
        return x * 3 + 1

def collatz_length(x):
    length = 1
    current = x
    while(current != 1):
        current = next_collatz(current)
        length += 1
    return length

max_length = 0
longest = 0

for i in range(1, 1000000):
    length = collatz_length(i)
    if(length > max_length):
        longest = i
        max_length = length


print(longest)
print(max_length)