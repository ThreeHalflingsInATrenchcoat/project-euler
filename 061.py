import math
import copy

def polygonal_number(n, s):
    """returns the `n`th polygonal number of `s` sides"""
    x = ((s - 2) * n * n - (s - 4) * n) / 2
    return int(x)


def is_polygonal_number(n, s):
    """determines if a number is a polygonal number of `s` sides"""
    x = (math.sqrt(8 * (s - 2) * n + (s - 4) ** 2) + (s - 4)) / (2 * (s - 2))
    return x % 1 == 0


def generate_polygonal_number_list(length, sides):
    """generates a list of all of polygonal numbers of `sides` with a length of `length`, numbers presented as strings"""
    p_num_list = []
    n = 1
    while True:
        p_num = polygonal_number(n, sides)
        p_num_length = len(str(p_num))
        if p_num_length == length:
            p_num_list.append(str(p_num))
        elif p_num_length > length:
            return p_num_list
        n += 1

def find_pentagonal_loop(polygonal_numbers: list, found_numbers=list(), required_length=0) -> list:
    """for first run, this should only run once"""
    if found_numbers == []:
        required_length = len(polygonal_numbers)
        first_set = polygonal_numbers.pop(0)
        for number in first_set:
            fn = find_pentagonal_loop(polygonal_numbers, [number],required_length=required_length)
            if fn != None:
                found_numbers = fn 
    #second and further runs
    else:
        last_two = found_numbers[0][-2:]
        for shape in range(len(polygonal_numbers)):
            for p_num in [num for num in polygonal_numbers[shape] if num[:2] == last_two]:
                fn = copy.deepcopy(found_numbers)
                fn.append(p_num)
                first_two = fn[-1][-2:]
                last_two = fn[0][:2]
                if found_numbers[0] == '2556':
                    None
                if len(fn) == required_length:
                    if first_two == last_two:
                        return fn
                    else:
                        return []
                pnums = copy.deepcopy(polygonal_numbers)
                pnums.pop(shape)
                fn = find_pentagonal_loop(pnums, fn, required_length=required_length)
                if fn != None:
                    found_numbers = fn
    try:
        if(len(found_numbers)) == required_length:
            return(found_numbers)        
    except:
        return []


    

#generate number sets
polygonal_number_length = 4
max_number_of_sides = 5
polygonal_numbers = []
for sides in range(3,max_number_of_sides + 1):
    polygonal_numbers.append(generate_polygonal_number_list(polygonal_number_length, sides))

#pentagonal_numbers[0] = ['8128']

#print(polygonal_numbers[0])
print(find_pentagonal_loop(polygonal_numbers))