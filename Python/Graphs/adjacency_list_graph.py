# Python program to represent adjacency list implementation of graph


# Basic code for creating node of a linked list
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None



class Graph:
    def __init__(self, V):
        self.V = V
        # Create list of None equal to number of vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        # Create node
        node = AdjNode(dest)
        # Check if src is None otherwise read till end of linked list
        if self.graph[src] is None:
            self.graph[src] = node
        else:
            temp = self.graph[src]
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        
        # Create node
        node = AdjNode(src)
        # Check if desc is None otherwise read till end of linked list. 
        # Perform reverse of above process for undirectional graph
        if self.graph[dest] is None:
            self.graph[dest] = node
        else:
            temp = self.graph[dest]
            while temp.next is not None:
                temp = temp.next
            temp.next = node


    def print_graph(self):
        for i in range(self.V):
            print('Adjancey list for head {}'.format(i))
            temp = self.graph[i]

            while temp:
                print('--> {}'.format(temp.vertex))
                temp = temp.next

V = 5
graph = Graph(V) 
graph.add_edge(0, 1) 
graph.add_edge(0, 4) 
graph.add_edge(1, 2) 
graph.add_edge(1, 3) 
graph.add_edge(1, 4) 
graph.add_edge(2, 3) 
graph.add_edge(3, 4) 

graph.print_graph()