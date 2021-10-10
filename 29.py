min = 2
max = 100

products = []

for a in range(min, max+1):
    for b in range(min, max+1):
        prod = a**b
        if(prod not in products):
            products.append(prod)

products.sort()

print(len(products))