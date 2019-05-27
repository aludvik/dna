from collections import deque

class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__edges = []

    def add_edge(self, v):
        self.__edges.append(v)

    def remove_edge(self, v):
        self.__edges.remove(v)

    def data(self):
        return self.__data

    def neighbors(self):
        return self.__edges[:]

class Graph:
    def __init__(self):
        self.__nodes = []
        self.__free = []

    def size(self):
        return len(self.__nodes) - len(self.__free)

    def node(self, u):
        assert(u < self.size())
        return self.__nodes[u]

    def add_node(self, data):
        if self.__free:
            reused = self.__free.pop()
            self.__nodes[reused] = Node(data)
            return reused

        self.__nodes.append(Node(data))
        return len(self.__nodes) - 1

    def remove_node(self, u):
        for v in self.__nodes[u].neighbors():
            self.__nodes[v].remove_edge(u)
        self.__nodes[u] = None
        self.__free.append(u)

    def add_edge(self, u, v):
        self.__nodes[u].add_edge(v)
        self.__nodes[v].add_edge(u)

    def remove_edge(self, u, v):
        self.__nodes[u].remove_edge(v)
        self.__nodes[v].remove_edge(u)

    def dfs(self, start):
        stack = [start]
        visited = [False] * len(self.__nodes)
        order = []
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                order.append(u)
                for v in self.__nodes[u].neighbors():
                    stack.append(v)
        return order

    def bfs(self, start):
        queue = deque([start])
        visited = [False] * len(self.__nodes)
        order = []
        while queue:
            u = queue.popleft()
            if not visited[u]:
                visited[u] = True
                order.append(u)
                for v in self.__nodes[u].neighbors():
                    queue.append(v)
        return order

    def shortest_path(self, start, end):
        queue = deque([(start, 0)])
        visited = [False] * len(self.__nodes)
        while queue:
            u, d = queue.popleft()
            if u == end:
                return d
            if not visited[u]:
                visited[u] = True
                for v in self.__nodes[u].neighbors():
                    queue.append((v, d+1))
        return -1
