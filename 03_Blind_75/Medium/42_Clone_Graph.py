"""
LeetCode 133. Clone Graph
Difficulty: Medium
Category: Graphs

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    """
    Create deep copy of graph.
    
    Args:
        node: Reference node of original graph
        
    Returns:
        Reference node of cloned graph
    """
    # TODO: Implement your solution here
    pass
