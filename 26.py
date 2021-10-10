from icecream import ic

#first remainder is calculated from num % den
#following remainders are calculated as rem * 10 % den
#results are calculated as rem * 10 // den

#numr = 1
#demr = 7

def find_repeating(numr, denr):

    #initialize decimal string
    res = ""

    #initialize map of remainders & positions
    mp = {}
    
    #get first remainder
    rem = numr % denr
    
    #loop until you find a repeating remainder or the remainder is zero
    while((rem != 0) and (rem not in mp)):
        #store current remainder with value of current position (derived from length of res)
        mp[rem] = len(res)

        #get next part of the result
        res_part = rem * 10 // denr
        #add result to decimal string
        res += str(res_part)

        #get next remainder
        rem = rem * 10 % denr

    if (rem == 0): 
        return ""
    else:
        return res[mp[rem]:]

def repeating_length(numr, demr):
    res = find_repeating(numr, demr)
    return len(res)

ic(repeating_length(1,1))

max_length = 0
max_number = 0

for i in range(1, 1000):
    length = repeating_length(1,i)
    if(length > max_length):
        max_length = length
        max_number = i

ic(max_length)
ic(max_number)