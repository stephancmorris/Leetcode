#Depth-First Search (DFS) - Recursive & Iterative

def dfs_recursive(graph, start_node):
    visited = set()
    result = [] 

    def _dfs(vertex):
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in graph.get(vertex, []):
                _dfs(neighbor)
    
    _dfs(start_node)
    return result 

#Depth-First Search (DFS) - Iterative DFS (Uses a Stack)
def dfs_iterative(graph, start_node):
    if start_node not in graph:
        return [] 
    
    visited = set()
    stack = [start_node]
    result = [] 

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in reversed(graph.get(vertex, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return result 