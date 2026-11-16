#Milestone lab 2 - Group 4: Ruby Gerard, Maddy Kato, Tholpi Machar (we could not contact Tholpi) 
def caesar(a,b,c):
    message = []
    if c == 2: 
        b = int(b) * -1 # if user wants to decode sets key to negative (shift left)
    elif c == 1:
        b = int(b) # if user wants do encode keeps key as positive (shift right)
    for j in a: # for every character in the message 
        if ord(j) >= 65 and ord(j) <= 90: # if letter is uppercase
            h = (ord(j) - 65 + b) % 26 + 65 # moves key # of characters right
            message.append(chr(h)) # adds letter to list
        elif ord(j) >= 97 and ord(j) <= 122: # if letter is lowercase 
            h = (ord(j) - 97 + b) % 26 + 97 # moves key # of characters right
            message.append(chr(h)) # adds character to list
        else: # if character is not a letter 
            message.append(j) # adds to list "message" 
    return("".join(message))


def vigenere_cipher(msg, key, do='encrypt'): # define function for vigenere cipher
    # define the cipher to have a message, a string key, and to do an encryption or decryption
    result = ""
    j = 0
    key = key.upper() # convert all letters to uppercase
    for ch in msg: # for character in message
        if ch.isalpha(): # check if entry is a letter
            shift = ord(key[j%len(key)])-ord('A') # key shift
            if do == 'decrypt':
                shift = -shift
            if ord(ch) >= 65 and ord(ch) <= 90: # to check if lowercase
                s = chr((ord(ch)- 65 + shift) % 26 + 65)
            elif ord(ch) >= 97 and ord(ch) <= 122: # to check if uppercase
                s = chr((ord(ch)- 97 + shift) % 26 + 97)
            result = result + s
            j = j + 1
        else: 
            result = result + ch
    return result

h = 0
user_choice_type = int(input("1: for Caesar cipher, 2: for Vigenere cipher")) # ask user to choose caesar or vigenere
if user_choice_type == 1: # if user picks caesar
    user_choice_by = int(input("Caesar cipher: 1- to encrypt a message, 2- to decrypt a message"))
    if user_choice_by == 1: # user wants to encrypt with caesar
        print("You have chosen to encrypt a message using a caesar cipher")
        msg = str(input("Add the message: "))
        shift = int(input("shift by: "))
        h += 1
        print(caesar(msg,shift,h)) # call caesar_cipher function, and ask to encrypt
    else: # if user chooses to decrypt using caesar
        print("You have chosen to decrypt a message using a caesar cipher")
        msg = str(input("Add the message: ")) # user defined message
        shift = int(input("shift by: ")) # user defined numerical shift amount
        h += 2
        print(caesar(msg,shift,h)) # call caesar_cipher function, and ask to decrypt

elif user_choice_type == 2: # if user wants to use the vigenere cipher
    code = int(input("Vigenere Cipher: Would you like to [1]encode or [2]decode a message\n"))
    if code == 1: # if user wants to encode a message
        print("encode")
        w = "encoded" # displays in print function in line 74
        do = "encrypt" # sets variable do equal to encrypt
    elif code == 2: # if user wants to decode a message 
        print("decode")
        w = "decoded" # displays in print function in line 74
        do = "decrypt" # sets variable do equal to decrypt
    else: # if user enters number other than 1 or 2
        print("invalid option")
        
    key = input("Enter the key: ") # user enters key used to encrypt/decript
    phrase = input("Enter the phrase: ") #user enters message to encrypt/decrypt
    print(f"Your {w} message is: {vigenere_cipher(phrase, key, do)}") # prints final encoded/decoded message 
