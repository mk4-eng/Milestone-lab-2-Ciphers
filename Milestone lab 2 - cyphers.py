
message = []
def caesarEncode(a,b):
    a = int(a) # makes key into an integer 
    for j in b: # for every character in the message 
        if ord(j) >= 65 and ord(j) <= 90: # if character is uppercase
            h = ord(j) - 65 + a % 26 + 65 # moves key # of characters right
            message.append(chr(h)) # adds character to list
        elif ord(j) >= 97 and ord(j) <= 122: # if character is lowercase 
            h = ord(j) - 97 + a % 26 + 97 # moves key # of characters right
            message.append(chr(h)) # adds character to list
        else: # if character is not a letter 
            message.append(j) # adds to list "message" 
    return(message)
    
def caesarDecode(a,b):
    a = int(a)
    for j in b:
        if ord(j) >= 65 and ord(j) <= 90: 
            h = ord(j) - 65 - a % 26 + 65
            message.append(chr(h))
        elif ord(j) >= 97 and ord(j) <= 122:
            h = ord(j) - 97 - a % 26 + 97
            message.append(chr(h))
        else:
            message.append(j)
    return(message)

def vigenereEncode(a,b):
    i = 1

def vigenereDecode(a,b):
    i = 1 

h = 0
code = int(input("Would you like to [1]encode or [2]decode a message\n"))
if code == 1:
    print("encode")
    h += 1 
elif code == 2:
    print("decode")
    h += 2
else: 
    print("invalid option")

cypher = int(input("which cypher do you want to use? \n[1] Caesar\n[2] Vigenere\n"))
if cypher == 1:
    print("Caesar")
    h += 1
elif cypher == 2:
    print("Vigenere")
    h += 3 
else:
    print("invalid number, start again")

key = input("Enter the key: ")
phrase = input("Enter the phrase: ")

if h == 2:
    print(caesarEncode(key, phrase))

elif h == 3:
    print(caesarDecode(key, phrase))

elif h == 4:
    print(vigenereEncode(key, phrase))

else:
    print(vigenereDecode(key, phrase))
















