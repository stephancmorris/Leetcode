class Node:
    def __init__(self, value):
        self.value = value  # Stores the value of the node
        self.next = None    # Pointer to the next node; initialized as None
        self.prev = None    # Pointer to the previous node; initialized as None


class Deque:
    def __init__(self):
        # Create two dummy nodes: head and tail
        self.head = Node(-1)  # Dummy head node
        self.tail = Node(-1)  # Dummy tail node

        # Link the dummy head and tail nodes
        self.head.next = self.tail  # Head points to tail
        self.tail.prev = self.head  # Tail points back to head

    def isEmpty(self) -> bool:
    #Checks if the deque is empty.
        return self.head.next == self.tail  # Returns True if no elements between head and tail

    def append(self, value) -> None:
    #Adds an element to the end of the deque.
        new_node = Node(value) # Create a new node
        last_node = self.tail.prev # Get the current last node

        #Insert the new node before the tail
        last_node.next = new_node #Last node's next points to the new node
        new_node.prev = last_node #New node's prev points to last node
        new_node.next = self.tail #New node's next points to the dummy tail
        self.tail.prev = new_node #Tail's prev points to new node

    def appendleft(self, value) -> None:
    #Adds an element to the beginning of the deque.
        new_node = Node(value) #Create a new node
        first_node = self.head.next #Get the current first node

       # Insert the new node after the head
        self.head.next = new_node      # Head's next points to new node
        new_node.prev = self.head      # New node's prev points to head
        new_node.next = first_node     # New node's next points to first node
        first_node.prev = new_node     # First node's prev points to new node
    
    def pop(self) -> int:
        if self.isEmpty():             # Check if deque is empty
            return -1                  # Return -1 if empty

        last_node = self.tail.prev     # Get the last node
        value = last_node.value        # Store its value

        # Remove the last node
        prev_node = last_node.prev     # Get the node before the last node
        prev_node.next = self.tail     # Set its next to tail
        self.tail.prev = prev_node     # Tail's prev points to prev_node

        return value                   # Return the removed value

    def popleft(self) -> int:
        if self.isEmpty():             # Check if deque is empty
            return -1                  # Return -1 if empty

        first_node = self.head.next    # Get the first node
        value = first_node.value       # Store its value

        # Remove the first node
        next_node = first_node.next    # Get the node after the first node
        self.head.next = next_node     # Head's next points to next_node
        next_node.prev = self.head     # Next_node's prev points to head

        return value                   # Return the removed value
