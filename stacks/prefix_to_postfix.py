class Conversion:

	def __init__(self):
		self.output = []

	def isEmpty(self):
		return self.output == []

	def push(self, data):
		self.output.append(data)

	def pop(self):
		if not self.isEmpty():
			return self.output.pop()

	def peek(self):
		if not self.isEmpty():
			return self.output[-1]
	def isOperand(self, data):
		return data.isalpha()

	def prefix_to_postfix(self, phr):

		for i in phr:

			if self.isOperand(i):
				self.push(i)
			else:
				a = self.pop()
				b = self.pop()
				insert = "{}{}{}".format(a,b,i)
				self.push(insert)


		print('Output:', ''.join(self.output))




exp = "*-A/BC-/AKL"
obj = Conversion()
obj.prefix_to_postfix(exp[::-1])