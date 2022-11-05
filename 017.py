def num_to_str(num):

    tens_str = {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    ones_or_hundreds_str = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    teens_str = {
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    written_num = ""
    #this will always exist
    ones = int(str(num)[-1])


    #1000
    if(num == 1000):
        written_num += "one thousand "

    #hundreds
    if(num % 1000 > 99):
        hundreds = int(str(num)[-3])
        written_num += ones_or_hundreds_str.get(int(hundreds), "") + " hundred "
        if(num % 100 != 0):
            written_num += "and "

    #tens
    if(num % 100 > 9):
        tens = int(str(num)[-2])
        tens_and_ones = tens*10 + ones

        #special case for teens
        if(tens_and_ones < 20 and tens_and_ones > 10):
            written_num += teens_str.get(tens_and_ones, "")
            return(written_num)
        else:
            written_num += tens_str.get(tens, "")
        if(ones != 0):
            written_num += "-"

    #ones
    written_num += ones_or_hundreds_str.get(ones, "")

    return(written_num)

max = 1000
total_length = 0
for i in range(1, max+1):    
    written_number = num_to_str(i)
    written_number_trimmed = written_number.replace(" ","").replace("-","")
    length = len(written_number_trimmed)
    print(str(length) + "\t" + written_number_trimmed)
    total_length += length

print(total_length)