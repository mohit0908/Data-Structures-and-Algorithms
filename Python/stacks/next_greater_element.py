class Stack:

	def __init__(self):
		self.top = -1
		self.stack = []
		self.max_list = []

	def isEmpty(self):
		return (self.stack == [])

	def pop(self):
		if not self.isEmpty():
			return self.stack.pop()

	def push(self, data):
		self.stack.append(data)

	def peek(self):
		return self.stack[-1]


	def findGreaterElement(self, input_list):
		result_dict = {}
		stack = []

		for element in input_list:
			if self.isEmpty():
				self.push(element)
			elif not self.isEmpty():
				while (not self.isEmpty() and element > self.peek()):
					self.max_list.append([self.pop(), element])
				self.push(element)

		while not self.isEmpty():
			self.max_list.append([self.pop(), -1])		

		print('Stack:', self.stack)
		print('Max:', self.max_list)


if __name__ == '__main__':

	k = int(input())

	for iter in range(k):
		input_len = int(input())
		input_list = list(map(int, input().strip().split()))
		stack = Stack()
		stack.findGreaterElement(input_list)
