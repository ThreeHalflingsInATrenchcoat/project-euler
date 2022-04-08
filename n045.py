import math

lowest = 286

#determines if a number is triangular
def is_triangular(n):
    if (n < 0):
        return False
 
    # Considering the equation n*(n+1)/2 = num
    # The equation is : a(n^2) + bn + c = 0
    c = (-2 * n)
    b, a = 1, 1
    d = (b * b) - (4 * a * c)
 
    if (d < 0):
        return False
 
    # Find roots of equation
    root1 = ( -b + math.sqrt(d)) / (2 * a)
    root2 = ( -b - math.sqrt(d)) / (2 * a)
 
    # checking if root1 is natural
    if (root1 > 0 and math.floor(root1) == root1):
        return True
 
    # checking if root2 is natural
    if (root2 > 0 and math.floor(root2) == root2):
        return True
 
    return False

#generates pentagonal numbers
def generate_pentagonal(n):
    pent = n * (3 * n - 1 ) / 2
    return int(pent)

#generates triangular numbers
def generate_triangular(n):
    tri = n * (n + 1) / 2
    return tri

#determines if number is pentagonal
def is_pentagonal(n):
    pent = (1 + math.sqrt(24 * n + 1)) / 6
    is_pent = pent % 1 == 0
    return is_pent

#determines if a number is hexagonal
def is_hexagonal(n):
    val = 8 * n + 1
    x = 1 + math.sqrt(val)
 
    # Calculate the value for n
    n = x / 4
 
    # Check if n - floor(n)
    # is equal to 0
    if ((n - int(n)) == 0):
        return True
    else:
        return False

current = lowest
while True:
    tri_num = generate_triangular(current)
    if is_pentagonal(tri_num) and is_hexagonal(tri_num):
        print(tri_num)
        break
    current += 1
