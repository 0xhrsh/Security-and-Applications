def validate(message, key):
    if len(message) != len(key):
        print("Error: message and key must be the same length")
        exit()
    for x in range(len(message)):
        if ord(message[x]) < ord('A') or ord(message[x]) > ord('Z'):
            print("Error: message must be upper case")
            exit()
        if ord(key[x]) < ord('A') or ord(key[x]) > ord('Z'):
            print("Error: key must be upper case")
            exit()


def encrypt(message, key):
    validate(message, key)

    ciphertext = ""
    for i in range(len(message)):
        sume = ord(message[i]) + ord(key[i]) - ord('A')
        if sume > 26 + ord('A'):
            ciphertext += chr(sume - 26)
        else:
            ciphertext += chr(sume)
    return ciphertext


def decrypt(ciphertext, key):
    validate(ciphertext, key)

    message = ""
    for i in range(len(ciphertext)):
        diff = ord(ciphertext[i]) - ord(key[i])
        if diff < 0:
            message += chr(diff + 26 + ord('A'))
        else:
            message += chr(diff + ord('A'))
    return message


message = "IITJODHPUR"
key = "VERYSECRET"

cipher = encrypt(message, key)
print("Cipher text:", cipher)
print("Decrypted Message: ", decrypt(cipher, key))
