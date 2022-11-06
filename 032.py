import itertools, functools, time

start_time = time.time()

digit_min = 1
digit_max = 9

num_list = []
for i in range(digit_min, digit_max + 1):
    num_list.append(i)

iterations = list(itertools.permutations(num_list))

products = []

for iteration in iterations:
    for i in range(1, digit_max - digit_min):
        for j in range(1, digit_max - digit_min - i + 1):
            product = functools.reduce(lambda N, digit: N * 10 + digit, iteration[-i:])
            multiplicand = functools.reduce(lambda N, digit: N * 10 + digit, iteration[-j-i:-i])
            multiplier = functools.reduce(lambda N , digit: N * 10 + digit, iteration[:-j-i])
            # print(f'{multiplier} -- {multiplicand} -- {product}')
            if multiplier * multiplicand == product:
                if product not in products:
                    products.append(product)

products.sort()

stop_time = time.time()
time_elapsed = stop_time - start_time
print(f'{time_elapsed:.2f}')
print(products)
sum_of_products = sum(products)
print(sum_of_products)