fibonacci = [1, 2]
max = fibonacci[len(fibonacci) - 1]
while (fibonacci[-1] + fibonacci[-2] < 4000000):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)

total = 0
for i in fibonacci:
    if(i % 2 == 0):
        total += i

print(total)