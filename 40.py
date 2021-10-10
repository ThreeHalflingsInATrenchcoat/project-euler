num = 1
fraction = '.'
while len(fraction) < 10000001:
    fraction = fraction + str(num)
    num = num + 1

product = int(fraction[1]) * int(fraction[10]) * int(fraction[100]) * int(fraction[1000]) * int(fraction[10000]) * int(fraction[100000]) * int(fraction[1000000])
print(product)