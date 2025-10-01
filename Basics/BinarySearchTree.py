class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key        # The key used for sorting in the BST
        self.val = val        # The value associated with the key
        self.left = None      # Pointer to left child
        self.right = None     # Pointer to right child

#This class implements a binary search tree map using the TreeNode class. New
class TreeMap:
    def __init__(self):
        self.root = None  # Root of the BST


#Inserts a new key-value pair into the BST.
    def insert(self, key: int, val: int) -> None:
        # Create a new TreeNode
        newNode = TreeNode(key, val)
        # If the tree is empty, set the new node as root
        if self.root == None:
            self.root = newNode
            return

    # Traverse the tree to find the insertion point
        current = self.root
        while True:
            # Go left if key is smaller than current key
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            # Go right if key is greater than current key
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            # Update the value if key already exists
            else:
                current.val = val
                return

#Retrieves the value for a given key.
    def get(self, key: int) -> int:
        current = self.root
        # Traverse the tree to find the key
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1  # Return -1 if key not found

#Returns the minimum value in the BST.
    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1

#Finds the node with the minimum key.    
    def findMin(self, node: TreeNode) -> TreeNode:
    # Traverse to the leftmost node
        while node and node.left:
            node = node.left
        return node

#Returns the maximum value in the BST.
    def getMax(self) -> int:
        current = self.root
        # Traverse to the rightmost node
        while current and current.right:
            current = current.right
        return current.val if current else -1

#Removes a key-value pair from the BST.
    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

#A recursive helper function for removing a node.
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        # Base case: Node is not found
        if curr == None:
            return None

        # Recursive case: Traverse to find the node
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            # Node with only one child or no child
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            # Node with two children: Get the inorder successor
            minNode = self.findMin(curr.right)
            curr.key = minNode.key
            curr.val = minNode.val
            curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

#Returns a list of keys in inorder traversal.
    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

#A recursive helper function for inorder traversal.
    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)