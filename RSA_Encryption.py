def rsa_encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

# Given primes
p, q = 3, 11
n = p * q
phi = (p-1) * (q-1)

e = 3  # Public exponent (chosen manually here)

message = "HI"
cipher = rsa_encrypt(message, e, n)

print("Encrypted Cipher:", cipher)
print(f"Public Key: (e = {e}, n = {n})")
