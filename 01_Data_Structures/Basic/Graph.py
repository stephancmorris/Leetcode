class Graph:
    def __init__(self):
        self.adj_list = {}  # Dictionary to store adjacency list

#Adds an edge between two nodes.
    def addEdge(self, src: int, dst: int) -> None:
        # Add src and dst to the adjacency list if they don't exist
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        # Add dst to the adjacency set of src
        self.adj_list[src].add(dst)

#Removes an edge between two nodes.
    def removeEdge(self, src: int, dst: int) -> bool:
        # Check if the edge exists
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False  # Edge does not exist
        # Remove the edge
        self.adj_list[src].remove(dst)
        return True

#Checks if a path exists between two nodes using Depth-First Search (DFS).
    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()  # Set to keep track of visited nodes
        return self._dfs(src, dst, visited)  # Start DFS

#Performs the DFS to find a path.
    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True  # Path found
        visited.add(src)  # Mark the node as visited
        # Recursively visit each unvisited neighbor
        for neighbor in self.adj_list.get(src, []):
            if neighbor not in visited:
                if self._dfs(neighbor, dst, visited):
                    return True  # Path found in a deeper call
        return False  # No path found

#An alternative implementation of hasPath using Breadth-First Search (BFS).
    def hasPathBFS(self, src: int, dst: int) -> bool:
        visited = set()  # Set to keep track of visited nodes
        queue = deque([src])  # Queue for BFS
        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True  # Path found
            visited.add(curr)  # Mark the node as visited
            # Add unvisited neighbors to the queue
            for neighbor in self.adj_list.get(curr, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return False  # No path found
