def hellman(p, g, a, b):
    A = pow(g, a, p)  # Alice's public key
    B = pow(g, b, p)  # Bob's public key

    shared_key_a = pow(B, a, p)  # Alice computes shared key
    shared_key_b = pow(A, b, p)  # Bob computes shared key

    assert shared_key_a == shared_key_b, "Keys do not match!"

    return A, B, shared_key_a

# Example values
p = 23
g = 5
a = 6
b = 15

A, B, shared_key = hellman(p, g, a, b)

print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")
print(f"Shared secret key: {shared_key}")
