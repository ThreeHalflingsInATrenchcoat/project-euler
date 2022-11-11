expansions = 1000

numerator = 1
denominator = 1

big_num = 0

for i in range(1, expansions + 1):
    previous_denominator = denominator
    denominator += numerator
    numerator = denominator + previous_denominator
    if len(str(numerator)) > len(str(denominator)):
        print(f'{i}: {numerator}/{denominator}')
        big_num += 1

print()
print(f'total: {big_num}')
