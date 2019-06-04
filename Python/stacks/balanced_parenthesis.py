class Stack:

	def __init__(self):
		self.stack = []
		self.braces_dict = {'(':0, '[':1, '{':2,')':0, ']':1, '}':2 }

	def isEmpty(self):
		return (self.stack == [])

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		if not self.isEmpty():
			return self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def dict_lookup(self, data1, data2):
		if self.braces_dict[data1] == self.braces_dict[data2]:
			return True
		else:
			return False

	def checkBalanced(self, exp):
		

		for i in exp:
			if self.isEmpty():
				self.push(i)
			elif self.dict_lookup(i, self.peek()):
				self.pop()
			else:
				self.push(i)

		if self.isEmpty():
			return 'balanced'
		else:
			return 'not balanced'

if __name__ == '__main__':
	k = int(input())

	for index in range(k):		
		stack = Stack()
		exp = input()

		stt = stack.checkBalanced(exp)
		print(stt)

