from icecream import ic

min = 2**5 * 5
max = 9**5 * 5


fifths = []
total_sum = 0

for i in range(min, max+1):
    sum = 0
    for num in str(i):
        sum += int(num)**5
    
    if(i == sum):
        ic(i)
        total_sum += sum

ic(total_sum)