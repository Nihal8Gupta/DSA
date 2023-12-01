#Reverse the stack by recursion
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
    
    def reverse(self,data=[]):  #reverse logic
        if self.size() == 0:
            return 
        data.append(self.pop())
        self.reverse()
        self.push(data.pop(0))

obj = Stack() 
obj.push(11)
obj.push(12)
obj.push(13)
print('Normal stack:')
while obj.size() != 0:
    print(obj.pop(),end=' ')
obj.push(11)
obj.push(12)
obj.push(13)
obj.reverse()
print()
print('After reverse:')
while obj.size() != 0:
    print(obj.pop(),end=' ')