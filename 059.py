import tools.timer as timer

t = timer.Timer(verbose=True)
t.start()

def filter_decryption(decryption, decryption_length, common_words, space_percentage):
    #check for spaces
    if decryption.count(' ') > decryption_length / space_percentage:
    #check for common words
        for word in common_words:
            if word in decryption:
                return True
    return False

common_words = ['the', 'from']
space_percentage = 10

with open('059_cipher.txt', 'r', encoding='utf_8') as f:
    message = f.readline().strip()

#convert to array of ints
message = [int(c) for c in message.split(',')]
message_length = len(message)
decrypted = ''
response = ''

#a = 97
#z = 122
#generate encryption keys
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            decryption = []
            key = (a,b,c)
            
            #convert numbers to chars
            for i in range(message_length):
                decryption.append(chr(message[i] ^ key[i % 3]))
            
            #convert to string
            decryption = ''.join(decryption)

            #run initial checks before manual revision
            if filter_decryption(decryption, message_length, common_words, space_percentage):
                print(key)
                print(decryption)
                response = input("Type something if this decryption is correct.")
                break
            if response != '': break
        if response != '': break
    if response != '': break

decryption = [ord(char) for char in decryption]

print(sum(decryption))