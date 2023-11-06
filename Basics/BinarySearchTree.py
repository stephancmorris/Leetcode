class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:  
            self.root - TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = TreeNode(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right = TreeNode(key)
            else:
                self._insert_recursive(current_node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, current_node, key):
        if current_node is None:
            return False #Key is not found
        if key == current_node.val:
            return True #Key found
        elif key < current_node.val:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

# Example usage:
bst = BinarySearchTree()
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(2)

# Search for a value
print(bst.search(4))  # Output: True
print(bst.search(5))  # Output: False