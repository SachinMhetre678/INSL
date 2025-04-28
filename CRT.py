def chinese_remainder_theorem(a, m):
    total = 0
    M = 1  # product of moduli
    for mi in m:
        M *= mi

    for ai, mi in zip(a, m):
        Mi = M // mi
        Mi_inv = pow(Mi, -1, mi)  # using built-in pow() with 3 arguments for modular inverse
        total += ai * Mi * Mi_inv

    return total % M

# Example
a = [2, 3, 1]
m = [3, 5, 7]

solution = chinese_remainder_theorem(a, m)
print(f"The solution to the system of congruences is x = {solution}")
