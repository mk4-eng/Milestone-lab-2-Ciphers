#Milestone lab 2 - Group 4: Ruby Gerard, Maddy Kato, Tholpi Machar (we could not contact Tholpi) 
message = []
def caesar(a,b,c):
    if c == 2: 
        a = int(a) * -1 # if user wants to decode sets key to negative (shift left)
    elif c == 1:
        a = int(a) # if user wants do encode keeps key as positive (shift right)
    for j in b: # for every character in the message 
        if ord(j) >= 65 and ord(j) <= 90: # if character is uppercase
            h = (ord(j) - 65 + a) % 26 + 65 # moves key # of characters right
            message.append(chr(h)) # adds character to list
        elif ord(j) >= 97 and ord(j) <= 122: # if character is lowercase 
            h = (ord(j) - 97 + a) % 26 + 97 # moves key # of characters right
            message.append(chr(h)) # adds character to list
        else: # if character is not a letter 
            message.append(j) # adds to list "message" 
    return("".join(message))
    

def vigenere(a, b, c):
    e = len(a)
    d = 0
    for j in b: # for each letter in the encoded/decoded message 
        t = ord(a[d % e]) # finds 
        if t >= 65 and t <= 90: # finds number to shift by if uppercase
            t = t - 65 
        elif t >= 97 and t <= 122:# finds number to shift by if lowercase
            t = t - 97
        if c == 2:
            t = t * -1 # if user wants to decode sets key to negative (shift left)
        elif c == 1:
            t = t # if user wants do encode keeps key as positive (shift right)
        if ord(j) >= 65 and ord(j) <= 90: # if character in message is uppercase
            h = (ord(j) - 65 + t) % 26 + 65 # shifts by the key
            message.append(chr(h)) 
            d += 1 # goes to the next letter in the key
        elif ord(j) >= 97 and ord(j) <= 122: # if character in message is lowercase
            h = (ord(j) - 97 + t) % 26 + 97 # shifts by the key
            message.append(chr(h))
            d += 1 # goes to the next letter in the key
        else: # if the character is not a letter 
            message.append(j) # adds to message without changing it 
    return("".join(message))


h = 0
g = 0
code = int(input("Would you like to [1]encode or [2]decode a message\n"))
if code == 1:
    print("encode")
    w = "encoded"
    h += 1 
elif code == 2:
    print("decode")
    w = "decoded"
    h += 2
else: # if user enters number other than 1 or 2
    print("invalid option")

    
cypher = int(input("which cypher do you want to use? \n[1] Caesar\n[2] Vigenere\n"))
if cypher == 1:
    print("Caesar")
    g += 1
elif cypher == 2:
    print("Vigenere")
    g += 2 
else: # if user enters number other than 1 or 2
    print("invalid number")


key = input("Enter the key: ")
phrase = input("Enter the phrase: ")


if g == 1:
    print(f"Your {w} message is: {caesar(key, phrase, h)}")
elif g == 2:
    print(f"Your {w} message is: {vigenere(key, phrase, h)}")

