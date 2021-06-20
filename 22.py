import os

print(os.path.dirname(__file__))

file = open("22_names.txt",'r')

try:
    names = file.read()
finally:
    file.close()



#remove quotes
names = names.replace('"','')
#split into list
names = names.split(',')
#sort list
names.sort()

total = 0
order = 0

#loop through names
for name in names:
    #loop through letters
    alpha_value = 0
    for letter in name:
#        print(letter)
        alpha_value += ord(letter)-64
    order += 1
    name_score = order * alpha_value
#    print(name_score)
    total += name_score

print(total)