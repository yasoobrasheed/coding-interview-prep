from collections import defaultdict


class Graph:
    # constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.visited = {}
        for i in range(0, vertices):
            self.visited[i] = False

    # create graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # graph depth first search
    def dfs(self, u, graph):
        print(u)
        self.visited[u] = True

        for v in self.graph[u]:
            if (self.visited[v] == False):
                self.dfs(v, graph)


def __main__():
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(1, 3)
    g.addEdge(3, 2)
    g.addEdge(2, 5)
    g.addEdge(2, 4)
    g.addEdge(4, 5)
    g.dfs(0, g)  # 0 1 3 2 5 4
