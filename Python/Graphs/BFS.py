from collections import defaultdict, deque

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	# function to add edge to graph

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def printGraph(self):
		print(self.graph)

	def BFS(self, s):

		# create empty list for storing visited vertices
		visited =  []

		# Create queue for BFS
		queue = deque()

		# Mark source node as visited and enque it
		queue.append(s)
		visited.append(s)
		print('Visited: ', s)
		while queue:
			# Dequeue the vertex from queue beginning and pop it
			s= queue.popleft()
			for i in self.graph[s]:
				if i not in visited:
					queue.append(i)
					visited.append(i)
					# Print each visited vertex
					print('Visited: ', i)

if __name__ == '__main__':
	g = Graph()
	
	# g.addEdge(1, 2) 
	# g.addEdge(1, 3) 
	# g.addEdge(1, 4) 
	# g.addEdge(3, 5) 


	# g.addEdge(1,2)
	# g.addEdge(1,3)
	# g.addEdge(2,1)
	# g.addEdge(2,5)
	# g.addEdge(2,4)
	# g.addEdge(3,1)
	# g.addEdge(3,5)
	# g.addEdge(4,2)
	# g.addEdge(4,5)
	# g.addEdge(4,6)
	# g.addEdge(5,3)
	# g.addEdge(5,2)
	# g.addEdge(5,4)
	# g.addEdge(5,6)
	# g.addEdge(6,4)
	# g.addEdge(6,5)
	# g.printGraph()
	# g.BFS(1)

	g.addEdge(0,1)
	g.addEdge(0,2)
	g.addEdge(1,2)
	g.addEdge(2,3)
	g.addEdge(3,1)
	g.addEdge(3,2)
	g.printGraph()
	g.BFS(3)

