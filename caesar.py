def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift uppercase and lowercase letters separately
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Non-alphabet characters stay the same
    return result

# Example usage
text = "Hello World!"
shift = 3
encrypted_text = caesar_cipher_encrypt(text, shift)
print("Encrypted:", encrypted_text)
