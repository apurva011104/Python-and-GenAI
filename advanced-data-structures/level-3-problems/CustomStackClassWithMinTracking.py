class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):

        if self.stack:
            removed = self.stack.pop()

            if removed == self.min_stack[-1]:
                self.min_stack.pop()

            return removed

    def get_min(self):
        return self.min_stack[-1]


ms = MinStack()

ms.push(3)
ms.push(5)
ms.push(2)

print(ms.get_min())