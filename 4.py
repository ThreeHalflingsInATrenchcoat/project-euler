#this assumes the problem is solvable

import math

#catscript, thanks Morrigan
#nnnnnnnnnnnnttttttttttthdiuejjjjjjjjjjjjjjjjjjjjjjjjjjj


#number of digits
digits = 3

#calculate highest and lowest multipliers and products
min_mult = int(10 ** (digits - 1))
max_mult = (10 ** digits) - 1
min_prod = min_mult ** 2
max_prod = max_mult ** 2
max_prod_digits = digits * 2

#returns true or false, checks if num is a palindrome
def is_this_a_palindrome(x):
    xS = str(x)
    middle = len(xS) // 2
    if(xS[:middle] == xS[middle:]):
        return True
    else:
        return False

#returns true or false, checks if num is a product of two numbers of digits length
def is_this_a_product(prod):

    #calculate minimum and maximum multiplier for product
    min = prod // int(str("9" * digits))
    if(min >= 10 ** digits):
        return False
    max = prod // (10 ** (digits - 1))
    if(min < 10 ** (digits - 1)):
        min = 10 ** (digits - 1)
    if(max >= 10 ** digits):
        max = int(str("9" * digits))

    #loop through possible multipliers, starting with max and decrementing
    mult = max
    while(mult >= min and prod % mult != 0 and prod / mult <= max):
        mult -= 1

    if(prod % mult == 0):
        return True
    else:
        return False

"""
#increment through numbers to find palindromes, slow but simple and reliable
while(max_prod > min_prod):
    #is_this_a_palindrome(max_prod)
    if(is_this_a_palindrome(max_prod)):
        break
    max_prod -= 1
"""



#given a particular number, it converts all digits to 9 (for a safe palindrome starting point)
pal = int("9" * len(str(max_prod)))
palS = str(pal)
ln = len(str(pal))

#loop through palindromes from max_prod (converted to all nines) to min_prod
while(pal > min_prod and not is_this_a_product(pal)):


    #increment through positions
    for i in reversed(range(0, math.ceil(ln / 2))):
        #print("i: " + str(i)) #Diag
        
        #center digits
        if(i == math.ceil(ln / 2) - 1):
            #if digit is greater than 0
            if(int(palS[i]) != 0):
                if(ln % 2 == 0):
                    sub = 11 * 10 ** i
                else:
                    sub = 10 ** i
                pal -= sub
                palS = str(pal)
                break

        #intermediate digits
        elif(i > 0):
            #if digit is greater than 0
            if(int(palS[i]) != 0):
                sub = 11 * 10 ** i
                pal -= sub
                palS = str(pal)
                break
        
        #first/last digits
        else:
            #if digit is greater than 1
            if(int(palS[i]) != 1):
                sub = 11 * 10 ** i
                pal -= sub
                palS = str(pal)
            else:
                pal -= 2
                palS = str(pal)
                ln -= 1

print(pal)


#Not my code, placed here for later reference. Quick to write, slow to execute.
"""
def find_palindrome():
  palindromes = []
  for x in range(999, 100, -1):
    for y in range(999, 100, -1):
      num = x * y
      num_as_string = str(num)
      middle = len(num_as_string) // 2
      if num_as_string[:middle] == num_as_string[middle:][::-1]:
        palindromes.append(num)
  return max(palindromes)
print(find_palindrome())
"""