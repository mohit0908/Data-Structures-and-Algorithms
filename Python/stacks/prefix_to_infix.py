class Conversion:

    def __init__(self):
        self.top = -1
        self.output = []


    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        if not self.isEmpty():
            return self.output[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.output.pop()
        else:
            return '$'

    def push(self, data):
        self.top += 1
        self.output.append(data)

    def isOperand(self, data):
        return data.isalpha()


    def prefixToInfix(self, phr):
        for i in phr:
            # If character is Operand, push to output
            if self.isOperand(i):
                self.push(i)
            else:
                a = self.pop()
                b = self.pop()
                insert = "({}{}{})".format(a,i,b)
                self.push(insert)

        print('Output:',''.join(self.output))

exp = "*-A/BC-/AKL"
obj = Conversion()
obj.prefixToInfix(exp[::-1])