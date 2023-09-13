class Stack:
    def __init__(self, limit=None):
        self.items = []
        self.limit = limit

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, value):
        if value not in self.items:
            return -1
        return self.items.index(value)

# Bonus: Uncomment the following lines if you want to test the additional methods
# stk = Stack(5)
# stk.push(1)
# stk.push(2)
# stk.push(3)
# stk.push(4)
# stk.push(5)
# print(stk.is_full())  # Should print True
# print(stk.size())     # Should print 5
# print(stk.search(3))  # Should print 2
# print(stk.search(6))  # Should print -1
