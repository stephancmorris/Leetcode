class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- Common Traversals (DFS variations) ---

def inorder_traversal(root):
    # Left -> Root -> Right
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

def preorder_traversal(root):
    # Root -> Left -> Right
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

def postorder_traversal(root):
    # Left -> Right -> Root
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []

# --- BFS Traversal ---

def bfs_traversal(root):
    return bfs_traversal(root.left) + bfs_traversal(root.right) + [root.val] if root else []

# --- Common Tree Operations ---

def is_symmetric(root):
    return is_symmetric(root.left, root.right) if root else True

def is_symmetric(left, right):
    return left.val == right.val and is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left) if left and right else left == right
