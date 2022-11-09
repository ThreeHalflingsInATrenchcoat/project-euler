import time

start_time = time.time()

#Brute Force
"""
ways = 0
for a in range(201):
    if (a*1) > 200:
        break
    for b in range(101):
        if(a+b*2) > 200:
            break
        for c in range(41):
            if(a+b*2+c*5)>200:
                break
            for d in range(21):
                if(a+b*2+c*5+d*10) > 200:
                    break
                for e in range(11):
                    if(a+b*2+c*5+d*10+e*20) > 200:
                        break
                    for f in range(5):
                        if(a+b*2+c*5+d*10+e*20+f*50) > 200:
                            break
                        for g in range(3):
                            if(a+b*2+c*5+d*10+e*20+f*50+g*100) > 200:
                                break
                            for h in range(2):
                                if (a*1+b*2+c*5+d*10+e*20+f*50+g*100+h*200) == 200:
                                    ways += 1
print(ways)
print(time.time() - start_time)
"""
#Dynamic Programming
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0]*(target+1)
ways[0] = 1 #this is just to make the math work, if I'm trying to figure out how many ways to make 50 cents from a 50 cent coin, we won't have a value from zero to reference, so default to 1
print(f's: {ways}')
for coin in coins:
    for i in range(coin,target+1):
        # ways[i] = how many ways have we found for this number already + how many ways can we make this number - the coin value?
        # add however many ways we can make this number to however many ways we can make (this number - coin value)
        ways[i] = ways[i] + ways[i-coin]
    print(f'{coin}: {ways[:50]}')
print(ways)
print(ways[-1])