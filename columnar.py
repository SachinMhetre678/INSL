def simple_columnar_encrypt(message, key):
    message = message.replace(" ", "").upper()
    num_cols = len(key)
    num_rows = -(-len(message) // num_cols)  # Ceiling division
    
    # Fill matrix row-wise
    matrix = [['X' for _ in range(num_cols)] for _ in range(num_rows)]
    k = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if k < len(message):
                matrix[i][j] = message[k]
                k += 1
    
    # Create ciphertext by reading columns based on key order
    ciphertext = ""
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    for index, _ in key_order:
        for row in matrix:
            ciphertext += row[index]
    
    return ciphertext

# Example usage
message = "HELLO WORLD"
key = [4, 3, 1, 2, 5, 6, 7]  # based on example
cipher_text = simple_columnar_encrypt(message, key)
print("Encrypted:", cipher_text)
