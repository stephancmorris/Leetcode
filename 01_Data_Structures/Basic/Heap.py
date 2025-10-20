class MinHeap:
    def __init__(self):
        self.heap = [0]  # Initialize heap with a dummy value at index 0 to simplify parent-child calculations
    
#Inserts a new value into the heap and maintains the heap property.        
    def push(self, val: int) -> None:
        """Pushes a value onto the heap."""
        self.heap.append(val)  # Add the new value to the end of the heap
        self._bubble_up(len(self.heap) - 1)  # Adjust the heap to maintain the heap property


#Removes and returns the smallest value from the heap.
    def pop(self) -> int:
        """Pops the smallest value off the heap."""
        if len(self.heap) <= 1:
            return -1  # Return -1 if the heap is empty
        if len(self.heap) == 2:
            return self.heap.pop()  # If heap has only one value, pop and return it
        
        # Swap the root with the last element and bubble it down
        root = self.heap[1]  # Save the root value
        self.heap[1] = self.heap.pop()  # Move the last element to the root
        self._bubble_down(1)  # Adjust the heap to maintain the heap property
        return root  # Return the original root value

        
#Returns the smallest value in the heap without removing it.
    def top(self) -> int:
        """Returns the smallest value without popping it."""
        return self.heap[1] if len(self.heap) > 1 else -1  # Return the root value or -1 if the heap is empty

        
#Transforms a list into a heap.
    def heapify(self, nums: List[int]) -> None:
        """Transforms a list into a heap in-place."""
        self.heap = [0] + nums  # Add dummy value at index 0 and append input list
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._bubble_down(i)  # Adjust each non-leaf node to maintain the heap property


#Adjusts the heap upwards to maintain the heap property after insertion.
    def _bubble_up(self, index: int) -> None:
        parent = index // 2  # Calculate parent index
        while index > 1 and self.heap[parent] > self.heap[index]:
            # Swap if parent is greater than the current node
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent  # Move up to the parent
            parent = index // 2  # Recalculate parent


#Adjusts the heap downwards to maintain the heap property after removal.
    def _bubble_down(self, index: int) -> None:
        child = 2 * index  # Calculate left child index
        while child < len(self.heap):
            # Choose the smaller child if right child exists and is smaller
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child += 1

            # If the current node is smaller than its smallest child, the heap property is satisfied
            if self.heap[child] >= self.heap[index]:
                break

            # Swap the current node with its smallest child
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child  # Move down to the child
            child = 2 * index  # Recalculate left child

        
        