#Creation of linked list
class linked:
    def __init__(self,data): #creation of node
        self.data=data
        self.next=None
obj1=linked(12)             #first node
print('obj1,Add:',obj1)
print('obj1.data=',obj1.data,'obj1.next=',obj1.next)
obj2=linked(13)             #second node
print('obj2 Add:',obj2)
print('obj2.data=',obj2.data,'obj2.next=',obj2.next)
obj1.next=obj2              #connection of node
print('obj1.data=',obj1.data,'obj1.next=',obj1.next)
print('obj1.next.data=',obj1.next.data)         #connected