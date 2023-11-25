class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val          # The value stored in the node
        self.next = next_node   # The reference to the next node; defaults to None



class LinkedList:
    def __init__(self):
        # Initialize with a dummy head node
        self.head = ListNode(-1)  # Dummy head node
        self.tail = self.head     # Initially, the tail is the same as the head

    
    def get(self, index: int) -> int:
        curr = self.head.next  # Start from the first real node
        i = 0                  # Index counter
        while curr:
            if i == index:
                return curr.val  # Return the value if index is found
            i += 1
            curr = curr.next
        return -1  # Return -1 if index is out of bounds or list is empty


    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next  # New node points to the first real node
        self.head.next = new_node       # Head now points to the new node

        if not new_node.next:  # If list was empty before insertion
            self.tail = new_node  # Update tail to new node


    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)  # Create new node and link it to the tail
        self.tail = self.tail.next      # Update tail to the new node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head  # Start from the dummy head
        while i < index and curr:
            i += 1
            curr = curr.next  # Traverse to the node before the one to be removed
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr  # Update tail if last node is being removed
            curr.next = curr.next.next  # Bypass the node to be removed
            return True
        return False  # Return False if index is out of bounds



    def getValues(self) -> List[int]:
        curr = self.head.next  # Start from the first real node
        res = []  # List to store values
        while curr:
            res.append(curr.val)  # Append each node's value to the list
            curr = curr.next
        return res  # Return the list of values

        