import os

#print(os.path.dirname(__file__))

file = open("42_words.txt",'r')

try:
    words = file.read()
finally:
    file.close()


def triangle_number(x):
    return int((x/2) * (x+1))

def triangle_numbers(mx):
    i = 1
    trinums = []
    trinum = 0
    while trinum < mx:
        trinum = triangle_number(i)
        trinums.append(trinum)
        i = i + 1
    return(trinums)

#requires all capital letters
def wordValue(word):
    val = 0
    for letter in word:
        val = val + ord(letter)-64
    return val

trinums = triangle_numbers(1000)
words = words.replace('"','')
wordlist = words.split(',')

num_words = 0
for word in wordlist:
    if(wordValue(word) in trinums):
        num_words = num_words + 1

print(num_words)