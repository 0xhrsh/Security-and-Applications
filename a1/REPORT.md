# Report 
Vernam Cipher is a method of encrypting alphabetic text, two strings: message and key of same length are used to encrypt a message.

## Encryption
0. Each alphabet in the message and the key are assigned a numerical value (same as alphabatical order in this case).
1. Add the numerical values of each character in the message with the corrosponding character of the key.
2. Subtract the number from 26 if the added number is greater than 26
3. convert this array of number to a string of characters (acc to step 0). This string is the encrypted message.

## Decryption
0. just reverse the steps of encryption.
    - Subtract the numerical values of each character in the key from the corrosponding character of the cipher text. 
    - Add the number 26 if the subtracted number is less than 0.
    - convert this array of number to a string of characters (acc to step 0 of encrpytion). This string is the decrypted message.
