# Creation of Stack
class Stack:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def isempty(self):
        if self.data == []:
            return True
        else:
            return False
    def pop(self):
        if self.isempty():
            return 'Stack Empty'
        else:
            return self.data.pop()
    def top(self):
        if self.isempty():
            return 'Stack Empty'
        else:
            return self.data[-1]
    def size(self):
        return len(self.data)

    
