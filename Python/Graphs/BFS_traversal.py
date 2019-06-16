from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        print(self.graph)

    def BFS(self, start):
        visit_list = dict.fromkeys(self.graph.keys(), False)
        queue = deque()
        queue.append(start)
        visit_list[start] = True

        while queue:
            node = queue.popleft()
            print('Pop:', node)
            for ele in self.graph[node]:
                if not visit_list[ele]:
                    queue.append(ele)
                    visit_list[ele] = True

g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,5)
g.addEdge(2,4)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(5,6)
g.print_graph()
g.BFS(3)
