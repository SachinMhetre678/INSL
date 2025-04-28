def rail_fence_encrypt(text, rails):
    fence = ['' for _ in range(rails)]
    rail, direction = 0, 1
    for char in text:
        fence[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return ''.join(fence)

def rail_fence_decrypt(cipher, rails):
    pattern = ['' for _ in range(len(cipher))]
    rail, direction = 0, 1
    for i in range(len(cipher)):
        pattern[i] = rail
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    pos = sorted(range(len(pattern)), key=lambda x: pattern[x])
    fence = ['' for _ in range(len(cipher))]
    idx = 0
    for r in range(rails):
        for i in range(len(cipher)):
            if pattern[i] == r:
                fence[i] = cipher[idx]
                idx += 1

    return ''.join(fence)

# Example usage
text = "HELLO WORLD"
rails = 3
cipher = rail_fence_encrypt(text.replace(' ', ''), rails)
decrypted = rail_fence_decrypt(cipher, rails)
print("Plaintext:", text)
print("Ciphertext:", cipher)
print("Decrypted:", decrypted)
