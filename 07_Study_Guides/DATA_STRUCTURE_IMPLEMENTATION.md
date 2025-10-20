# Data Structure Implementation Guide

## 📚 Implementation Checklist

For each data structure, ensure you can:

### ✅ Basic Operations
- [ ] Implement from scratch without looking
- [ ] Handle edge cases (empty, single element)
- [ ] Explain time/space complexity
- [ ] Write clean, readable code
- [ ] Add proper error handling

### ✅ Advanced Features
- [ ] Handle duplicates appropriately
- [ ] Implement iterators/enumerators
- [ ] Add size/length tracking
- [ ] Implement equality comparison
- [ ] Add serialization/deserialization

## 🔧 Implementation Templates

### Array/Dynamic Array
```python
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity
    
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]
    
    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = value
    
    def push_back(self, value):
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1
    
    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
```

### Linked List
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add_at_head(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def add_at_tail(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
```

### Hash Map
```python
class HashMap:
    def __init__(self):
        self.capacity = 16
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.size += 1
        
        if self.size > self.capacity * 0.75:
            self._resize()
    
    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
```

### Stack
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

### Queue
```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

### Binary Tree
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if not node.left:
                node.left = TreeNode(val)
                return
            elif not node.right:
                node.right = TreeNode(val)
                return
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)
```

### Heap (Min Heap)
```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, index):
        while index > 0:
            parent = self.parent(index)
            if self.heap[index] >= self.heap[parent]:
                break
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
    
    def _heapify_down(self, index):
        while True:
            smallest = index
            left = self.left_child(index)
            right = self.right_child(index)
            
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == index:
                break
            
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
```

## 🎯 Practice Problems

### Arrays
- Implement dynamic array with resize
- Implement circular buffer
- Implement sparse array

### Linked Lists
- Reverse linked list (iterative and recursive)
- Detect cycle in linked list
- Merge two sorted linked lists
- Remove nth node from end

### Hash Maps
- Implement LRU Cache
- Implement LFU Cache
- Design hash map with custom hash function

### Stacks & Queues
- Implement stack using two queues
- Implement queue using two stacks
- Implement min stack
- Implement circular queue

### Trees
- Validate binary search tree
- Find lowest common ancestor
- Serialize and deserialize binary tree
- Implement trie

### Heaps
- Implement priority queue
- Find kth largest element
- Merge k sorted lists

## 💡 Common Mistakes to Avoid

1. **Off-by-one errors** in array indexing
2. **Null pointer exceptions** in linked lists
3. **Infinite loops** in tree traversals
4. **Memory leaks** in dynamic structures
5. **Incorrect complexity analysis**
6. **Not handling edge cases**
7. **Poor variable naming**
8. **Missing error handling**

## 🔍 Interview Tips

1. **Start with the interface** - Define the public methods first
2. **Handle edge cases** - Empty structures, single elements
3. **Explain complexity** - Time and space for each operation
4. **Test your implementation** - Walk through examples
5. **Consider trade-offs** - Different implementations for different use cases
6. **Be ready for follow-ups** - Variations and optimizations
