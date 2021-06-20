number_of_digits = 9
permutations = 1000000

digit_list = []

for i in range(0, number_of_digits + 1):
    digit_list.append(i)

remaining_digits = []

#loop through characters in current string, starting at the end
#print(len(digit_list)-1)
for count in range(0,permutations-1):
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

digit_str = ""
for digit in digit_list:
    digit_str += str(digit)

print(digit_str)