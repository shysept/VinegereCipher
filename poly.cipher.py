# -*- coding: utf-8 -*-
"""

@author: Melissa Milli
"""

#This program takes your encryption Key and encryps your message using the key given to you. This is called Vigenère Cipher.
plaintext_message= "canyoumeetmeatmidnightihavethegoods"
print("Please input your encryption key:")
encryption_key=input()
cipher=""
alphabet="abcdefghijklmnopqrstuvwxyz123456789.,?"
#turns all the inputs into lowercase
plaintext_message = plaintext_message.lower()
encryption_key=encryption_key.lower()
cipher = cipher.lower()
print("Encryption key:",encryption_key,"\nPlaintext message:",plaintext_message)
print ("Length of the encryption key:",len(encryption_key),"\nLength of the plaintext:",len(plaintext_message))

#checks if plaintext length matches the key if not repeats and adds the remainder to match the length
if len(plaintext_message) != len(encryption_key):
    x=len(plaintext_message)/len(encryption_key) #how many times encryption key needs to be repeated
    y=len(plaintext_message)%len(encryption_key) #check how much more string needs to be added after repeated
    encryption_key=(encryption_key*int(x))+(encryption_key[0:y]) #turns encyription key to be same length as plaintext for conversion
    pass


i=0
for a in plaintext_message:
    c=encryption_key[i]  #c is the next key letter to change in the encryption
    i=i+1 #increments encyription key so it switches to next letter
    d=alphabet.index(c) #looks up where the current encryption key letter is located in the alphabet
    #print("\n\nencryption list order",c,"the order of key",i,"where the next encription key located in alphabet",d) this part was used to check c,i,d values
    position=alphabet.index(a)  # checks where is the current letter located in the alphabet
    deque=collections.deque(alphabet)  #turns alphabet string into an array
    deque.rotate(-d) #it shifts the deque to match the row where the encrpytion key is located
   # print("deque",deque) this was used to check the current row in the vinegere chart

 #checks the location of the original letter in the shifted vinegere row, return value is added top on eachother until the loop ends
    cipher=cipher+deque[position]
    pass

print("Ciphertext:",cipher) 


k=input("press any button to exit") 