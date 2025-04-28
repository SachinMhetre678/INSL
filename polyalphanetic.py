def polyalphabetic_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_length = len(key)
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            new_char = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += new_char
        else:
            ciphertext += plaintext[i]  # keep spaces and symbols as they are
    return ciphertext

# Example usage
plaintext = "HELLO WORLD"
key = "KEY"
ciphertext = polyalphabetic_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
