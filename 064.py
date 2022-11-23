import tools.timer as timer
import math

t = timer.Timer(verbose=True)
t.start()

def continued_fraction(number):
    mn = 0.0
    dn = 1.0
    a0 = int(math.sqrt(number))
    an = int(math.sqrt(number))
    cf_list = []
    if a0 != math.sqrt(number):
        while an != 2*a0:
            mn = dn * an - mn
            dn = (number - mn**2) / dn
            an = int((a0 + mn) / dn)
            cf_list.append(an)
    return cf_list

print(continued_fraction(23))

odd_period = 0
for i in range(2, 10001):
    if len(continued_fraction(i)) %2 == 1:
        odd_period += 1

print(odd_period)

t.stop()