class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # 'n' is the number of nodes in the graph
        # 'edges' is a list of edges, each edge represented as [source, destination, weight]
        # 'src' is the starting node for Dijkstra's algorithm

        adj = {}
        for i in range(n):
            adj[i] = []  # Initialize adjacency list for each node

        for s, d, w in edges:
            adj[s].append([d, w])  # Add edge to adjacency list

        shortest = {}  # Dictionary to store shortest path distance from src to each node
        minHeap = [[0, src]]  # Initialize min heap with source node and distance 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # Pop node with smallest distance
            if n1 in shortest:
                continue  # Skip if the shortest path to n1 is already found
            shortest[n1] = w1  # Assign shortest path distance to n1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])  # Push adjacent nodes with updated distances

        # Fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1  # Set distance to -1 for nodes unreachable from src

        return shortest

# Explanation of the Algorithm:
# Adjacency List: The graph is represented as an adjacency list, where each node points to a list of its neighbors and the corresponding edge weights.
# Heap: A min heap is used to efficiently retrieve the node with the smallest known distance from the source at each step.
# Shortest Paths: The algorithm maintains a dictionary shortest that maps each node to its shortest distance from the source node. This distance is finalized when the node is popped from the heap.
# Updating Distances: For each node popped from the heap, the algorithm updates the distances to its adjacent nodes if a shorter path is found.
# Unreachable Nodes: After processing all reachable nodes, the algorithm assigns a distance of -1 to nodes that are unreachable from the source.
# Usefulness in LeetCode Questions:
# Dijkstra's algorithm is a fundamental algorithm in graph theory and is widely used in problems involving shortest paths.
# Understanding this algorithm is crucial for solving various network routing, map navigation, and graph traversal problems.
# The implementation demonstrates important concepts such as graph representation, priority queues (heaps), and greedy algorithms.