class Node:
    def __init__(self, key: int, value: int):
        self.key = key        # The key associated with the node
        self.value = value    # The value associated with the key
        self.next = None      # Pointer to the next node (for handling collisions)


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity  # The initial capacity of the hash table
        self.size = 0             # Number of elements in the hash table
        self.table = [None] * self.capacity  # The hash table array with 'None' initial values

#Calculates the hash for a given key.
    def hash_function(self, key: int) -> int:
        return key % self.capacity  # Simple modulo-based hash function

#Inserts a new key-value pair into the hash table.
    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)  # Get hash index for the key
        node = self.table[index]

        if not node:
            # Insert new node if no node exists at index
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            # Handle collision with linked list chaining
            prev = None
            while node:
                if node.key == key:
                    # Update value if key already exists
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)  # Append new node at the end of the chain
            self.size += 1

        # Resize table if load factor is greater than 0.5
        if self.size / self.capacity >= 0.5:
            self.resize()


#Retrieves the value for a given key.
    def get(self, key: int) -> int:
        index = self.hash_function(key)  # Get hash index for the key
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value  # Return value if key is found
            node = node.next

        return -1  # Return -1 if key not found

#Removes a key-value pair from the hash table.
    def remove(self, key: int) -> bool:
        index = self.hash_function(key)  # Get hash index for the key
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next  # Remove node from chain
                else:
                    self.table[index] = node.next  # Set table entry to next node
                self.size -= 1
                return True
            prev, node = node, node.next

        return False  # Return False if key not found

#Returns the current size of the hash table.
    def getSize(self) -> int:
        return self.size

#Returns the current capacity of the hash table.
    def getCapacity(self) -> int:
        return self.capacity

#Doubles the size of the hash table and rehashes all elements.
    def resize(self) -> None:
        new_capacity = self.capacity * 2  # Double the capacity
        new_table = [None] * new_capacity  # Create new table with new capacity

        # Rehash all nodes to the new table
        for node in self.table:
            while node:
                index = node.key % new_capacity  # Get new index
                # Insert node into new table
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next

        self.capacity = new_capacity  # Update capacity
        self.table = new_table        # Replace old table with new table


