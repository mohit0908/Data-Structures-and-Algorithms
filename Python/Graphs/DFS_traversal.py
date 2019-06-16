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

    def dfs_traversal(self, start):
        self.visit_list = dict.fromkeys(self.graph.keys(), False)

        self.stack.append(start)
        self.visit_list[start] = True
        print('Visited ', start)
        while self.stack:
            top = self.stack[-1]
            for ele in self.graph[top]:
                visit_flag = True
                if not self.visit_list[ele]:
                    visit_flag = False
                    self.stack.append(ele)
                    print('Visited ', ele)
                    self.visit_list[ele] = True
                    break
            if visit_flag == True:
                self.stack.pop()



g = Graph()

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,5)
g.addEdge(2,4)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(5,6)

# g.addEdge(0,1)
# g.addEdge(0,2)
# g.addEdge(1,3)
# g.addEdge(1,4)
# g.addEdge(2,4)
# g.addEdge(2,5)
# g.addEdge(3,6)
# g.addEdge(4,6)
# g.addEdge(4,7)
# g.addEdge(5,7)
# g.addEdge(6,8)
# g.addEdge(7,8)
g.printgraph()
g.dfs_traversal(1)



