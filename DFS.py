# Define a class to represent a graph
class Graph:
    def __init__(self):
        self.graph = {}
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    # Recursive function for DFS
    def dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # DFS traversal starting from a given vertex
    def dfs_traversal(self, start_vertex):
        visited = set()
        self.dfs(start_vertex, visited)

# Now, let's implement BFS using a queue
from collections import deque

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("DFS traversal starting from vertex 2:")
    g.dfs_traversal(2)
    print("\nBFS traversal starting from vertex 2:")
    bfs(g.graph, 2)
