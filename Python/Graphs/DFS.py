from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.stack = []
        self.visiting_list = []
    # Function to add edge in graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        print('Adjacency list graph: ',self.graph)

    def DFS(self, s):

        # Push initial node to stack and visiting list
        self.stack.append(s)
        self.visiting_list.append(s)
        print('Visiting: ', s)

        while self.stack:
            ele = self.stack[-1]
            if ele not in self.graph:
                self.stack.pop()
            for i in self.graph[ele]:
                count = 0
                if i not in self.visiting_list and count <=1:
                    self.stack.append(i)
                    self.visiting_list.append(i)
                    print('Visiting: ', i)
                    count += 1
                elif self.stack != []:
                        self.stack.pop()

if __name__ == '__main__':
    g = Graph()

    g.addEdge(1, 2) 
    g.addEdge(1, 3) 
    g.addEdge(1, 4) 
    g.addEdge(3, 5)  
    g.printGraph()
    g.DFS(1)


 