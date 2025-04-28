def rsa(cipher, d, n):
    return ''.join(chr(pow(c, d, n)) for c in cipher)

p, q = 3, 11
n = p * q
phi = (p - 1) * (q - 1)
e = 3

d = pow(e, -1, phi)  # modular inverse

cipher = [18, 31]
decrypted_message = rsa(cipher, d, n)

print("Decrypted Message:", decrypted_message)
print(f"Private Key (d={d}, n={n})")
