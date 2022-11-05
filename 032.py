import math
#from icecream import ic

digit_min = 1
digit_max = 9
possible_permutations = math.factorial(digit_max - digit_min + 1)
print(possible_permutations)
permutations = []
products = []

digit_list = []
for i in range(digit_min, digit_max + 1):
    digit_list.append(i)

remaining_digits = []

def listToInt(lst):
    lst_str = ''.join([str(x) for x in lst])
    lst_int = int(lst_str)
    return lst_int

first = []
for i in range(digit_min, digit_max+1):
    first.append(i)

permutations.append(first)
#loop through characters in current string, starting at the end
#print(len(digit_list)-1)
for count in range(1,possible_permutations):
    for i in reversed(range(0, len(digit_list)-1)):
        first = digit_list[i]
        second = digit_list[i+1]

        #look for a pair of digits, left < right
        if(first<second):

            #select digits starting at left digit found above to end and sort them
            affected_digits = digit_list[i:]
            affected_digits.sort()

            #find index of left digit, bump it up to the next available digit in the sorted string
            index = affected_digits.index(first)
            increment = affected_digits[index+1]

            #remove incremented digit from sorted list
            affected_digits.remove(increment)

            #create new list in this order: untouched digits, incremented digit, remainder sorted in ascending order
            digit_list = digit_list[:i]
            digit_list.append(increment)
            digit_list = digit_list + affected_digits
            #print(str(count+2) + "\t" + str(digit_list))  #diagnostic

            break
    permutations.append(digit_list)

digit_str = ""
for digit in digit_list:
    digit_str += str(digit)

#ic(digit_str)
#ic(len(permutations))
#ic("")

#loop through permutations
for permutation in permutations:
    #ic(permutation)
    #loop through possible products
    for prod_i in range(0, digit_max - digit_min - 1):
        prod = permutation[digit_max - prod_i - 1:digit_max - digit_min + 1]
        prod_int = listToInt(prod)
        #ic(prod)
        #ic(prod_str)
        #ic(prod_int)

        #loop through possible multipliers
        for mult in range(1, digit_max - len(prod)):
            #ic(permutation[:mult])
            m1 = permutation[:mult]
            m1_int = listToInt(m1)
            
            m2 = permutation[mult:-len(prod)]
            m2_int = listToInt(m2)

            if(m1_int * m2_int == prod_int):
                #ic(m1_int, m2_int, prod_int)
                if(prod_int not in products):
                    products.append(prod_int)

print(products)
products.sort()

print(sum(products))
