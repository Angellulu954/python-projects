import random 
import string 
chars=" "+string.punctuation +string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
# print(f"chars:{chars}")
# print(f"key:{key}")
# ENCRYPTION 
plaintext=input("Enter a message to encrypt:")
ciphertext=""
for letter in plaintext:
    index=chars.index(letter)
    ciphertext+=key[index]
print(f"original message:{plaintext}")  
print(f"encrypted message:{ciphertext}")   
# decryption 
ciphertext=input("Enter a message to dencrypt:")
plaintext=""
for letter in ciphertext:
    index=key.index(letter)
    plaintext+=chars[index]
  
print(f"encrypted message:{ciphertext}")    
print(f"original message:{plaintext}")
  
  