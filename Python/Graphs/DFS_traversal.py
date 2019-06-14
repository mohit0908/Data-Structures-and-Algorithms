from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.stack = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printgraph(self):
        print(self.graph)

    def BFS(self, ele):
        self.visited_list = dict.fromkeys(self.graph.keys(), False)

        self.stack.append(ele)
        self.visited_list[ele] = True
        print('printing :', ele)
        
        while self.stack:
            self.visit_status = False
            initial = self.stack[-1]
            for node in self.graph[initial]:
                print('Inside stack:', self.stack)
                if self.visited_list[node] == False:
                    self.stack.append(node)
                    self.visited_list[node] = True
                    print('printing inside:', node)
                    break
                else:
                    self.visit_status = True
                    self.stack.pop()



g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(4,6)
g.addEdge(4,7)
g.addEdge(5,7)
g.addEdge(6,8)
g.addEdge(7,8)
g.printgraph()
g.BFS(0)
