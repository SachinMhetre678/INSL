def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()
    for char in key:
        if char not in used and char.isalpha():
            used.add(char)
            matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Note: No J
        if char not in used:
            used.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def prepare_text(text):
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        if i+1 < len(text):
            char2 = text[i+1]
            if char1 == char2:
                prepared += char1 + 'X'
                i += 1
            else:
                prepared += char1 + char2
                i += 2
        else:
            prepared += char1 + 'X'
            i += 1
    return prepared

def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = prepare_text(text)
    encrypted = ""
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:
            encrypted += matrix[row1][(col1 + 1) % 5]
            encrypted += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted += matrix[(row1 + 1) % 5][col1]
            encrypted += matrix[(row2 + 1) % 5][col2]
        else:
            encrypted += matrix[row1][col2]
            encrypted += matrix[row2][col1]
    return encrypted

# Example usage
key = "playfair example"
text = "hide the gold"
cipher_text = playfair_encrypt(text, key)
print("Encrypted:", cipher_text)
