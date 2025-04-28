class HashTable:
    def __init__(self):
        self.table = {}  # Python's built-in dictionary acts as our hash table

    def insert(self, key, value):
        """Insert or update key-value pair."""
        self.table[key] = value

    def search(self, key):
        """Search for a value by key."""
        return self.table.get(key, None)  # Returns None if key is not found

    def delete(self, key):
        """Delete a key-value pair."""
        if key in self.table:
            del self.table[key]
            return True
        return False

    def display(self):
        """Display the entire hash table."""
        for key, value in self.table.items():
            print(f"{key}: {value}")

# Example usage:
ht = HashTable()
# Insert some key-value pairs
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)
# Insert a duplicate key to test updating the value
ht.insert("banana", 25)
# Search for a key
print("Search for 'banana':", ht.search("banana"))  # Should return 25
# Delete a key
ht.delete("apple")
# Display the hash table
ht.display()
