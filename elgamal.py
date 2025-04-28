import random

def elgamal_keygen(p, g):
    x = random.randint(2, p-2)
    y = pow(g, x, p)
    return (p, g, y), x

def elgamal_encrypt(p, g, y, m):
    k = random.randint(2, p-2)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2

def elgamal_decrypt(p, x, c1, c2):
    s = pow(c1, x, p)
    s_inv = pow(s, -1, p)
    m = (c2 * s_inv) % p
    return m

p = 7919
g = 2
public_key, private_key = elgamal_keygen(p, g)
p, g, y = public_key
x = private_key
message = 1234
c1, c2 = elgamal_encrypt(p, g, y, message)
print(f"Ciphertext : (c1 = {c1} , c2 = {c2})")
decrypted_message = elgamal_decrypt(p, x, c1, c2)
print(f"Decrypted Message: {decrypted_message}")
