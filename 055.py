import tools.timer as timer

def is_palindrome(a):
    a = str(a)
    middle = len(a) // 2
    left = a[:middle]
    right = a[:-middle-1:-1]
    return left == right


def reverse_number(x):
    x = str(x)
    x = x[::-1]
    return int(x)


def lychrel_iteration(x):
    rev = reverse_number(x)
    return x + rev


def is_lychrel(number, max_iterations):
    total = number
    for i in range(max_iterations):
        total = lychrel_iteration(total)
        if is_palindrome(total):
            return(False)
    return(True)


max_iterations = 50
max_number = 9999
lychrel_number_count = 0

t = timer.Timer(verbose=True)
t.start()

for number in range(1, max_number + 1):
    if is_lychrel(number, max_iterations):
        lychrel_number_count += 1
        print(number)

t.stop()

print(lychrel_number_count)