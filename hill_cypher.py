import numpy as np

def hill_encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = plaintext.upper().replace(' ', '')
    while len(plaintext) % n != 0:
        plaintext += 'X'  # padding

    numbers = [ord(c) - ord('A') for c in plaintext]
    ciphertext = ''

    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        cipher_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join(chr(num + ord('A')) for num in cipher_block)
    
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = pow(det % 26, -1, 26)
    adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_key = (det_inv * adj) % 26
    numbers = [ord(c) - ord('A') for c in ciphertext]
    plaintext = ''

    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        plain_block = np.dot(inv_key, block) % 26
        plaintext += ''.join(chr(num + ord('A')) for num in plain_block)
    
    return plaintext

# Example usage
key = np.array([[3, 3], [2, 5]])
plaintext = "HELP"
cipher = hill_encrypt(plaintext, key)
decrypted = hill_decrypt(cipher, key)
print("Plaintext:", plaintext)
print("Ciphertext:", cipher)
print("Decrypted:", decrypted)
