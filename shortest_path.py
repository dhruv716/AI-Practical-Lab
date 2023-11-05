import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def min_distance(self, dist, spt_set):
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_val and not spt_set[v]:
                min_val = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if not spt_set[v] and self.graph[u][v] and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]

        print("Vertex \tDistance from Source")
        for i in range(self.V):
            print(i, "\t", dist[i])

# Example usage:
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 5)
    g.add_edge(1, 3, 10)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 8)
    g.add_edge(4, 5, 6)

    source = 0

    g.dijkstra(source)
