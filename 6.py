max = 100

#sum = 
sum_of_squares = 0
square_of_sums = (((1 + max) * 100 // 2) ** 2)

for i in range(1, max + 1):
    sum_of_squares += i ** 2

dif = square_of_sums - sum_of_squares

print(dif)