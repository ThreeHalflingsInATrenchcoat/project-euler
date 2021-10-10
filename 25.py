"""
#this works, but breaks the recursion limit
#iterations = how many fibonacci numbers to generate, iteration = 0, fib_list = []
def fibonacci(iterations, iteration, fib_list):
    #print(fib_list)


    iteration += 1
    if(iteration >= iterations):
        return
    if(iteration <= 2):
        fib_list.append(1)
    else:
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    fibonacci(iterations, iteration, fib_list)
    return fib_list

fibonacci_list = fibonacci(1000000, 0, [])
print(fibonacci_list)
"""


def lowest_fibonacci_of_length(x):
    fib = [1, 1]

    while(len(str(fib[-1])) < x):
        fib.append(fib[-1]+fib[-2])

    return len(fib), fib[-1],

print(lowest_fibonacci_of_length(1000))