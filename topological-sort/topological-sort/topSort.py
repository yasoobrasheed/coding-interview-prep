from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.visited = {}
        for i in range(0, vertices):
            self.visited[i] = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topSort(self):
        order = [0] * 13
        endIndex = self.V - 1

        for i in range(0, self.V):
            if (self.visited[i] == False):
                endIndex = self.dfs(i, order, endIndex)

        return order

    def dfs(self, u, order, endIndex):
        self.visited[u] = True

        for v in self.graph[u]:
            if (self.visited[v] == False):
                endIndex = self.dfs(v, order, endIndex)

        order[endIndex] = u
        return endIndex - 1


def __main__():
    g = Graph(13)
    g.addEdge(0, 3)
    g.addEdge(1, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(3, 7)
    g.addEdge(3, 6)
    g.addEdge(4, 0)
    g.addEdge(4, 3)
    g.addEdge(4, 5)
    g.addEdge(5, 10)
    g.addEdge(5, 9)
    g.addEdge(6, 8)
    g.addEdge(7, 8)
    g.addEdge(7, 9)
    g.addEdge(8, 11)
    g.addEdge(9, 11)
    g.addEdge(9, 12)
    arr = g.topSort()
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    for num in arr:
        print(letters[num], end=" ")
    # E F K C B A D G H J M I L
