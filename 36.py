import math

max = 999999

dbpal = []

#recursion, input integer, output binary as int
"""
def decToBin(num):
    if num == 0:
        return 0
    else:
        return(num % 2 + 10 * decToBin(int(num // 2)))
"""

#built-in binary function
def decToBin(num):
    return bin(num)[2:]

#requires an integer, returns true or false
def is_this_a_palindrome(x):
    if(int(x) < 10):
        return True
    else:
        xS = str(x)
        middle = len(xS) // 2
        if(xS[-middle:] == xS[:middle][::-1]):
            return True
        else:
            return False

for i in range(1,max+1):
    if is_this_a_palindrome(i):
        if(is_this_a_palindrome(decToBin(i))):
            dbpal.append(i)

print(dbpal)

print(sum(dbpal))