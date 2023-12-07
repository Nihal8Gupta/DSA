#Creation of Queue by list
class Queue:
    def __init__(self):
        self.container = []
        self.count = 0
    def enque(self,data):
        self.container.append(data)
    def isEmpty(self):
        return True if not self.container else False
    def deque(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            return self.container.pop(0)
    def front(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            return self.container[0]
    def size(self):
        return len(self.container)
obj = Queue()
obj.isEmpty()
obj.enque(60)
obj.isEmpty()
obj.deque()
obj.deque()
obj.size()