#3- Taking input with head and stail
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def takeInput():
    head = None
    tail = None
    ele=[int(i) for i in input().split()] #[1,2,3,-1]
    for curval in ele:
        if curval == -1:
            break
        else:
            node=Node(curval)
            if head is None:
                head = node 
                tail = node
            else:
                tail.next = node
                tail = node

    return head